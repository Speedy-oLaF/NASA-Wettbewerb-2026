import json
import os
import subprocess
import sys

ordner = os.path.dirname(os.path.abspath(__file__))

# Neuesten Datensatz von send_data.py holen
ausgabe = subprocess.run(
    [sys.executable, os.path.join(ordner, "send_data.py")],
    capture_output=True, text=True
).stdout
daten = json.loads(ausgabe)


def wert(key):
    """Gibt den Wert als Zahl zurück, oder None, wenn er fehlt/ungültig ist."""
    try:
        return float(daten[key])
    except (KeyError, ValueError, TypeError):
        return None


# ---------- Einzelne Prüfungen ----------
# Jede Funktion gibt eine Warnung (Text) oder None zurück.

def pruefe_bpm(bpm):
    if bpm < 50 or bpm >3120:
        return f"Puls auffällig: {bpm:g} BPM"

def pruefe_blutdruck(sys_, dia):
    if sys_ > 145 or dia > 90:
        return f"Blutdruck zu hoch: {sys_:g}/{dia:g}"
    if sys_ < 100 or dia < 68:
        return f"Blutdruck zu niedrig: {sys_:g}/{dia:g}"

def pruefe_temperatur(t):
    if t < 38.5 or t > 38:
        return f"Erhöhte Temperatur: {t:g} °C"
    if t > 38.5:
        return f"Fieber: {t:g} °C"
    if t < 37:
        return f"Unterkühlung: {t:g} °C"

def pruefe_sauerstoff(o2):
    if o2 < 95:
        return f"Sauerstoffsättigung zu niedrig: {o2:g} %"

def pruefe_schlaf(h):
    if h < 6:
        return f"Zu wenig Schlaf: {h:g} h"

def pruefe_knochen(aktuell, anfang):
    if anfang > 0 and aktuell < anfang * 0.9:
        return f"Knochendichte um {(1 - aktuell / anfang) * 100:.0f} % gesunken"

def pruefe_muskeln(aktuell, anfang):
    if anfang > 0 and aktuell < anfang * 0.9:
        return f"Muskelkraft um {(1 - aktuell / anfang) * 100:.0f} % gesunken"

def pruefe_strahlung(s):
    if s > 1:
        return f"Strahlenbelastung hoch: {s:g}"


# Welche Prüfung braucht welche Felder?
pruefungen = [
    (["BPM"],                              pruefe_bpm),
    (["Systole", "Diastole"],              pruefe_blutdruck),
    (["Bodytemperature"],                  pruefe_temperatur),
    (["Oxygen-Saturation"],                pruefe_sauerstoff),
    (["Sleep-Duration"],                   pruefe_schlaf),
    (["Bone-Density", "Initial-Bone-Density"],         pruefe_knochen),
    (["Muscle-Strength", "Initial-Muscle-Strength"],   pruefe_muskeln),
    (["Radiation-Exposure"],               pruefe_strahlung),
]

# ---------- Auswertung ----------
geprueft = []
warnungen = []

for felder, funktion in pruefungen:
    werte = [wert(f) for f in felder]
    if None in werte:
        continue                      # Daten fehlen -> Prüfung ignorieren
    geprueft.extend(felder)
    warnung = funktion(*werte)
    if warnung:
        warnungen.append(warnung)

print(json.dumps({
    "alarm": len(warnungen) > 0,
    "warnungen": warnungen,
    "geprueft": geprueft
}, ensure_ascii=False))

pfad = os.path.join(os.path.dirname(os.path.abspath(__file__)), "critical_data.json")

with open(pfad, "w", encoding="utf-8") as file:
    json.dump({
    "alarm": len(warnungen) > 0,
    "warnungen": warnungen,
    "geprueft": geprueft
}, file, ensure_ascii=False)