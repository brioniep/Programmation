x = 0

x = int(input("Entrez un nombre entier :"))

if x % 2 == 0:
    parité = "paire"
else:
    parité = "impaire"

if x > 0:
    signe = "positif"
elif x < 0:
    signe = "négatif"
else:
    signe = "égal à 0"

print("Le nombre est", signe, "et", parité)



