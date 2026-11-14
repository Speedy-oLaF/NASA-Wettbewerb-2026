# Webserver und connection zu html
from flask import Flask, render_template, request, jsonify
import pandas as pd
import numpy as np
import sqlite3
import Auswertung
from datetime import datetime, date
import json
import os
import logging
from pathlib import Path

#Speicherort der Projektdateien
BASE_DIR = Path(__file__).resolve().parent
WEBSITE_DIR = BASE_DIR.parent / "Website"

# Kontrolle der Pfade
print("Python-Ordner:", BASE_DIR)
print("Website-Ordner:", WEBSITE_DIR)
print("Website existiert:", WEBSITE_DIR.exists())
print("HTML-Dateien:", list(WEBSITE_DIR.glob("*.html")))

#Flask initialisieren
app = Flask(
    __name__,
    template_folder=str(WEBSITE_DIR),
    static_folder=str(WEBSITE_DIR)
)

#Website Routen

#Hauptseite
@app.route("/")
def home():
    return render_template("index.html")

#Datenseite
@app.route("/data")
def data():
    return render_template("vitalMeasurements.html")

#API: Gesundheitswerte auswerten
@app.route("/api/auswertung", methods=["POST"])
def auswertung_api():

    try:
        # Daten von der Website empfangen
        daten = request.get_json()

        if not isinstance(daten, dict):
            return jsonify({
                "status": "fehler",
                "fehler": "Keine gültigen JSON-Daten empfangen."
            }), 400

        # Einzelne Werte auslesen
        herzfrequenz = float(daten["herzfrequenz"])
        blutdruck = str(daten["blutdruck"])
        koerpertemperatur = float(daten["koerpertemperatur"])
        sauerstoffsaettigung = float(daten["sauerstoffsaettigung"])
        schlafdauer = float(daten["schlafdauer"])

        knochendichte = float(daten["knochendichte"])
        anfangs_knochendichte = float(daten["anfangs_knochendichte"])

        ernaehrung = float(daten["ernaehrung"])

        strahlungsbelastung = float(daten["strahlungsbelastung"])
        bereich = int(daten["bereich"])

        muskelkraft = float(daten["muskelkraft"])
        ausgangswert_muskelkraft = float(daten["ausgangswert_muskelkraft"])

        sport = float(daten["sport"])

        # AUSWERTUNG DURCH auswertung.html
        bewertung = {

            "herzfrequenz":
                Auswertung.is_in_danger_herzfrequenz(herzfrequenz),

            "blutdruck":
                Auswertung.is_in_danger_blutdruck(blutdruck),

            "koerpertemperatur":
                Auswertung.is_in_danger_koerpertemperatur(koerpertemperatur),

            "sauerstoffsaettigung":
                Auswertung.is_in_danger_sauerstoffsaetigung(sauerstoffsaettigung),

            "schlafdauer":
                Auswertung.is_in_danger_schlafdauer(schlafdauer),

            "knochendichte":
                Auswertung.is_in_danger_knochendichte(
                    knochendichte, anfangs_knochendichte
                ),

            "ernaehrung":
                Auswertung.is_in_danger_ernaeung(ernaehrung),

            "strahlungsbelastung":
                Auswertung.is_in_danger_strahlungsbelastung(
                    strahlungsbelastung, bereich
                ),

            "muskelkraft":
                Auswertung.is_in_danger_muskelkraft(
                    muskelkraft, ausgangswert_muskelkraft
                ),

            "sport":
                Auswertung.is_in_danger_sport(sport)
        }

        # Ergebnisse an die Website zurückgeben
        return jsonify({
            "status": "erfolgreich",
            "bewertung": bewertung
        })

    except (KeyError, ValueError, TypeError) as fehler:

        return jsonify({
            "status": "fehler",
            "fehler": str(fehler)
        }), 400


#Server Starten
if __name__ == "__main__":
    app.run(debug=True)

