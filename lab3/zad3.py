produkty = {"banany": "kg",
            "ananas": "sztuki",
            "baton": "sztuki",
            "gruszki": "kg"}
odwrocony = {value: key for key, value in produkty.items()}
#sztuki = [odwrocony["sztuki"] for odwrocony["sztuki"] in odwrocony]
print(produkty)
print(odwrocony)
#print(sztuki)