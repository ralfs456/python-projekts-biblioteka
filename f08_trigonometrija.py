# Funkcija 8: math.sin(), math.cos(), math.tan()
# Trigonometriskās funkcijas - izmanto leņķus radiānos

import math

def piemers():
    lenki = 30  # grādi
    radiani = math.radians(lenki)  # pārvērš grādus radiānos

    print(f"Leņķis: {lenki} grādi")
    print(f"sin({lenki}°) = {round(math.sin(radiani), 4)}")
    print(f"cos({lenki}°) = {round(math.cos(radiani), 4)}")
    print(f"tan({lenki}°) = {round(math.tan(radiani), 4)}")

piemers()
