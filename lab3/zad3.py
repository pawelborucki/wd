produkty = {"banany": "kg",
            "ananas": "sztuki",
            "baton": "sztuki",
            "gruszki": "kg"}
sztuki = [key for key,value in produkty.items() if value == "sztuki"]
print(produkty)
print(sztuki)

