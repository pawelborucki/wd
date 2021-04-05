class NaZakupy:
    def __init__(self, nazwa, ilosc, jednostka, cena):
        self.nazwa_produktu = nazwa 
        self.ilosc = ilosc
        self.jednostka_miary = jednostka 
        self.cena_jed = cena
    def wyswietl_produkt(self):
        print(self.nazwa_produktu, "\n")
        print(self.ilosc, "\n")
        print(self.jednostka_miary, "\n")
        print(self.cena_jed, "\n")
    def ile_produktu(self):
        print(self.ilosc, " ", self.jednostka_miary)
    def ile_kosztuje(self):
        print(int(self.cena_jed) * self.ilosc)

obiekt1 = NaZakupy("ananas", 5, "szt", "6")
print(obiekt1.wyswietl_produkt())
print(obiekt1.ile_produktu())
print(obiekt1.ile_kosztuje())

