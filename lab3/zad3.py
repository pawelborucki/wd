produkty = {"banany": "kg",
            "ananas": "sztuki",
            "baton": "sztuki",
            "gruszki": "kg"}
sztuki = [x for x in produkty if produkty.values() == "sztuki"]
print(sztuki)