def Encuentra(lista,elemento):
    if lista == []:
        return False
    elif lista[-1]==elemento:
        return True
    else:
        return Encuentra(lista[1:],elemento)  