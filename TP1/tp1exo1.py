nom = 'sero'
prenom = 'leonard'
math = 12
anglais = 17
info = 19
promo = 2023
moy = 0

moy = (anglais+math+info)/3

print (type(math), type(anglais), type(info), type(promo), type(moy))
print("L'étudiant {} {} de la promotion {} a une moyenne de {}".format(nom, prenom, promo, moy))
