def proste(a1, a2):
    if a1 == a2:
        return 1
    elif a1 * a2 == -1:
        return 2
    else:
        return 3
a1 = int(input("Podaj współczynnik pierwszej prostej \n"))
a2 = int(input("Podaj współczynnik drugiej prostej \n"))

if proste(a1,a2) == 1:
    print("Proste są równoległe")
elif proste(a1,a2) == 2:
    print("Proste są prostopadłe")
else: 
    print("Nie są prostopadłe ani równoległe")