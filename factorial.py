def factorial(n):
    if n < 0:
        return 0
    else:
        if n > 1:
            return n* factorial(n-1)
        return 1
    
print factorial(3)
        
