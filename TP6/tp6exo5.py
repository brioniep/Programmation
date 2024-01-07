def transfo(Phrase):
    S1 = list(Phrase.lower())
    S2 = []
    for i in range (0, len(Phrase)):
        if S1[i].isalpha():
            S2.append(S1[i])
    return S2

def verification(liste):
    pa = True
    for k in range( len(liste)//2):
        if liste[k] != liste[len(liste)-1-k]:
            pa = False
            break
    return pa
    
Phrase = input("Veuillez entrer un mot ou une phrase : ")
listephrase = transfo(Phrase)

palindrome = verification(listephrase)

if palindrome == False :
    print ("Ce n'est pas un palindrome ...")

else :
    print ("C'est une palindrome ")