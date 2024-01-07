import random

def generer(nbr, vmin, vmax):
    Tbl = []
    for i in range(nbr):
        Tbl.append(random.randint(vmin, vmax))
    return Tbl

def combienInferieur(table, seuil):
    count =0
    for k in table:
        if k < seuil :
            count += 1
    return count

nb = int(input("Veuillez choisir le nombre de valeurs a généré : "))
vmin = int(input("Veuillez choisir la valeur minimum : "))
vmax = int(input("Veuillez choisir la valeur maximum : "))

question = input("Souhaitez vous choisir un seuil (30 par défaut) OUI(O) ou NON(N) : 10")
if question == "O":
    seuil = int(input("Veuillez choisir le seuil : "))
else: 
    seuil = 30
        
print(f"Générer ",nb, "nombres entiers entre ",vmin," et ",vmax,)
tab = generer(nb, vmin, vmax)
tab.sort()
print(tab)
total = combienInferieur(tab, seuil)
print(f"Il y en a",total," inférieurs à ",seuil,)