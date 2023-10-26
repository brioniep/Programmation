x = int(input("Entrez x : "))
y = int(input("Entrez y : "))
o = y # variable temporel

y = x
x = o

print("Avant permutation : ")
print("x : " , y)
print("y : " , x)

print("Après permutation : ")
print("x : " , x)
print("y : " , y)

