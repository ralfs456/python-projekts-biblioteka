# Funkcija 15: math.comb()
# Aprēķina kombināciju skaitu - cik veidos var izvēlēties k elementus no n

import math

def piemers():
    n = 10  # kopējais skaits
    k = 3   # cik izvēlamies
    rezultats = math.comb(n, k)
    print(f"Cik veidos var izvēlēties {k} no {n}?")
    print(f"Atbilde: {rezultats} veidos")

piemers()
