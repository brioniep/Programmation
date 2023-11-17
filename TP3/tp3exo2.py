#Première version avec la boucle for

import time

N = int(input("Veuillez entrer un nombre entier : "))

for i in range(N, -1, -1):
    print(i)
    time.sleep(1)

# Deuxième version avec la boucle while

import time

N = int(input("Veuillez entrer un nombre entier : "))
retard = N

while retard >= 0:
    print(retard)
    time.sleep(1) 
    retard -= 1
