#Zadanie 4
#Napisz funkcję, która oblicza pole, obwód oraz długość przekątnej kwadratu dla podanej długości boku x. Wyświetlaj wyniki na ekran
import math as m
def kwadrat(x):
    pole = x ** 2
    obwod = x * 4
    przekatna = x * m.sqrt(2)
    return "Pole:{} Obwód: {} Przekątna: {}".format(pole, obwod, przekatna)
print(kwadrat(5))