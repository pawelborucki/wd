class Kwadrat: 
    def __init__(self, x):
        self.x = x
    def __radd__(self, other):
        if other == 0:
            return self
        else:
            return self.__add__(other)
    def __add__(self, other):
        return self.x + other
    def __ge__(self, other):
        return self.x >= other
    def __gt__(self, other):
        return self.x > other
    def __le__(self, other):
        return self.x <= other
    def __lt__(self, other):
        return self.x < other
kw1 = Kwadrat(5)  
kw2 = Kwadrat(6)
duzy_kwadrat = kw1.__add__(kw2)
if kw1.__ge__(kw2):
    print("kw1 wiekszy albo taki sam ")
if kw1.__gt__(kw2):
    print("kw1 wiekszy")
if kw1.__le__(kw2):
    print("kw2 wiekszy albo taki sam ")
if kw1.__lt__(kw2):
    print("kw2 wiekszy")
