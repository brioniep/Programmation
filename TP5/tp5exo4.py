valeur = input("ENTREZ VOTRE SOMME D'ARGENT : ")

S1 = list(valeur)

a=0
a2 =0
b= 0
c= 0


if len(S1) == 5 :
    i = 0
    a = 1
    a2 = 1
    b = 1 
    c = 1
    
elif len(S1) == 4 :
    i = -1
    a2 =1
    b = 1 
    c = 1

elif len(S1) == 3 :
    i = -2
    b= 1
    c = 1

elif len(S1) == 2 :
    i = -3
    b=1
    c = 1
    
elif len(S1) == 1 :
    i = -4
    c = 1

B100 = int(S1[0 + i])*10000/100 * a + int(S1[1 + i])*1000/100 * a2 +int(S1[2 + i])

B50 = int(S1[3 + i])//5 * b
B10 = (int(S1[3 + i])- B50*5) * b

P2 = int(S1[4 + i])//2 * c
P1 = (int(S1[4 + i])- P2*2) * c

print(f" {valeur} euros, c’est donc {B100} billets de 100, {B50} de 50, {B10} de 10, {P2} pièces de 2 et {P1} pièce 1.")