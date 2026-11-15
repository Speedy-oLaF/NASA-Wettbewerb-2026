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


# Werte innen
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

min_muskelkraft_prozent = 80

min_sport = 1.5

# Werte außen
max_herzfrequenz_außen = 120
min_herzfrequenz_außen = 50

max_first_int_blutdruck_außen = 135
max_second_int_blutdruck_außen = 85
min_first_int_blutdruck_außen = 90
min_second_int_blutdruck_außen = 60

max_koerpertemperatur_außen = 37.3
min_koerpertemperatur_außen = 35.8

min_sauerstoffsaetigung_außen = 95

min_schlafdauer_außen = 7

min_knochendichte_außen = 0.95

max_ernaeung_außen = 3800
min_ernaeung_außen = 2500

max_strahlungsbelastung_außen = 0.9

min_muskelkraft_prozent_außen = 90

min_sport_außen = 1.5

def is_in_danger_herzfrequenz(herzfrequenz=70, innen_1_oder_außen_2=1):
    match innen_1_oder_außen_2:
        case 1:
            if herzfrequenz > max_herzfrequenz or herzfrequenz < min_herzfrequenz:
                auswertung = True
            else:
                auswertung = False
        case 2:
            if herzfrequenz > max_herzfrequenz_außen or herzfrequenz < min_herzfrequenz_außen:
                auswertung = True
            else:
                auswertung = False
        case _:
            return None
    return auswertung

def is_in_danger_blutdruck(blutdruck="120/80", innen_1_oder_außen_2=1):
    teile = blutdruck.split("/")
    try:
        first_int = float(teile[0])
        second_int = float(teile[1])
    except (ValueError, IndexError):
        print("Du hast etwas falsch Eingegeben!")
        return None

    match innen_1_oder_außen_2:
        case 1:
            if first_int > max_first_int_blutdruck or second_int > max_second_int_blutdruck:
                auswertung = True
            elif first_int < min_first_int_blutdruck or second_int < min_second_int_blutdruck:
                auswertung = True
            else:
                auswertung = False
        case 2:
            if first_int > max_first_int_blutdruck_außen or second_int > max_second_int_blutdruck_außen:
                auswertung = True
            elif first_int < min_first_int_blutdruck_außen or second_int < min_second_int_blutdruck_außen:
                auswertung = True
            else:
                auswertung = False
        case _:
            return None
    return auswertung

def is_in_danger_koerpertemperatur(koerpertemperatur=36.5, innen_1_oder_außen_2=1):
    match innen_1_oder_außen_2:
        case 1:
            if koerpertemperatur > max_koerpertemperatur or koerpertemperatur < min_koerpertemperatur:
                auswertung = True
            else:
                auswertung = False
        case 2:
            if koerpertemperatur > max_koerpertemperatur_außen or koerpertemperatur < min_koerpertemperatur_außen:
                auswertung = True
            else:
                auswertung = False
        case _:
            return None
    return auswertung

def is_in_danger_sauerstoffsaetigung(sauerstoffsaetigung=98, innen_1_oder_außen_2=1):
    match innen_1_oder_außen_2:
        case 1:
            if sauerstoffsaetigung < min_sauerstoffsaetigung:
                auswertung = True
            else:
                auswertung = False
        case 2:
            if sauerstoffsaetigung < min_sauerstoffsaetigung_außen:
                auswertung = True
            else:
                auswertung = False
        case _:
            return None
    return auswertung

def is_in_danger_schlafdauer(schlafdauer=7, innen_1_oder_außen_2=1):
    match innen_1_oder_außen_2:
        case 1:
            if schlafdauer < min_schlafdauer:
                auswertung = True
            else:
                auswertung = False
        case 2:
            if schlafdauer < min_schlafdauer_außen:
                auswertung = True
            else:
                auswertung = False
        case _:
            return None
    return auswertung

def is_in_danger_knochendichte(aktuelle_knochendichte=1.0, anfangs_knochendichte=1.0, innen_1_oder_außen_2=1):
    match innen_1_oder_außen_2:
        case 1:
            if anfangs_knochendichte * min_knochendichte >= aktuelle_knochendichte:
                auswertung = True
            else:
                auswertung = False
        case 2:
            if anfangs_knochendichte * min_knochendichte_außen >= aktuelle_knochendichte:
                auswertung = True
            else:
                auswertung = False
        case _:
            return None
    return auswertung

def is_in_danger_ernaeung(ernaerung=2500, innen_1_oder_außen_2=1):
    match innen_1_oder_außen_2:
        case 1:
            if ernaerung > max_ernaeung or ernaerung < min_ernaeung:
                auswertung = True
            else:
                auswertung = False
        case 2:
            if ernaerung > max_ernaeung_außen or ernaerung < min_ernaeung_außen:
                auswertung = True
            else:
                auswertung = False
        case _:
            return None
    return auswertung

