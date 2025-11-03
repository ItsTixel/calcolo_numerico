import matplotlib.pyplot as plt
import numpy as np
import matplotlib
matplotlib.use("TkAgg")

f = lambda x: (x-1)**2 + np.exp(x)
df = lambda x: 2*(x-1) + np.exp(x)

x1 = np.linspace(-4, 4, 400)
y1 = f(x1)

# definiamo la funzione per il backtracking di alpha
def backtracking(f, df, x_k):
    alpha = 1
    rho = 1/2 # tolleranza
    c = 0.25

    # Cond. Armijo: f(x_k + alpha*p_k) <= f(x_k) + c*alpha*(grad.f(x_k)**T * p_k)
    # Nel nostro caso: p_k = -df(x) (direzione di discesa, antigradiente)
    #
    # Il loop "while" continua FINCHÉ la condizione è VIOLATA (segno >)

    grad_norm = df(x_k) # Per ora siamo in R1, ||df(x)||^2 è semplicemente df(x)**2
    p_k=-df(x_k)

    while f(x_k + alpha * p_k) > f(x_k) + c * alpha * grad_norm * p_k:
        alpha = rho * alpha

    return alpha


# metodo del gradiente ---------------------------

def GD(f, df, x_old, maxit, x_true, tol_f, tol_x): 
    # Creiamo gli array di dimensione maxit+1 per includere il passo iniziale (k=0)
    errore = np.zeros((maxit + 1,))
    fun = np.zeros((maxit + 1,))
    
    k = 0

    # x_new --> x_k+1, mentre x_old --> x_k
    x_new = 0   
    
    # Salviamo i valori iniziali (passo k=0)
    # Usiamo la norma (abs) per l'errore, coerente con il problema
    errore[k] = np.abs(x_true - x_old) 
    fun[k] = f(x_old)

    # np.linalg.norm(df(x)) = norma della derivata di f(x)
    # np.linalg.norm(x_new-x_0)>tol_x condizione di arresto.

    # np.linalg.norm(df(x_old)**2 > tol_f) and (np.linalg.norm(x_new-x_old)>tol_x)

    current_grad_norm = np.linalg.norm(df(x_old))

    while k < maxit and current_grad_norm > tol_f: # Lo deve fare almeno una volta?

        # Calcoliamo alpha con il backtracking
        alpha = backtracking(f, df, x_old)
        x_new = x_old - alpha * df(x_old)
        # print(f"Valore: {x_new}")

        if np.abs(x_new - x_old) < tol_x:
            print("Metodo interrotto dalla tolleranza x: il passo è troppo piccolo per fare progressi")
            break
        
        # Aggiorno per l'iterazione
        k += 1
        x_old = x_new
        
        current_grad_norm = np.linalg.norm(df(x_old)) # Ricalcola la norma del gradiente

        # Inserisco i valori per gli errori e la funzione
        errore[k] = np.abs(x_true - x_new)
        fun[k] = f(x_new)

    
    # Se usciamo prima di maxit, tronchiamo gli array
    if k < maxit:
        errore = errore[:k+1]
        fun = fun[:k+1]

    if k == maxit:
        print("Metodo interrotto dal numero di iterazione massime")
    elif current_grad_norm > tol_f:
        print("Metodo interrotto dalla tolleranza f:")

    return x_new, k, errore, fun


x_true = 0.31492 
maxit = 300 # Max 300 iterazioni
tolleranza_f = 1.e-6 # Tolleranza ...
tolleranza_x = 1.e-5 # Tolleranza ...

# ignora: 
# PER HOMEWORK: questo è un metodo molto lento, ha un esponente p = 1
# LE ULTIME DUE SONO UTILIZZATE PER IL MACHINE LEARNING

sol = GD(f, df, 0, maxit, x_true, tolleranza_f, tolleranza_x)

n_iterazioni = sol[1] # Numero di iterazioni fatte
soluzione = sol[0]
errore_finale=sol[2][n_iterazioni]
print(f"Soluzione: {soluzione}")
print(f"Iterazioni: {n_iterazioni}")
print(f"Errore finale (restituito dalla funzione): {errore_finale}")
print(f"Errore assoluto (calcolato manualmente): {np.abs(soluzione-x_true)}")



# <------ CREAZIONE GRAFICO ------>

valore_funzione=sol[3]
errori_assoluti=sol[2]

# np.arange = crea intervalli basati al numero di iterazioni
# potremmo anche aver utilizzato np.linspace()
iterations = np.arange(n_iterazioni + 1) # +1 perché includiamo lo step 0

# Al posto di utilizzare subplots(2,1,1)... come l'ultimo homework, decido di farlo in questo modo che è più comodo
fig, axs = plt.subplots(2, 1, figsize=(10, 8))

# --- Plot 1: Errore Assoluto ---
# Usiamo semilogy per vedere meglio la discesa (scala logaritmica su Y)
axs[0].semilogy(iterations, errori_assoluti, 'b-o', label='Errore assoluto')
axs[0].set_title('Andamento della Convergenza (Errore)')
axs[0].set_ylabel(r'$|x_{true} - x_k|$')
axs[0].grid(which='both', linestyle='--', alpha=0.6)
axs[0].legend()

# --- Plot 2: Valore della Funzione ---
axs[1].plot(iterations, valore_funzione, 'r-o', label='Valore funzione')
axs[1].set_title('Andamento della Funzione Obiettivo')
axs[1].set_xlabel('Iterazione (k)')
axs[1].set_ylabel(r'$f(x_k)$')
axs[1].grid(linestyle='--', alpha=0.6)
axs[1].legend()

# Mostra i grafici
plt.tight_layout() # Aggiusta la spaziatura
plt.show()