import numpy as np

a = np.arange(81).reshape(9,9)
b = a.reshape(3,27)
c = a.reshape(1,81)
#Można stworzyc macierze o ilosci kolumn lub wierszy rownych dzielnikom 81(9x9) np 3,27 oraz transponować każdą z nich