def ajouter_elt(lst=[0,1,2], elt=3):
    lst.append(elt)
    print (id(lst))
    return lst


def ajouter_carac(ch="abc", elt="d"):
    print (id(ch))
    return ch + elt
    

print (ajouter_elt())
print (ajouter_carac())