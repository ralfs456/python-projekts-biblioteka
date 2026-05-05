# Funkcija 5: math.pi
# Matemātiskā konstante PI (apļa laukuma aprēķināšanai)

import math

def piemers():
    rādiuss = 5
    laukums = math.pi * rādiuss ** 2
    print(f"PI vērtība: {math.pi}")
    print(f"Apļa laukums ar rādiusu {rādiuss}: {round(laukums, 2)}")

piemers()
