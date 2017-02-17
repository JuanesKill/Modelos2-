def palindromo(s):
    if (len(s) < 2):
        return "palindromo"
    else:        
        if (s[-len(s)]) == (s[len(s)-1]):
            return palindromo(s[1: len(s)-1])
        else:        
            return "no palindromo"

print palindromo("rotor")
