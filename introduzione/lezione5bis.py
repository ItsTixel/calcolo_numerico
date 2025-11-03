import numpy as np
from scipy import optimize

# cerchiamo di calcolare f(x) = cos(x) - x
f = lambda x: np.cos(x) - x # lambda function
r = optimize.fsolve(f, -2) # fsolve serve per calcolare gli zeri di una funzione. -2 è il punto di partenza, ovvero dove inizia la ricerca
print(f"zero calcolato: {r}")
print(f"valore funzione in zero calcolato: {f(r)}")

# cerchiamo di calcolare f(x) = x^3 - x - 2
f2 = lambda x: x**3-x-2
r = optimize.fsolve(f2, -2) 
print(f"zero calcolato: {r}")
print(f"valore funzione in zero calcolato: {f2(r)}")




# bisezione con a=2 e b=4 non ha soluzinoe, il while deve essere infinito

