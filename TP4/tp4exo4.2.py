L1 = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7, 6]

occurence = [0] * len(L1)
print (occurence)
for i in  L1:
    occurence[i] = L1.count(i)
print(occurence)

maxi = max(occurence)

nombre = occurence.index(maxi)

print(f"Le nombre le plus frequent dans la liste est le : ",nombre, ", qui apparait",maxi, "fois")


""" ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
* Ne rien modifier apres cette ligne.
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** * /
"""