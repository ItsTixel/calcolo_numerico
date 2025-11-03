import matplotlib.pyplot as plt
import numpy as np
import matplotlib
matplotlib.use("TkAgg")

def f(X):
    x = X[0]
    y = X[1]

    return (x-5)**2+(y-2)**2

def df(X):
    x = X[0]
    y = X[1]

    df_dx = 2*(x-5) 
    df_dy = 2*(y-2)
    
    return np.array([df_dx, df_dy])

x0=np.linspace(-6,8,200)
y0=np.linspace(-4,10,200)

# Backtracking per alpha
def backtracking(f, df, X_k):
    alpha = 1
    rho = 1/2
    c= 0.25

    # Calcola la norma del gradiente
    grad_k = df(X_k)

    # Direzione di discesa
    p_k=-df(X_k)

    # Calcola lo SCALARE del prodotto scalare (grad_k^T * p_k)
    # np.dot fa il prodotto scalare tra due vettori
    grad_dot_p = np.dot(grad_k, p_k)
    
    # Nota: grad_dot_p è un numero negativo, è l'elemento che rende vero la prima condizione di wolfe

    # Condizione Di Armijo
    while f(X_k + alpha * p_k) > f(X_k) + c * alpha * grad_dot_p:
        alpha = rho * alpha

    return alpha

# Metodo del gradiente stocastico
def SGD (f, df, X_old, max_steps, tol_f, tol_x):
    
    # Dimensione del mini-batch
    k = 3

    # Inizializziamo il dataset
    S_k = np.arange(0,20,1)

    # Per la condizione di uscita
    step_count=0

    # Dichiare un array di 0 di dimensione maxit + 1
    fun_history = np.zeros((max_steps + 1,2))
    fun_history[0,]=X_old

    # Caso che tutto va bene, esce per maxit
    exit_flag = 'maxit'

    current_grad_norm=np.linalg.norm(df(X_old))
    print(f"Norma gradiente corrente: {current_grad_norm}")

    # Controllo se ho superato le iterazioni o se ho raggiunto la tolleranza desiderata
    while step_count < max_steps and current_grad_norm > tol_f :

        # Randomizziamo gli indici del mini-batch
        np.random.shuffle(S_k)

        for i in range (0,len(S_k),k):
            # (Nota: qui useremmo S_k[i:i+k] se df dipendesse dai dati)
            
            # Calcola la direzione (gradiente stocastico)
            grad_stoc = df(X_old)
            p_k = -grad_stoc

            # Backtracking per alpha
            alpha = backtracking(f, df, X_old) # Dobbiamo utilizzarlo? È molto lento

            # Calcolo di X_k+1
            X_new = X_old + alpha * p_k

            # Controllo se sto facendo progressi (tolleranza x)
            if np.linalg.norm(X_new - X_old) < tol_x:
                exit_flag = 'tol_x'
                break

            # Aggiorno per l'iterazione successiva
            X_old = X_new
            step_count += 1
            
            # Aggiungo il valore della funzione in x_k nell'array dei risultati
            fun_history[step_count] = X_new

            # Controllo se ho superato il numero di passi
            if step_count >= max_steps:
                break # Interrompe il 'for' loop

        # Ricalcolo la norma del gradiente
        current_grad_norm=np.linalg.norm(df(X_new))

        if exit_flag == 'tol_x':
            break

    # In caso siamo usciti per tolleranza
    if exit_flag == 'maxit' and current_grad_norm <= tol_f:
        exit_flag = 'tol_f'

    # Tronciamo l'array inizializzato all'inizio
    if step_count<max_steps: 
        fun_history = fun_history[:step_count+1]

    return X_old, step_count, fun_history, exit_flag

maxit = 300
tolleranza_f = 1.e-6
tolleranza_x = 1.e-6
punto=np.array([0.0,0.0])

ris = SGD(f, df, punto, maxit, tolleranza_f, tolleranza_x)
soluzione = ris[0]
n_iterazione = ris[1]
path_history = ris[2]
exit_condition = ris[3]
print(f"Soluzione: {soluzione}")
print(f"Numero iterazioni: {n_iterazione}")
print(f"Uscita per: {exit_condition}")




# <--- GENERAZIONE GRAFICO --->

X_mesh, Y_mesh = np.meshgrid(x0, y0)
Z = f([X_mesh, Y_mesh])

plt.figure(figsize=(10, 8))

# Disegna le curve di livello
plt.contour(X_mesh, Y_mesh, Z, levels=50, cmap='viridis', alpha=0.7)
plt.colorbar(label='Valore di $f(x,y)$')

# Disegno il percorso fatto dall'algoritmo
path_x = path_history[:, 0] # [:,0 ] selezione tutto della prima colonna, ovvero il percorso delle x
path_y = path_history[:, 1]
plt.plot(path_x, path_y, 'r-o', label='Percorso del Gradiente')

# Evidenzia il punto iniziale e finale
plt.plot(path_x[0], path_y[0], 'go', label=f'Start: ({path_x[0]}, {path_y[0]})') # punto iniziale
plt.plot(path_x[-1], path_y[-1], 'rx', label=f'End: ({soluzione[0]:.2f}, {soluzione[1]:.2f})', markersize=16) # punto finale

# Disegno il minimo teorico
plt.plot(5, 2, 'b*', markersize=15, label='Minimo Teorico (5, 2)')

# Etichette e titoli
plt.title('Metodo del Gradiente con Backtracking')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend()
plt.grid(linestyle='--', alpha=0.5)
plt.gca().set_aspect('equal', adjustable='box') # "Grafo è quadrato"
plt.show()

