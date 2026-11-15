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

def check_bpm(bpm, location):
    if location == "Raumstation":
        if bpm < 50:
            return f"Puls zu niedrig: {bpm:g} BPM"

        if bpm > 120:
            return f"Puls zu hoch: {bpm:g} BPM"

    if location == "Montstation":
        if bpm < 50:
            return f"Puls zu niedrig: {bpm:g} BPM"

        if bpm > 120:
            return f"Puls zu hoch: {bpm:g} BPM"

def check_blood_pressure(systole, diastole, location):
    if location == "Raumstation":
        if systole > 145 or diastole > 90:
            return f"Blutdruck zu hoch: {systole:g}/{diastole:g}"
            
        if systole < 100 or diastole < 68:
            return f"Blutdruck zu niedrig: {systole:g}/{diastole:g}"

    if location == "Montstation":
        if systole > 145 or diastole > 90:
            return f"Blutdruck zu hoch: {systole:g}/{diastole:g}"
            
        if systole < 100 or diastole < 68:
            return f"Blutdruck zu niedrig: {systole:g}/{diastole:g}"

def check_temperature(temp, location):
    if location == "Raumstation":
        if temp > 38.5:
            return f"Fieber: {temp:g} °C"
        if temp > 38:
            return f"Erhöhte Temperatur: {temp:g} °C"
        if temp < 37:
            return f"Unterkühlung: {temp:g} °C"

    if location == "Montstation":
        if temp > 38.5:
            return f"Fieber: {temp:g} °C"
        if temp > 38:
            return f"Erhöhte Temperatur: {temp:g} °C"
        if temp < 37:
            return f"Unterkühlung: {temp:g} °C"

def check_oxygen(oxygen, location):
    if location == "Raumstation":
        if oxygen < 95:
            return f"Sauerstoffsättigung zu niedrig: {oxygen:g} %"

    if location == "Montstation":
        if oxygen < 95:
            return f"Sauerstoffsättigung zu niedrig: {oxygen:g} %"

def check_sleep(hours, location):
    if location == "Raumstation":
        if hours < 6:
            return f"Zu wenig Schlaf: {hours:g} h"

    if location == "Montstation":
        if hours < 6:
            return f"Zu wenig Schlaf: {hours:g} h"

def check_bone(current, initial, location):
    initial = 1.1
    if location == "Raumstation":
        if initial > 0 and current < initial * 0.9:
            return f"Knochendichte um {(1 - current / initial) * 100:.0f} % gesunken"

    if location == "Montstation":
        if initial > 0 and current < initial * 0.9:
            return f"Knochendichte um {(1 - current / initial) * 100:.0f} % gesunken"

def check_radiation(radiation, location):
    if location == "Raumstation":
        if radiation > 1:
            return f"Strahlenbelastung hoch: {radiation:g}"

    if location == "Montstation":
        if radiation > 1:
            return f"Strahlenbelastung hoch: {radiation:g}"

def check_weight(weight, location):
    if location == "Raumstation":
        if weight < 55:
            return f"Gewicht zu niedrig: {weight:g} kg"

    if location == "Montstation":
        if weight < 55:
            return f"Gewicht zu niedrig: {weight:g} kg"

def check_fluid(fluid, location):
    if location == "Raumstation":
        if fluid < 2000:
            return f"Zu wenig getrunken: {fluid:g} ml"

        if fluid > 4500:
            return f"Achtung vor Wasservergiftung: {fluid:g} ml"

    if location == "Montstation":
        if fluid < 2500:
            return f"Zu wenig getrunken: {fluid:g} ml"

        if fluid > 5000:
            return f"Achtung vor Wasservergiftung: {fluid:g} ml"

def check_energy(energy, location):
    if location == "Raumstation":
        if energy < 2250:
            return f"Zu wenig Energie: {energy:g} kcal"

        if energy > 2750 :
            return f"Zu viel Energie: {energy:g} kcal"

    if location == "Montstation":
        if energy < 2250:
            return f"Zu wenig Energie: {energy:g} kcal"

        if energy > 2750:
            return f"Zu viel Energie: {energy:g} kcal"

def check_vitamin_a(vitamin_a, location):   
    if location == "Raumstation":
        if vitamin_a < 1000:
            return f"Zu wenig Vitamin A: {vitamin_a:g} µg"

    if location == "Montstation":
        if vitamin_a < 900:
            return f"Zu wenig Vitamin A: {vitamin_a:g} µg"

def check_vitamin_d(vitamin_d, location):
    if location == "Raumstation":
        if vitamin_d < 10:
            return f"Zu wenig Vitamin D: {vitamin_d:g} µg"

    if location == "Montstation":
        if vitamin_d < 25:
            return f"Zu wenig Vitamin D: {vitamin_d:g} µg"


def check_vitamin_k(vitamin_k, location):
    if location == "Raumstation":
        if vitamin_k < 80:
            return f"Zu wenig Vitamin K: {vitamin_k:g} µg"

    if location == "Montstation":
        if vitamin_k < 120:
            return f"Zu wenig Vitamin K: {vitamin_k:g} µg"


def check_vitamin_e(vitamin_e, location):
    if location == "Raumstation":
        if vitamin_e < 20:
            return f"Zu wenig Vitamin E: {vitamin_e:g} mg"

    if location == "Montstation":
        if vitamin_e < 15:
            return f"Zu wenig Vitamin E: {vitamin_e:g} mg"


def check_vitamin_c(vitamin_c, location):
    if location == "Raumstation":
        if vitamin_c < 100:
            return f"Zu wenig Vitamin C: {vitamin_c:g} mg"

    if location == "Montstation":
        if vitamin_c < 125:
            return f"Zu wenig Vitamin C: {vitamin_c:g} mg"


