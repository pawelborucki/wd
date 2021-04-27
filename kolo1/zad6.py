#Zadanie 6
#Napisz funkcję, która odczyta plik z kolejnymi wartościami liczbowymi (przygotuj plik) zapisanymi po jednej w wierszu a następnie do
#tego samego pliku zapisze te wartości posortowane rosnąco (również po jednej w wierszu).

def zadanie6():
    with open("plik1.txt", "r+") as p:
        liczby = [int(x) for x in p.read().split()]
        p.seek(0)
        p.write('\n'.join([str(x) for x in sorted(liczby)]))
zadanie6()


