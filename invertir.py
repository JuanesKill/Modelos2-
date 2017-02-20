def invertir(lista):
    if lista == [1]:
        return str(lista[0])
    else:
        return str(lista[len(lista)-1]) + str(invertir(lista[:len(lista)-1]))

print invertir([1,2,3])
