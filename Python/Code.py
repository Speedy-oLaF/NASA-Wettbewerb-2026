# Webserver und connection zu html
from flask import Flask, render_template, request, jsonify

#Datenverarbeitung
import pandas as pd
import numpy as np

#Datenbank
import sqlite3

#Datum und Uhrzeit
from datetime import datetime, date

#Daten und Dateien verwalten
import json
import os

#Fehlerprotokoll
import logging

#Flask Konfiguration
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
    return render_template("data.html")

#Server Starten
if __name__ == "__main__":
    app.run(debug=True)

from Auswertung import werte_auswerten

ergebnis = werte_auswerten(messwerte)

