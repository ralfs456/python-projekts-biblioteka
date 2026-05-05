# Funkcija 12: math.exp()
# Aprēķina e pakāpē x (e ir Eilera skaitlis ≈ 2.718)

import math

def piemers():
    x = 3
    rezultats = math.exp(x)
    print(f"e pakāpē {x} = {round(rezultats, 4)}")
    print(f"(e = {round(math.e, 4)})")

piemers()
