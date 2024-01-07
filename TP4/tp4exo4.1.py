L1 = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7, 6]

occurence = {}
print (occurence)
for i in  L1:
    print (i)
    if i in occurence:
        occurence[i] += 1
    else :
        occurence[i] = 1
print(occurence)
maxi = max(occurence.values())

nombre = [k for k, values in occurence.items() if values == maxi ]

print(f"Le nombre le plus frequent dans la liste est le : ",nombre, ", qui apparait",maxi, "fois")

""" ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
* Ne rien modifier apres cette ligne.
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** * /
"""
