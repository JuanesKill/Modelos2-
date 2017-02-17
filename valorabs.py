def valorabsoluto(n):
    if n > 0:
        return n;
    else:
        if n < 0:      
            return valorabsoluto(n*-1)
        
print valorabsoluto(-5)

        
