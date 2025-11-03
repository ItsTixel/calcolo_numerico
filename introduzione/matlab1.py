import matplotlib.pyplot as plt
import numpy as np
import matplotlib
matplotlib.use("TkAgg") # per evitare il warning
# serve per specificare quale backend di matplotlib utilizzare

#creiamo due VETTORI
a = 0
b = 2 * np.pi
N = 50

# x = [0,2*\pi,4*\pi...]
x= np.linspace(a,b,N)

# y1 = sin(x) , y2 = cos(x)
y1 = np.sin(x)
y2 = np.cos(x)

# Dimensione della finestra (x, y)
plt.figure(figsize=(10,6))

# visualizzazione:
plt.title("Un grafico di funzioni trigonometriche")
plt.plot(x, y1, label="seno") # Per default plt.plot(x,y,"linea",color="b")
plt.plot(x,y2, label="coseno")

# Descrizione delle assi
plt.xlabel("Angolo in rad: ", fontsize=12)
plt.ylabel("Risultato: ", fontsize=12)

# Utilizza label definito nel comando plt.plot
plt.legend()

# plt.xticks() mostra il valore dell'asse orizontale. Nei casi del seno e coseno può essere intuitivo
plt.xticks(
    ticks=[0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi],
    labels=[r'0', r'$\frac{\pi}{2}$', r'$\pi$', r'$\frac{3\pi}{2}$', r'$2\pi$']
)

# Aggiungiamo una griglia, con lo stile dei puntini
plt.grid(linestyle=":")

# Rendiamo più moderno
# ax = plt.gca()  # gca = "Get Current Axes"
# ax.spines['top'].set_visible(False)
# ax.spines['right'].set_visible(False)

# Serve a far vedere il grafico
plt.show()






