import random
macierz = [[random.random() for j in range(4)] for i in range(4)]
transposed = [[row[i] for row in macierz] for i in range(4)]
przekatna = [i for i in transposed if transposed[i] == i]
print(przekatna)
