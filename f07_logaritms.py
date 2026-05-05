# Funkcija 7: math.log()
# Aprēķina logaritmu (pēc noklusējuma dabiskais logaritms)

import math

def piemers():
    skaitlis = 100
    dabiskais = math.log(skaitlis)       # dabiskais logaritms (bāze e)
    desmitais = math.log(skaitlis, 10)   # logaritms ar bāzi 10
    print(f"Dabiskais logaritms no {skaitlis}: {round(dabiskais, 4)}")
    print(f"Logaritms ar bāzi 10 no {skaitlis}: {round(desmitais, 4)}")

piemers()
