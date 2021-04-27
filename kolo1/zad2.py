#Napisz funkcję, która posiada listę 10 elementową z dowolnymi imionami. Funkcja generuje 2 listy 5 elementowe, które posiadają
#wylosowane imiona z listy wejściowej. Wypisz listy na ekran.
import random
def zadanie2():
    lista = ["Anna", "Adam", "Adrian", "Bartosz", "Piotr", "Jan", "Janusz", "Agnieszka", "Eryk", "Ewelina"]
    lista2 = [random.choice(lista) for x in range(5)]
    lista3 = [random.choice(lista) for x in range(5)] 
    print(lista2)
    print(lista3)
print(zadanie2())