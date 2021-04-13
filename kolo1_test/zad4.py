def najwieksze(lista):
    lista = sorted(lista)
    print(lista)
    return lista[:3]
test = [1,3,2,8,10,12]
print(najwieksze(test))
