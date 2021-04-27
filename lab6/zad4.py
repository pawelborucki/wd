import numpy as np

def generuj(a, b):
    lista = np.logspace(1, b+1, num = b, endpoint=False, base=a)
    return lista
print(generuj(3,5))