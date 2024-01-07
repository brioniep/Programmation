L1 = [0] * 3
print(L1, id(L1))

for i in L1 :
    print( type(i), id(i))

L1[1]+= 1
print("---------------------------------------------------------")
for i in L1 :
    print( type(i), id(i))

a = "machaine"

print("---------------------------------------------------------")
for k in a :
    print( type(k), id(k))