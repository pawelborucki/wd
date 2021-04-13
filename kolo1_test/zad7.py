import random
def suma_srednia(ile, przedzial):
    random.seed()
    liczby = [random.randint(*przedzial) for i in range(ile)]
    suma = 0
    for x in range(len(liczby)):
        suma += liczby[x]
    srednia = suma / len(liczby)
    return liczby, suma, srednia
print(suma_srednia(5, (1, 10)))