N = int(input("Veuillez entrer un nombre entier : "))

Boucle = int(input("Veuillez choisir une boucle a utilisé (1 = for / 2 = while) : "))

while Boucle != 1 and Boucle !=2 :
    print("ERREUR, VOUS DEVEZ ENTRER 1 OU 2")
    Boucle = int(input("Veuillez choisir une boucle a utilisé (1 = for / 2 = while) : "))

if Boucle == 1 :
    print("Vous avez choisi la boucle for")
else :
    print("Vous avez choisi la boucle while")

Factoriel = 1

if Boucle == 1 :
    for i in range (0,N+1) :
        Factoriel = Factoriel * i
        print(i, " X " ,Factoriel/i, "=", Factoriel)
    print(Factoriel)

else:
    while N > 1 : 
        N= N - 1
        Factoriel = N * (N - 1)

print(Factoriel)