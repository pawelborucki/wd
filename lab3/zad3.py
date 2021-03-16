produkty = {"banany": "kg",
            "ananas": "sztuki",
            "baton": "sztuki",
            "gruszki": "kg"}
sztuki = [x for x, value in produkty.items() if produkty.values() == "sztuki"]
print(sztuki)