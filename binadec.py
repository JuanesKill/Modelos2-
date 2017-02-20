def binadec(n):
    if n < 10:
        return n
    else:
        (n%2) + (binadec(n/10)*2)

print binadec(15)
    
