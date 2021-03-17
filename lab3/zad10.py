def lista_zakupow(** zakupy):
    suma = 0.0
    for i in zakupy:
        suma += zakupy[i]
    return suma
print(lista_zakupow(jeden=10, dwa=20))
