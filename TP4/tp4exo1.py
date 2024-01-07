N = float(input("Vous cherchez la table de multiplication de quel nombre : "))
T = [None] * 10


for i in range(10):
    
    T[i] = N * i
    print(N, "*" ,i ,"=" ,round(T[i], 10))