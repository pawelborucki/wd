tekst = input("Podaj napis \n")
wielkie = 0
male = 0
for x in range(len(tekst)):
    if tekst[x].isupper():
        wielkie += 1
    elif tekst[x].islower():
        male += 1
print(f'Malych liter jest {male}, a wielkich jest {wielkie}')
