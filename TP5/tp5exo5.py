salaireHeure = int(input("Veuillez entrer le salaire horaire : "))
Heure = int(input("Veuillez entrer le nombres d'heures travaillers : "))

if Heure > 200 :
    a = 160
    b = Heure - 200
    c = Heure - a -b

elif Heure > 0 and Heure < 161 :
    a = Heure
    b = 0
    c = 0

else :
    a = 160
    b = 0
    c = Heure - 160


SalaireTOTAL = a * salaireHeure + c * salaireHeure * 1.25 + b *salaireHeure * 1.5

print (f"Le salaire pour {Heure} Heures est de {SalaireTOTAL} Euros")
   