def is_in_danger_strahlungsbelastung(strahlungsbelastung=1.0, innen_1_oder_außen_2=1):
    match innen_1_oder_außen_2:
        case 1:
            if strahlungsbelastung > max_strahlungsbelastung_innen:
                auswertung = True
            else:
                auswertung = False
        case 2:
            if strahlungsbelastung > max_strahlungsbelastung_außen:
                auswertung = True
            else:
                auswertung = False
        case _:
            return None
    return auswertung

def is_in_danger_muskelkraft(muskelkraft=450.0, ausgangswert=450.0, innen_1_oder_außen_2=1):
    if ausgangswert <= 0:
        return None

    match innen_1_oder_außen_2:
        case 1:
            if muskelkraft / ausgangswert * 100 < min_muskelkraft_prozent:
                auswertung = True
            else:
                auswertung = False
        case 2:
            if muskelkraft / ausgangswert * 100 < min_muskelkraft_prozent_außen:
                auswertung = True
            else:
                auswertung = False
        case _:
            return None
    return auswertung

def is_in_danger_sport(sport=1.3, innen_1_oder_außen_2=1):
    match innen_1_oder_außen_2:
        case 1:
            if sport < min_sport:
                auswertung = True
            else:
                auswertung = False
        case 2:
            if sport < min_sport_außen:
                auswertung = True
            else:
                auswertung = False
        case _:
            return None
    return auswertung


def is_allowed_to_work_Raumstation(messwerte):
    probleme = []

    if is_in_danger_herzfrequenz(messwerte["herzfrequenz"]) != False:
        probleme.append("herzfrequenz")

    if is_in_danger_blutdruck(messwerte["blutdruck"]) != False:
        probleme.append("blutdruck")

    if is_in_danger_koerpertemperatur(messwerte["koerpertemperatur"]) != False:
        probleme.append("koerpertemperatur")

    if is_in_danger_sauerstoffsaetigung(messwerte["sauerstoffsaetigung"]) != False:
        probleme.append("sauerstoffsaetigung")

    if is_in_danger_schlafdauer(messwerte["schlafdauer"]) != False:
        probleme.append("schlafdauer")

    if is_in_danger_knochendichte(messwerte["knochendichte"], messwerte["anfangs_knochendichte"]) != False:
        probleme.append("knochendichte")

    if is_in_danger_ernaeung(messwerte["ernaehrung"]) != False:
        probleme.append("ernaehrung")

    if is_in_danger_strahlungsbelastung(messwerte["strahlungsbelastung"], 1) != False:  # 1 = innen
        probleme.append("strahlungsbelastung")

    if is_in_danger_muskelkraft(messwerte["muskelkraft"], messwerte["muskelkraft_ausgangswert"]) != False:
        probleme.append("muskelkraft")

    if is_in_danger_sport(messwerte["sport"]) != False:
        probleme.append("sport")

    if len(probleme) == 0:
        return True
    else:
        return False, probleme

def is_allowed_to_work_Montstation(messwerte):
    probleme = []

    if is_in_danger_herzfrequenz(messwerte["herzfrequenz"], 2) != False:
        probleme.append("herzfrequenz")

    if is_in_danger_blutdruck(messwerte["blutdruck"], 2) != False:
        probleme.append("blutdruck")

    if is_in_danger_koerpertemperatur(messwerte["koerpertemperatur"], 2) != False:
        probleme.append("koerpertemperatur")

    if is_in_danger_sauerstoffsaetigung(messwerte["sauerstoffsaetigung"], 2) != False:
        probleme.append("sauerstoffsaetigung")

    if is_in_danger_schlafdauer(messwerte["schlafdauer"], 2) != False:
        probleme.append("schlafdauer")

    if is_in_danger_knochendichte(messwerte["knochendichte"], messwerte["anfangs_knochendichte"], 2) != False:
        probleme.append("knochendichte")

    if is_in_danger_ernaeung(messwerte["ernaehrung"], 2) != False:
        probleme.append("ernaehrung")

    if is_in_danger_strahlungsbelastung(messwerte["strahlungsbelastung"], 2) != False:
        probleme.append("strahlungsbelastung")

    if is_in_danger_muskelkraft(messwerte["muskelkraft"], messwerte["muskelkraft_ausgangswert"], 2) != False:
        probleme.append("muskelkraft")

    if is_in_danger_sport(messwerte["sport"], 2) != False:
        probleme.append("sport")

    if len(probleme) == 0:
        return True
    else:
        return False, probleme
