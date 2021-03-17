# symbol * oznacza dowolną ilość argumentów przechowywanych w krotce
def ciag(* liczby):
    # jeżeli nie ma argumentów to
    if len(liczby) == 0:
        return 0.0
    else:
        iloczyn = 1.0
    # sumujemy elementy ciągu
    for i in liczby:
        iloczyn *= i
    # zwracamy wartość sumy
    return iloczyn
print(ciag(1,2,3,4,5))