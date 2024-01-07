chaine = input("Veuillez entrer une phrase : ").lower()
taille = 0
voyelle = 0 
count = 0
position = 0

for i in chaine :
    taille += 1
    if i in ["a" ,"e" ,"i" ,"o" ,"u" ,"y"]:
        voyelle += 1

S1 = list(chaine)
for i in range (0, taille):
    if S1[i]== "w" :
        position = i
        if S1[i+1] =="a" and S1[i+2] =="g" and S1[i+3] =="o" and S1[i+4] =="n" :
            count += 1
        else: 
            position = "aucune"
    

print (f"cette chaine de caractère fait {taille} caractères, elle possèdes {round(100*voyelle/taille, 1)} % de voyelles et possèdes {count} fois le mot wagon, à la position {position} pour la première occurence")