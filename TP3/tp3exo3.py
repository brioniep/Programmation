import random

N = random.randint(0, 100)

T = 0


while True:
    
    a = int(input("Essayez de deviner le nombre entre 0 et 100 : "))
    
    T += 1

    if a < N:
        print("Le nombre auquel je pense est plus grand")
    elif a > N:
        print("Le nombre auquel je pense est plus petit")
    else:
        print("Vous avez trouver le nombre en ", T ," tours")
        break
