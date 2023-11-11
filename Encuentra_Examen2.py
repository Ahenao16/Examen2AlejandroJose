def Encuentra(lista,elemento):
    if isinstance(lista,list) and isinstance(elemento,int):
        if lista == []:
            return False
        elif lista[0]==elemento:
            return True
        else:
            return Encuentra(lista[1:],elemento)  
    else:
        return "Error"