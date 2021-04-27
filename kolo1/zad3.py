#Zadanie 3
#Stwórz generator o nazwie miesiace(), który będzie zwracał kolejne nazwy polskich miesięcy.

def miesiace():
    nazwy = ["Styczeń", "Luty", "Marzec", "Kwiecień", "Maj", "Czerwiec", "Lipiec", "Sierpień", "Wrzesień", "Październik", "Listopad", "Grudzień"]
    for x in range(13):
        yield nazwy[x]
mies = miesiace()
print(next(mies))
print(next(mies))
print(next(mies))
print(next(mies))
print(next(mies))
print(next(mies))
print(next(mies))
print(next(mies))
print(next(mies))
print(next(mies))
print(next(mies))
print(next(mies))
