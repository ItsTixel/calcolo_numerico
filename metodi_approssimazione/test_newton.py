import numpy as np
import matplotlib.pyplot as plt

f = lambda x: x-np.cos(x)
df = lambda x: 1+np.sin(x)

def newton(f,df,x_0,tol_1,tol_2,maxit):
    count= 0
    while(np.abs(f(x_0)) > tol_1 and (count < maxit)):
        x_new=x_0-f(x_0)/df(x_0)

        print(f"Valore iterazione numero {count}: {x_new}")
        
        if np.abs(x_0-x_new) < tol_2:
            break
        x_0=x_new
        count=count+1
    return (x_0,count)

x_0 = 0
sol = newton(f,df,x_0,1.e-6,1.e-6,100)
print(f"Soluzione metodo newton: {sol[0]}")
print(f"Iterazione: {sol[1]}")

