a = int(input("podaj a\n"))
b = int(input("podaj b\n"))
c = int(input("podaj c\n"))
if (a > 0 and a <= 10) and (a > b or b > c):
    print("warunki spelnione\n")
else:
    print("warunki nie spelnione")