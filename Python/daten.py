import json
import os
import time
from datetime import datetime




folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Astronauten")

files = [
    ("send_data_glover.json", "critical_data_glover.json"),
    ("send_data_hansen.json", "critical_data_hansen.json"),
    ("send_data_koch.json", "critical_data_koch.json"),
    ("send_data_wiseman.json", "critical_data_wiseman.json"),
]

def check_bpm(bpm):
    if bpm < 50:
        return f"Puls zu niedrig: {bpm:g} BPM"

    if bpm > 120:
        return f"Puls zu hoch: {bpm:g} BPM"

def check_blood_pressure(systole, diastole):
    if systole > 145 or diastole > 90:
        return f"Blutdruck zu hoch: {systole:g}/{diastole:g}"
           
    if systole < 100 or diastole < 68:
        return f"Blutdruck zu niedrig: {systole:g}/{diastole:g}"

def check_temperature(temp):
    if temp > 38.5:
        return f"Fieber: {temp:g} °C"
    if temp > 38:
        return f"Erhöhte Temperatur: {temp:g} °C"
    if temp < 37:
        return f"Unterkühlung: {temp:g} °C"

def check_oxygen(oxygen):
    if oxygen < 95:
        return f"Sauerstoffsättigung zu niedrig: {oxygen:g} %"

def check_sleep(hours):
    if hours < 6:
        return f"Zu wenig Schlaf: {hours:g} h"

def check_bone(current, initial):
    if initial > 0 and current < initial * 0.9:
        return f"Knochendichte um {(1 - current / initial) * 100:.0f} % gesunken"

def check_muscle(current, initial):
    if initial > 0 and current < initial * 0.9:
        return f"Muskelkraft um {(1 - current / initial) * 100:.0f} % gesunken"

def check_radiation(radiation):
    if radiation > 1:
        return f"Strahlenbelastung hoch: {radiation:g}"

def check_weight(weight):
    if weight < 50:
        return f"Gewicht zu niedrig: {weight:g} kg"

checks = [
    (["BPM"], check_bpm),
    (["Systole", "Diastole"], check_blood_pressure),
    (["Bodytemperature"], check_temperature),
    (["Oxygen-Saturation"], check_oxygen),
    (["Sleep-Duration"], check_sleep),
    (["Bone-Density", "Initial-Bone-Density"], check_bone),
    (["Muscle-Strength", "Initial-Muscle-Strength"], check_muscle),
    (["Radiation-Exposure"], check_radiation),
    (["Weight"], check_weight),
]

def get_latest(data):
    if isinstance(data, dict):
        return data
    if isinstance(data, list) and data:
        return max(data, key=lambda entry: datetime.fromisoformat(entry["timestamp"]))
    return {}

def evaluate(data):
    def get_value(key):
        try:
            return float(data[key])
        except (KeyError, ValueError, TypeError):
            return None

    warnings = []
    for fields, function in checks:
        values = [get_value(field) for field in fields]
        if None in values:
            continue
        warning = function(*values)
        if warning:
            warnings.append(warning)

    return {
        "alarm": len(warnings) > 0,
        "warnings": warnings
    }
while True:
    for input_file, output_file in files:
        try:
            with open(os.path.join(folder, input_file), "r", encoding="utf-8") as f:
                data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            continue

        result = evaluate(get_latest(data))

        with open(os.path.join(folder, output_file), "w", encoding="utf-8") as f:
            json.dump(result, f, ensure_ascii=False, indent=4)

        from flask import send_from_directory

    @app.route("/astronaut-data/<filename>")
    def astronaut_data(filename):
        return send_from_directory("Astronauten", filename)
    time.sleep(0.1)





