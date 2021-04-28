import numpy as np
import math as m
mat = np.arange(6).reshape(2,3)
for x in mat.flat:
    a = m.sin(mat[x])
print(a)

