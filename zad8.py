tekst_1 = "Lorem ipsum dolor sit amet."
tekst_2 = "Lorem ipsum dolor sit amet, consectetur."
print('{} {}'.format(tekst_1, tekst_2)) # konkatenacja
print('{:>50}'.format(tekst_1)) # wyrównanie do lewej
print('{:50}'.format(tekst_2)) # wyrównanie do prawej
print('{:_<50}'.format(tekst_1)) # dodawanie padding z prawej strony
print('{:^50}'.format(tekst_2)) # centrowanie

