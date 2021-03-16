import sys 
wys = int(sys.stdin.readline())
if wys < 3 or wys > 9:
    print("Wysokosc musi byc >3 i <9")
for x in range(1, (wys + 1) // 2 + 1): 
    for y in range((wys + 1) // 2 - x):
        print(" ", end = "")
    for z in range((x*2)-1):
        print("o", end = "")
    print()

for x in range((wys + 1) // 2 + 1, wys + 1): 
    for y in range(x - (wys + 1) // 2):
        print(" ", end = "")
    for z in range((wys + 1 - x)*2 - 1):
        print("o", end = "")
    print()
''' 
wys = int(sys.stdin.readline())

for x in list(range(wys)) + list(reversed(range(wys-1))):
  print('{: <{w1}}{:*<{w2}}'.format('', '', w1=wys-x-1, w2=x*2+1)) '''