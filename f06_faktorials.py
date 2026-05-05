# Funkcija 6: math.factorial()
# Aprēķina skaitļa faktoriālu (piemēram, 5! = 5x4x3x2x1)

import math

def piemers():
    skaitlis = 6
    rezultats = math.factorial(skaitlis)
    print(f"{skaitlis}! (faktoriāls) = {rezultats}")

piemers()
