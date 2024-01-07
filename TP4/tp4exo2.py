nombreEtudiants = int(input("Donnez le nombre d'étudiants : "))
moyenne = 0.0
S = 0
T = []

for i in range (nombreEtudiants) :
    
    note = float(input("Entrez la note d'un étudiant "))
    
    while note > 20 or note < 0:
        note = float(input("La valuer est incorect, entrez une valeur entre 0 et 20 : "))
    T.append(note)
    
moyenne = sum(T) / nombreEtudiants
print("Moyenne de la classe : ",moyenne)


for i in range (nombreEtudiants) : 
    print("Numéro de l'Etudiant | note | ecart a la moyenne")
    print(i + 1 , " | " ,T[i], " | " ,T[i] - moyenne)
