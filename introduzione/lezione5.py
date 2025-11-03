import numpy as np
import sys

print(sys.float_info)
# print(np.finfo(np.float32))
# print(np.finfo(np.float64))

# print(4.9-4.845)
# in fl MAI utilizzare a==b, al massimo puoi utilizzare |a-b|<epsilon
#epsilon = 1e-1
#a = 4.9
#b = 4.845
#print(abs(a-b)<epsilon)

# CALCOLIAMO E
# distanza tra e e la sua approssimazione
# logspace è 
esp = np.logspace(0, 16, 17)
print(esp)

for i in range(0,17):
    s=(1+1/esp[i])**esp[i]
    print(f"i={i} e approssimato={s} distanza={np.e-s}")

print(s)


def calcola_precisione_macchina():
    epsilon = 1.0
    while (1.0 + epsilon) != 1.0:
        epsilon /= 2.0
    return epsilon

precisione = calcola_precisione_macchina()
print(f"Precisione macchina calcolata: {precisione}")