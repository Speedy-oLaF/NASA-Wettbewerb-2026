import json
from pathlib import Path

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

datei = Path("astronauten.json")
datei_bereit = Path("bereit.json")

 
class Werte(BaseModel):
    herzfrequenz: float | None = None
    blutdruck: str | None = None
    koerpertemperatur: float | None = None
    sauerstoffsaetigung: float | None = None
    schlafdauer: float | None = None
    knochendichte: float | None = None
    anfangs_knochendichte: float | None = None
    ernaehrung: float | None = None
    strahlungsbelastung: float | None = None
    muskelkraft: float | None = None
    muskelkraft_ausgangswert: float | None = None
    sport: float | None = None


class AstronautNeu(BaseModel):
    name: str
    werte: Werte = Werte()


class Bereit(BaseModel):
    bereit_innen: bool | None = None
    bereit_aussen: bool | None = None


def laden(pfad=datei):
    if pfad.exists():
        return {int(k): v for k, v in json.loads(pfad.read_text(encoding="utf-8")).items()}
    return {}


def speichern(pfad=datei, daten=None):
    if daten is None:
        daten = astronauten
    pfad.write_text(json.dumps(daten, indent=2, ensure_ascii=False), encoding="utf-8")


astronauten = laden()
bereit = laden(datei_bereit)


def finden(astronaut_id):
    if astronaut_id not in astronauten:
        raise HTTPException(status_code=404, detail="Astronaut nicht gefunden")
    return astronauten[astronaut_id]


@app.get("/astronauten")
def alle_astronauten():
    return astronauten


@app.post("/astronauten", status_code=201)
def astronaut_anlegen(neu: AstronautNeu):
    neue_id = max(astronauten, default=0) + 1
    astronauten[neue_id] = {"name": neu.name, "werte": neu.werte.model_dump()}
    speichern()
    return {"id": neue_id, **astronauten[neue_id]}


@app.get("/astronauten/{astronaut_id}")
def astronaut_holen(astronaut_id: int):
    return finden(astronaut_id)


@app.patch("/astronauten/{astronaut_id}/werte")
def werte_aendern(astronaut_id: int, werte: Werte):
    astronaut = finden(astronaut_id)
    astronaut["werte"].update(werte.model_dump(exclude_unset=True))
    speichern()
    return astronaut


@app.delete("/astronauten/{astronaut_id}")
def astronaut_loeschen(astronaut_id: int):
    finden(astronaut_id)
    del astronauten[astronaut_id]
    speichern()
    bereit.pop(astronaut_id, None)
    speichern(datei_bereit, bereit)
    return {"geloescht": astronaut_id}


def bereit_holen_oder_standard(astronaut_id):
    return bereit.get(astronaut_id, {"bereit_innen": False, "bereit_aussen": False})


@app.get("/bereit")
def alle_bereit():
    return bereit


@app.get("/bereit/{astronaut_id}")
def bereit_holen(astronaut_id: int):
    finden(astronaut_id)
    return bereit_holen_oder_standard(astronaut_id)


@app.post("/bereit/{astronaut_id}")
def bereit_setzen(astronaut_id: int, werte: Bereit):
    finden(astronaut_id)
    eintrag = bereit_holen_oder_standard(astronaut_id)
    eintrag.update(werte.model_dump(exclude_unset=True))
    bereit[astronaut_id] = eintrag
    speichern(datei_bereit, bereit)
    return eintrag