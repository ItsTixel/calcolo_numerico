import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("TkAgg")

# precisione
N = 200

# Creiamo i dati della prima tabella
x_1 = np.random.normal(0, 1, N)
y_1 = np.random.normal(0, 1, N)
# Attenzione! con random.normal(0,1), non stiamo generando valori casuali da 0 a 1, ma da 0 a infinito!
# con (0,1) stiamo semplicemente dicendo che la maggior parte dei numeri sarà tra 0 a +-1.
# La probabilità che troviamo un numero al di fuori di x=3, è sotto l'1%.

# Creiamo i dati della seconda tabella
x_2 = np.random.normal(0, 0.5, (N, )) # numeri molto più vicini al centro orizontale del grafico
y_2 = np.random.normal(0, 2, (N, )) # numeri più sparsi nell'asse verticale, ovvero del "risultato"

# La finestra è rettangolare, 10 di lunghezza e 4 di altezza
plt.figure(figsize=(12, 5)) 

# <-- VISUALIZZIAMO LA PRIMA TABELLA -->
plt.subplot(1, 2, 1) # 1,2 vuol dire quante sottofigure mettere, una matrice con una riga e due colonne. 1 = quale grafico
plt.plot(x_1, y_1, 'o', color='red') # Froma e colore dei pallini del primo grafico 
plt.title('Distribuzione normale') 
plt.xlim([-3, 3])
plt.ylim([-4, 4])
plt.grid()

# <-- VISUALIZZIAMO LA SECONDA TABELLA -->
plt.subplot(1, 2, 2) # Secondo grafico
plt.plot(x_2, y_2, 'o', color='green')
plt.title('Distribuzione normale di dati verticali')
plt.xlim([-3, 3])
plt.ylim([-4, 4])
plt.grid()

# Facciamo vedere il risultato
plt.show()