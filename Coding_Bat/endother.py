def end_other(a,b):
    listeda = list(a.lower())
    listedb = list(b.lower())
    for i in range(len(a)-1):
        if (listeda[len(a)-len(b):len(a)] == listedb):
            return True
    for s in range(len(b)-1):
        if (listedb[len(b)-len(a):len(b)] == listeda):
            return True
    return False
