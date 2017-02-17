def mcd(n,m):
    if m==0:
        return n
    return mcd(m,n % m)

print mcd(10,4)
