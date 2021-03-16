import random
macierz = [[random.random() for j in range(4)] for i in range(4)]
przekatna = [[x for x in macierz] for i in macierz]
print(przekatna)
