def multiplicar(n,m):
    if m < 1:
        return 0
    return n+ multiplicar(n,m-1)

print multiplicar(6,6)
