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
kwadrat = Kwadrat(5)  
kw2 = Kwadrat(6)
duzy_kwadrat = kwadrat.__add__(kw2)
print(duzy_kwadrat)
