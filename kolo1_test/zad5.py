def ilosc_znakow(tekst):
    znaki = {i:tekst.count(i) for i in tekst}
    return znaki
print(ilosc_znakow("testowy tekst"))
