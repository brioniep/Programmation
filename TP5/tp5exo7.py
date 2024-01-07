nombre = float(input("Vous cherchez la table de multiplication pour le nombre ? "))
L = []
for i in range(10):
    L.append(nombre*float(i))
    print(f"{nombre} * {i} = {L[i]}")