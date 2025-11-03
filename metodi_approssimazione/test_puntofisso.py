import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("TkAgg")

#Calcoliamo prima la funzione f(x) e poi g(x) ??????????????

# Definiamo le funzioni
f = lambda x: x-np.cos(x) # f (x) = x-cos(x)
g = lambda x: np.cos(x)   # g (x) = cos(x)

# Definiamo i dati:
N = 100
x = np.linspace(-1,1,N)

y_1 = g(x)
y_2 = x

# Aggiungiamo le caratteristiche per il grafico
plt.figure()
plt.plot(x,y_1, label="cos(x)")
plt.plot(x,y_2, label="x")
plt.title("Intersezione tra cos(x) e x")
plt.legend()
plt.grid()

# Mostriamo il grafico
plt.show()

"""
Definiamo:
tol_1 = tolleranza, ovvero quando |x_k-g(x_k)| < tol_1
tol_2 = tolleranza nel caso la condizione converga su x^*
maxit = numero massimo di interazioni
x_new = x_k+1
x_0 = x_k
"""

# Definiamo la funzione del punto fisso
def punto_fisso(g,fun,x_0,tol_1,tol_2, maxit) : 
    
    count=0
    
    # Verifica se abbiamo raggiunto la tolleranza o se abbiamo raggiunto il numero massimo di iterazioni
    while np.abs(fun(x_0))>tol_1 and count<maxit:
        # x_k+1 = g(x_k)
        x_new = g(x_0)

        # print(f"Valore iterazione numero {count}: {x_new}")
        
        # se |x_k-g(x_k+1)| < tol_2
        if (np.abs(x_0-x_new))<tol_2:
            break

        # x_k = x_k+1
        x_0 = x_new
        count=count+1
    return (x_new,count)

# Quindi: 
# g = funzione con cui vogliamo approssimare, f = funzione che dobbiamo approssimare, tol_1 e tol_2 tolleranze, maxit = tempo massimo
sol=punto_fisso(g,f,0,1.e-6,1.e-6,100)
print(f"Soluzione punto fisso: {sol[0]}")
print(f"Numero interazioni: {sol[1]}")

# Quindi...
#   Vede se è minore dalle tolleranze (no)
#   La x equivale a cos(0) = 1
#   La nuova x = 1
# RIPETE IL CICLO
#   Vede se è minore dalle tolleranze (no)
#   La x equivale a cos(1) = 0.5403
#   La nuova x = 0.5403
# RIPETE IL CICLO
#   Vede se è minore dalle tolleranze (no)
#   La x equivale a cos(0.5403) = 0.85755
#   La nuova x = 0.85755
# ...
# ripete finchè maxit o tol.
