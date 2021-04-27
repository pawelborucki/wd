#Zadanie 1
#Wykorzystując python comprehensions (wyrażenie listowe) wygeneruj ciąg 10 elementów 1/n dla n z przedziału <1, 20> z krokiem 2.
def zadanie1():
    ciag = [(1/n) for n in range(1,20,2)]
    print(ciag)
print(zadanie1())