def check_vitamin_b12(vitamin_b12, location):
    if location == "Raumstation":
        if vitamin_b12 < 2.0:
            return f"Zu wenig Vitamin B12: {vitamin_b12:g} µg"

    if location == "Montstation":
        if vitamin_b12 < 2.4:
            return f"Zu wenig Vitamin B12: {vitamin_b12:g} µg"


def check_vitamin_b6(vitamin_b6, location):
    if location == "Raumstation":
        if vitamin_b6 < 2.0:
            return f"Zu wenig Vitamin B6: {vitamin_b6:g} mg"

    if location == "Montstation":
        if vitamin_b6 < 1.3:
            return f"Zu wenig Vitamin B6: {vitamin_b6:g} mg"


def check_carbohydrates(carbohydrates, location):
    if location == "Raumstation":
        if carbohydrates < 312.5:
            return f"Zu wenig Kohlenhydrate: {carbohydrates:g} g"

        if carbohydrates > 343.8:
            return f"Zu viele Kohlenhydrate: {carbohydrates:g} g"

    if location == "Montstation":
        if carbohydrates < 281.3:
            return f"Zu wenig Kohlenhydrate: {carbohydrates:g} g"

        if carbohydrates > 406.3:
            return f"Zu viele Kohlenhydrate: {carbohydrates:g} g"


def check_protein(protein, location):
    if location == "Raumstation":
        if protein < 75:
            return f"Zu wenig Protein: {protein:g} g"

        if protein > 93.8:
            return f"Zu viel Protein: {protein:g} g"

    if location == "Montstation":
        if protein < 90:
            return f"Zu wenig Protein: {protein:g} g"

        if protein > 135:
            return f"Zu viel Protein: {protein:g} g"


def check_fat(fat, location):
    if location == "Raumstation":
        if fat < 83.3:
            return f"Zu wenig Fett: {fat:g} g"

        if fat > 97.2:
            return f"Zu viel Fett: {fat:g} g"

    if location == "Montstation":
        if fat < 55.6:
            return f"Zu wenig Fett: {fat:g} g"

        if fat > 97.2:
            return f"Zu viel Fett: {fat:g} g"


def check_magnesium(magnesium, location):
    if location == "Raumstation":
        if magnesium < 350:
            return f"Zu wenig Magnesium: {magnesium:g} mg"

    if location == "Montstation":
        if magnesium < 420:
            return f"Zu wenig Magnesium: {magnesium:g} mg"


def check_iron(iron, location):
    if location == "Raumstation":
        if iron >= 10:
            return f"Zu viel Eisen: {iron:g} mg"

    if location == "Montstation":
        if iron < 8:
            return f"Zu wenig Eisen: {iron:g} mg"


def check_zinc(zinc, location):
    if location == "Raumstation":
        if zinc < 15:
            return f"Zu wenig Zink: {zinc:g} mg"

    if location == "Montstation":
        if zinc < 11:
            return f"Zu wenig Zink: {zinc:g} mg"


def check_calcium(calcium, location):
    if location == "Raumstation":
        if calcium < 1200:
            return f"Zu wenig Calcium: {calcium:g} mg"

        if calcium > 2000:
            return f"Zu viel Calcium: {calcium:g} mg"

    if location == "Montstation":
        if calcium < 1000:
            return f"Zu wenig Calcium: {calcium:g} mg"

        if calcium > 1200:
            return f"Zu viel Calcium: {calcium:g} mg"

def check_sport(sport, location):
    if location == "Raumstation":
        if sport < 2:
            return f"Zu wenig Sport: {sport:g} h"

    if location == "Montstation":
        if sport < 2:
            return f"Zu wenig Sport: {sport:g} h"
        
checks = [
    (["BPM", "Measurement-Location"], check_bpm),
    (["Systole", "Diastole", "Measurement-Location"], check_blood_pressure),
    (["Bodytemperature", "Measurement-Location"], check_temperature),
    (["Oxygen-Saturation", "Measurement-Location"], check_oxygen),
    (["Sleep-Duration", "Measurement-Location"], check_sleep),
    (["Bone-Density", "Measurement-Location"], check_bone),
    (["Sport-Duration", "Measurement-Location"], check_sport),
    (["Radiation-Exposure", "Measurement-Location"], check_radiation),
    (["Weight", "Measurement-Location"], check_weight),
    (["Fluid", "Measurement-Location"], check_fluid),
    (["Energy", "Measurement-Location"], check_energy),
    (["Protein", "Measurement-Location"], check_protein),
    (["Carbonhydrates", "Measurement-Location"], check_carbohydrates),
    (["Fat", "Measurement-Location"], check_fat),
    (["Iron", "Measurement-Location"], check_iron),
    (["Zinc", "Measurement-Location"], check_zinc),
    (["Magnesium", "Measurement-Location"], check_magnesium),
    (["Calcium", "Measurement-Location"], check_calcium),
    (["Vitamin-A", "Measurement-Location"], check_vitamin_a),
    (["Vitamin-B6", "Measurement-Location"], check_vitamin_b6),
    (["Vitamin-B12", "Measurement-Location"], check_vitamin_b12),
    (["Vitamin-C", "Measurement-Location"], check_vitamin_c),
    (["Vitamin-D", "Measurement-Location"], check_vitamin_d),
    (["Vitamin-E", "Measurement-Location"], check_vitamin_e),
    (["Vitamin-K", "Measurement-Location"], check_vitamin_k)
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

    time.sleep(0.1)