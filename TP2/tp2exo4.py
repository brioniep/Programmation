BASE = 4
fromage = 800.0
eau = 2
ail = 2
pain = 400

nbConvives = int(input("Entrez le nombre de personne (s) conviées à la fondue : "))

fromage = fromage * nbConvives / BASE
eau = eau * nbConvives / BASE
pain = pain * nbConvives / BASE
ail = ail * nbConvives / BASE

print ("Pour faire une fondue fribourgeoise pour ",nbConvives , ",il vous faut :")
print(fromage, " gr de fromage")
print(eau, " dl d'eau")
print(ail, " gousse(s) d'ail")
print(pain, " gr de pain")
