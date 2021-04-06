class Material:
    def __init__(self, rodzaj, dlugosc, szerokosc):
        self.rodzaj = rodzaj
        self.dlugosc = dlugosc
        self.szerokosc = szerokosc
    def wyswietl_nazwe(self):
        return "Nazwa: {}".format(self.rodzaj)
class Ubrania(Material):
    def __init__(self, rozmiar, kolor, dla_kogo):
        self.rozmiar = rozmiar
        self.kolor = kolor
        self.dla_kogo = dla_kogo
    def wyswietl_dane(self):
        return "Rozmiar: {} Kolor: {} Dla kogo: {}".format(self.rozmiar, self.kolor, self.dla_kogo)
class Sweter(Ubrania):
    def __init__(self, rodzaj_swetra):
        self.rodzaj_swetra = rodzaj_swetra
    def wyswietl_dane(self):
        return "Rodzaj swetra: {}".format(self.rodzaj_swetra)
material1 = Material("jedwab", 60, 50)

print(material1.wyswietl_nazwe())

ubrania1 = Ubrania("L", "czarny", "M")

print(ubrania1.wyswietl_dane())

sweter1 = Sweter("Rozpinany")

print(sweter1.wyswietl_dane())