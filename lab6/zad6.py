import numpy as np
import random
import string
w1 = "szum"
w2 = "mata"
w3 = "mózg"
w4 = list(w1)[::-1]
mat1 = np.diag(list(w1)[::-1])
mat1[0:4,0] = list(w3)
mat1[0,0:4] = list(w2)
print(mat1)