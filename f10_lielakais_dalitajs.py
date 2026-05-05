# Funkcija 10: math.gcd()
# Aprēķina divu skaitļu lielāko kopīgo dalītāju

import math

def piemers():
    a = 48
    b = 18
    rezultats = math.gcd(a, b)
    print(f"Lielākais kopīgais dalītājs ({a}, {b}) = {rezultats}")

piemers()
