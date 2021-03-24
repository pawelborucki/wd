class NaZakupy:
    nazwa_produktu = ""
    ilosc = 0
    jednostka_miary = ""
    cena_jed = 0
    def konstruktor(self, nazwa, ilosc, jednostka, cena):
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
        print(self.ilosc, " ")
        print(self.jednostka_miary)
    def ile_kosztuje(self, x):
        print(self.cena_jed * x)

obiekt = NaZakupy.konstruktor(x,"s",2,"szt",2)
print(obiekt)

