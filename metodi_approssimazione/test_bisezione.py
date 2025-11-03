import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("TkAgg")

# Definiamo i dati
a = -2
b = 2
N = 100

x = np.linspace(a,b,N) # Se omettiamo N, il valore è di 50
y = np.log(x+1)-x # y= ln(x+1)-x

plt.figure() # Qual è la dimensione migliore?
plt.plot(x,y)

# Definiamo una funzione con y=0 \forall x
y_0=np.zeros(len(x))
plt.plot(x,y_0,'r')

plt.show()

# Definiamo la funzione lambda(x) = ln(x+1)-x
f=lambda x: np.log(x+1)-x

# Definiamo la funzione per la bisezione, con intervallo [a,b]
def bisezione (fun,a,b,tol,maxit):
    # Controlliamo se l'intervallo sia corretto (teorema degli zeri)
    if fun(a) * fun(b) >= 0:
        print("Errore: la funzione non ha segni opposti agli estremi dell'intervallo.")
        return (None, 0)

    count = 0

    # Verifichiamo se siamo dentro la tolleranza o se abbiamo superato le iterazioni massime
    while (b-a) / 2 > tol and count < maxit:
        c=(a+b)/2

        # print(f"Valore iterazione numero {count}: {c}")
        
        if (fun(a)*fun(c))>0:
            a=c # la radice è nella metà a destra
        else:
            b=c # la radice è nella metà a sinistra
        count = count + 1
    # Punto medio finale
    c=(a+b)/2
    return (c,count)

sol=bisezione(f,a,b,1.e-6,100)
print (f"Soluzione: {sol[0]}")
print (f"Iterazioni: {sol[1]}")

