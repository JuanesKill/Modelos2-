def binadec(n):
    if n < 10:
        return n
    else:
        return (n%2) + (binadec(n/10)*2)

print binadec(111)

def decabin(n):
    if n < 1:
        return '0'
    else:
        return (decabin(n//2)) + str(n%2)  

print decabin(7)
    
