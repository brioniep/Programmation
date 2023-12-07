nMAX = 3
Scalaire = 0
v = 0
V1 = []
V2 = []

nEFF = int(input("Quelle est la taille de vos vecteurs [entre 1 et 3] ?"))

while nEFF > 3 or nEFF < 0:
    nEFF = int(input("VALEUR INCORECT. Quelle est la taille de vos vecteurs [entre 1 et 3] ?"))



print ("Saisie du premier vecteur : ")
for i in range (nEFF):
    v = int(input(f"V1[{i}] = "))
    V1.append(v)
print ("Saisie du deuxième vecteur : ")
for i in range (nEFF):
    v = int(input(f"V2[{i}] = "))
    V2.append(v)

for i in range (nEFF):
    Scalaire += V1[i] * V2[i]

print("Le produit scalaire de v1 par v2 vaut", Scalaire)
