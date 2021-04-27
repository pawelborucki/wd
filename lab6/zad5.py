import numpy as np

def w_diag(n):
    wektor = [x for x in range(1, n+1)]
    wektor = wektor[::-1]
    mac_diag = np.diag([a for a in wektor])
    return mac_diag
print(w_diag(5))