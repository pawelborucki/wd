class Robot:
    def __init__(self, x, y, krok):
        self.x = x
        self.y = y
        self.krok = krok
    def idz_w_gore(self, ile_krokow):
        self.x += ile_krokow * self.krok
    def idz_w_dol(self, ile_krokow):
        self.x -= ile_krokow * self.krok
    def idz_w_lewo(self, ile_krokow):
        self.y = self.y * -1 * ile_krokow * self.krok
    def idz_w_prawo(self, ile_krokow):
        self.y *= ile_krokow * self.krok
    def pokaz_gdzies_jestes(self):
        print(f'Współrzędne: {self.x}, {self.y}')

obiekt = Robot(0,0,1)
obiekt.idz_w_gore(10)
obiekt.idz_w_lewo(6)