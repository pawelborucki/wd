class Slowa:
    def __init__(self, slowo1, slowo2):
        self.slowo1 = slowo1
        self.slowo2 = slowo2
    def sprawdz_czy_palindrom(self):
        if self.slowo1 == self.slowo1[::-1]:
            print(f'{self.slowo1} jest palindromem')
        if self.slowo2 == self.slowo2[::-1]: 
            print(f'{self.slowo2} jest palindromem')
    def sprawdz_czy_metagramy(self):
        roznica = 0
        if len(self.slowo1) == len(self.slowo2):
            for x in range(len(self.slowo1)):
                if self.slowo1[x] != self.slowo2[x]:
                        roznica += 1
        if roznica == 1:
            print("wyrazy są metagramami")
        else: 
            print("To nie sa metagramy")
    def sprawdz_czy_anagramy(self):
        if sorted(self.slowo1) == sorted(self.slowo2):
            print(f'{self.slowo1} i {self.slowo2} to anagramy')
        else:
            print(f'{self.slowo1} i {self.slowo2} to nie są anagramy')
    def wyswietl_wyrazy(self):
        print(f'{self.slowo1} , {self.slowo2}')
obiekt = Slowa("tama", "mata")
print(obiekt.sprawdz_czy_anagramy())
print(obiekt.wyswietl_wyrazy())
