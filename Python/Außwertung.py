herzfrequenz = 100  #bpm
blutdruck = 100
koerpertemperatur = 100
sauerstoffsaetigung = 100
schlafdauer = 100
knochendichte = 100
ernaeung = 100
strahlungsbelastung = 100
muskelabbau = 100
galaktische_kosmische_strahlung = 100

max_herzfrequenz = 130
min_herzfrequenz = 50

max_first_int_blutdruck = 140
max_second_int_blutdruck = 90
min_first_int_blutdruck = 90
min_second_int_blutdruck = 60

def is_in_danger_herzfrequenz(herzfrequenz=70):
    if herzfrequenz > max_herzfrequenz or herzfrequenz < min_herzfrequenz:
        auswertung = True
    else:
        auswertung = False
    return auswertung

def is_in_danger_blutdruck(blutdruck="120/80"):
    teile = blutdruck.split("/")
    first_int = int(teile[0])
    second_int = int(teile[1])
    if first_int > max_first_int_blutdruck or second_int > max_second_int_blutdruck:
        auswertung = True
    elif first_int < min_first_int_blutdruck or second_int < min_second_int_blutdruck:
        auswertung = True
    else:
        auswertung = False
    return auswertung

print(is_in_danger_blutdruck("90/60"))