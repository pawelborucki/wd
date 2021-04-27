#Zadanie 7
#Napisz funkcję, która:
#- „rozdaje” karty z talii 52 kart (np. As pik, Dama karo, itd.) dla 4 graczy
#- karty rozdawane są bez powtórzeń po 5 dla każdego gracza (sprawdź random.sample())
#- wyświetlana jest informacja jak wygląda „ręka” każdego z graczy, np. Alan [As pik, 9 karo, itd.]
import random as r
def zadanie7():
    class karta:
        def __init__(self, kolor, wartosc):
            self.kolor = kolor
            self.wartosc = wartosc
        def wypisz(self):
            print(f'{self.wartosc} {self.kolor}')
    class talia:
        def __init__(self):
            self.karty = []
            self.uloz()
        
        def uloz(self):
            for x in ["Karo", "Pik", "Kier", "Trefl"]:
                for y in range(1,14):
                    self.karty.append(karta(x,y))
        def wypisz(self):
            print(self.karty)
    class gracze(talia):
        def __init__(self, imie):
            self.imie = imie
            self.reka()
        def reka():
            r = r.sample(talia.karty, 5)
            print(r)
        def pokaz_reke(self):
            print(self.reka())
    g1 = gracze("adam");
    print(g1.pokaz_reke())
print(zadanie7())