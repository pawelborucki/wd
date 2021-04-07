class ciagi:
    def __init__(self):
        self.elementy = []
        self.pierwszy = 0
        self.krok = 1
        self.ilosc = 0
    def wyswietl_dane(self):
        for elem in self.elementy:
            print(elem, end="\t")

    def pobierz_elementy(self,*element):
        self.ciagi.append(element)

    def pobierz_parametry(self, pierwszy, krok, ilosc):
        # self.a1 = int(input("Podaj a1: "))
        # self.n = int(input("Podaj ilosc elementow: "))
        # self.r = int(input("Podaj r: "))
        self.elementy = [elem for elem in range(pierwszy, krok*ilosc, krok)]
        self.ilosc = ilosc
        self.krok = krok
        self.pierwszy = pierwszy
        
    def policz_sume(self):
        return sum(self.elementy)

    def policz_elementy(self):
        return len(self.elementy)

ciag = ciagi()
ciag.pobierz_elementy()
ciag.pobierz_parametry()
print(ciag.policz_sume())
print(ciag.policz_elementy())
ciag.wyswietl_dane()