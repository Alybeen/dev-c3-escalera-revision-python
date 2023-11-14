listing = [7, 9, 11, 7, 4, 0, 9, 5, 3, 8]
if len(listing) > 0:
    listing.sort()
    print("le chiffre minimum est : ", listing[0])
    print("le chiffre maximum est :", listing[len(listing) - 1])
    res = 0
    for i in listing:
        res += i
    print("la moyenne est : ", res / len(listing))
else:
    print("pas de nombres")
