saisie = input("Veuillez saisir la date sous la forme jjmmaaaa : ")
D = [int(chiffre) for chiffre in saisie]
print(D)

Jour = D[0] * 10 + D[1]
Mois = D[2] *10 + D[3]
année = D[4] * 1000 + D[5] *100 + D[6] * 10 + D[7]

if année > 9999 or année < 0000 :
    print ("incorrect")

elif année % 4 == 0 and année % 100 != 0 or année % 400 == 0  :
    if  Mois == 2 and Jour > 29 or Jour < 1:
        print("incorrect")  
    if Mois > 12 or Mois < 1 :
        print ("incorrect")

    elif Mois in [1, 3 ,5 , 7, 8, 10, 12] and Jour > 31 or Jour < 1:
            print("incorrect")

    elif Mois == 2 and Jour > 28 or Jour < 1:
         print ("incorrect")

    elif Mois in [4, 6, 9, 11] and  Jour > 30 or Jour < 1:
        print ("incorrect")

    else:
        print ("correct")
 

else : 
    if Mois > 12 or Mois < 1 :
        print ("incorrect")

    elif Mois in [1, 3 ,5 , 7, 8, 10, 12] and Jour > 31 or Jour < 1:
            print("incorrect")

    elif Mois == 2 and Jour > 28 or Jour < 1:
         print ("incorrect")

    elif Mois in [4, 6, 9, 11] and  Jour > 30 or Jour < 1:
        print ("incorrect")

    else:
        print ("correct")