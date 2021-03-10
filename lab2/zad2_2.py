import sys
print("Podaj pierwsza liczbe\n")
liczba_1 = int(sys.stdin.readline())
print("Podaj druga liczbe")
liczba_2 = int(sys.stdin.readline())
wynik = liczba_1*liczba_2
sys.stdout.write(str(wynik))
