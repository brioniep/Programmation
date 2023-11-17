#a
N = int(input("Entrez un nombre entier : "))
somme = 0

for i in range (0,N+1):
    somme +=i

print ("la somme du nombre entier naturel que vous avez entrez jusqu'a 0 est : ", somme)

#b
N = 0
while N != 100 : 
    print("Vous etes coincé dans une boucle infinie, veuillez entrer un nombre entier pour en sortir")
    N = int(input("Entrez une valeur : "))

print("Bravo vous etes sortie de la boucle")

#c
N = 0
inferieur10 = 0
superieur10 = 0
superieur15 = 0

for i in range (10) :
    value = int(input("entrez une valeur entre 0 et 20 : "))

    while value < 0 or value > 20:
        print("La valuer doit etre comprise entre 0 et 20 : ")
        value = int(input("Entrez une valeur réelle entre 0 et 20 : "))

    if value < 10 :
        inferieur10 += 1
    elif value < 15:
        superieur10 += 1
    else:
        superieur15 +=1

print("Nombre de valeurs inférieur strictement à 10 :", inferieur10)
print("Nombre de valeurs supérieur ou égale à 10 et inférieur strictement à 15 :", superieur10)
print("Nombre de valeurs supérieur ou égale à 15 :", superieur15)

#d

X = int(input("Entrez un nombre supérieur à 1 : "))
somme = 0
Compteur = 0

while somme <= X:
    Compteur += 1
    somme += N

print("Le plus grand nombre N tel que la somme des entiers de 0 à N soit inférieure ou égale à {} est : {}".format(X, Compteur-1))