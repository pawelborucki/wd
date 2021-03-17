def mono(a):
    if a > 0:
        return 1
    elif a < 0:
        return 2
    else: 
        return 3
x = int(input("Podaj współczynnik funkcji \n"))
if mono(x) == 1:
    print("Funkcja rosnąca")
elif mono(x) == 2:
    print("Funkcja malejąca")
else:
    print("Funkcja stała")
    