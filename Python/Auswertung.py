# herzfrequenz          bpm
# blutdruck             mmHg
# koerpertemperatur     °C
# sauerstoffsaetigung   %
# schlafdauer           h
# knochendichte         g/cm²
# ernaehrung            kcal
# strahlungsbelastung   mSv
# muskelkraft           N
# sport                 h


max_herzfrequenz = 130
min_herzfrequenz = 50

max_first_int_blutdruck = 140
max_second_int_blutdruck = 90
min_first_int_blutdruck = 90
min_second_int_blutdruck = 60

max_koerpertemperatur = 37.5
min_koerpertemperatur = 35.5

min_sauerstoffsaetigung = 92

min_schlafdauer = 6

min_knochendichte = 0.9

max_ernaeung = 3200
min_ernaeung = 2000

max_strahlungsbelastung_innen = 1.3
min_strahlungsbelastung_außen = 0.9

min_muskelkraft_prozent = 80

min_sport = 1.3

def is_in_danger_herzfrequenz(herzfrequenz=70):
    if herzfrequenz > max_herzfrequenz or herzfrequenz < min_herzfrequenz:
        auswertung = True
    else:
        auswertung = False
    return auswertung

def is_in_danger_blutdruck(blutdruck="120/80"):
    teile = blutdruck.split("/")
    try:
        first_int = float(teile[0])
        second_int = float(teile[1])
    except ValueError:
        print("Du hast etwas falsch Eingegeben!")
        return None

    if first_int > max_first_int_blutdruck or second_int > max_second_int_blutdruck:
        auswertung = True
    elif first_int < min_first_int_blutdruck or second_int < min_second_int_blutdruck:
        auswertung = True
    else:
        auswertung = False
    return auswertung

def is_in_danger_koerpertemperatur(koerpertemperatur=36.5):
    if koerpertemperatur > max_koerpertemperatur or koerpertemperatur < min_koerpertemperatur:
        auswertung = True
    else:
        auswertung = False
    return auswertung

def is_in_danger_sauerstoffsaetigung(sauerstoffsaetigung=98):
    if sauerstoffsaetigung < min_sauerstoffsaetigung:
        auswertung = True
    else:
        auswertung = False
    return auswertung

def is_in_danger_schlafdauer(schlafdauer=7):
    if schlafdauer < min_schlafdauer:
        auswertung = True
    else:
        auswertung = False
    return auswertung

def is_in_danger_knochendichte(aktuelle_knochendichte=1.0, anfangs_knochendichte=1.0):
    if anfangs_knochendichte*min_knochendichte < aktuelle_knochendichte:
        auswertung = True
    else:
        auswertung = False
    return auswertung

def is_in_danger_ernaeung(ernaerung=2500):
    if ernaerung > max_ernaeung or ernaerung < min_ernaeung:
        auswertung = True
    else:
        auswertung = False
    return auswertung

def is_in_danger_strahlungsbelastung(strahlungsbelastung=1.0, innen_1_oder_außen_2=1):
    match innen_1_oder_außen_2:
        case 1:
            if strahlungsbelastung > max_strahlungsbelastung_innen:
                auswertung = True
            else:
                auswertung = False
        case 2:
            if strahlungsbelastung > min_strahlungsbelastung_außen:
                auswertung = True
            else:
                auswertung = False
        case _:
            return None
    return auswertung

def is_in_danger_muskelkraft(muskelkraft=450.0, ausgangswert=450.0):
    if ausgangswert <= 0:
        return None
    if muskelkraft / ausgangswert * 100 < min_muskelkraft_prozent:
        auswertung = True
    else:
        auswertung = False
    return auswertung

def is_in_danger_sport(sport=1.3):
    if sport < min_sport:
        auswertung = True
    else:
        auswertung = False
    return auswertung