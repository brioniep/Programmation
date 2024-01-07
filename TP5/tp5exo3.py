Phrase = input("Entrez un mot ou une phrase : ")

S1 = list(Phrase.lower())
S2 = []

for i in range (0, len(Phrase)):
    if S1[i].isalpha():
        S2.append(S1[i])
print (S2)

palindrome = True 
for k in range( len(S2)//2):
    if S2[k] != S2[len(S2)-1-k]:
        palindrome = False
        break
    
if palindrome == False :
    print ("Ce n'est pas un palindrome")

else :
    print ("C'est une palindrome")
