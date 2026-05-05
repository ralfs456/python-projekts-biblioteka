# Funkcija 9: math.radians() un math.degrees()
# Pārvērš grādus radiānos un otrādi

import math

def piemers():
    grādi = 180
    radiani = math.radians(grādi)
    atpakaļ = math.degrees(radiani)

    print(f"{grādi} grādi = {radiani} radiāni")
    print(f"{radiani} radiāni = {atpakaļ} grādi")

piemers()
