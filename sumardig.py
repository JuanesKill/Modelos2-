def sumardigitos(n):
    if n==0:
        return n
    else:
        return (n%10)+sumardigitos(n/10)

print sumardigitos(25)
