# Funkcija 14: math.isfinite(), math.isinf(), math.isnan()
# Pārbauda vai skaitlis ir normāls, bezgalīgs vai "nav skaitlis"

import math

def piemers():
    normāls = 42.0
    bezgaligs = math.inf
    nan = math.nan

    print(f"{normāls} ir normāls skaitlis: {math.isfinite(normāls)}")
    print(f"Bezgalība ir bezgalīga: {math.isinf(bezgaligs)}")
    print(f"math.nan ir 'nav skaitlis': {math.isnan(nan)}")

piemers()
