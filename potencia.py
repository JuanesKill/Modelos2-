def potencia(n,m):
    if m < 1:
        return 1
    return n* potencia(n,m-1)

print potencia(3,3)
