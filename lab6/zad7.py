import numpy as np

def przekatne(n):
    lista = [2*x for x in range(1,n*n+1)]
    a = np.array([lista[y * n : y * n + n] for y in range(int(len(lista) / n))])
    
    return a
print(przekatne(3))