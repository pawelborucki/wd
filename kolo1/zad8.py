#Zadanie 8
#Zadeklaruj klasę Student, która posiada atrybuty: imie, nazwisko, kierunek_studiow, rok_studiow, indeks. Klasa powinna posiadać
#konstruktor i metodę wypisz_mnie() która będzie wyświetlała informacje w postaci:
#Student <imie> <nazwisko>: <rok_studiow> roku na kierunku <kierunek_studiow>. Indeks: <indeks>. Stwórz 4 instancje klasy
#Student i zapisz wynik metody wypisz_mnie() do pliku, każdy student w oddzielnej linii.
class Student:
    def __init__(self, imie, nazwisko, kierunek_studiow, rok_studiow, indeks):
        self.imie = imie
        self.nazwisko = nazwisko
        self.kierunek_studiow = kierunek_studiow
        self.rok_studiow = rok_studiow
        self.indeks = indeks
    def wypisz_mnie(self):
        print(f'Student {self.imie} {self.nazwisko}: {self.rok_studiow} roku na kierunku {self.kierunek_studiow}. Indeks: {self.indeks}')
s1 = Student("Jan", "Nowak", "Informatyka", 2, 32131)
s2 = Student("Ewa", "Kowalska", "Ekonomia", 1, 54432)
s3 = Student("Kamil", "Wiśniewski", "Medycyna", 3, 44343)
s4 = Student("Paulina", "Kwaśniewska", "Weterynaria", 1, 43322)
print(s1.wypisz_mnie())
print(s2.wypisz_mnie())
print(s3.wypisz_mnie())
print(s4.wypisz_mnie())