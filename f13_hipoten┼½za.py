# Funkcija 13: math.hypot()
# Aprēķina taisnleņķa trijstūra hipotenūzu pēc Pitagora teorēmas

import math

def piemers():
    a = 3  # katete
    b = 4  # katete
    c = math.hypot(a, b)  # hipotenūza
    print(f"Trijstūris ar katetēm {a} un {b}")
    print(f"Hipotenūza = {c}")

piemers()
