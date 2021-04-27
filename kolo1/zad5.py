#Zadanie 5
#Napisz funkcję, która generuje 10 list 10 elementowych wartości losowych z przedziału <1,100>. Następnie wyświetl te listy w
#kolejności rosnącej, porównując sumę wartości wszystkich elementów listy.
import random as r
def zadanie5():
    lista = [[r.randrange(1,100,1) for x in range(10)]]*10
    print(lista)
    suma = []
    for x in range(10):
        print(sum(lista[x]))
    
    print(suma)
print(zadanie5())