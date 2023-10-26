y = int(input("Entrez un nombre :"))

if y >= 2:
    if y < 3:
        print(y,"appartient à I")
elif y > 0:
    if y <= 1:
        print(y,"appartient à I")
elif y >= -10:
    if y <= -2:
        print(y,"appartient à I")
else:
    print(y,"n'appartient pas à I")
