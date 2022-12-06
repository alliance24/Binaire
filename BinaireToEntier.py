# Convertit un binaire en entier

def entier(b):
    n=0
    for i in range(len(b)):
        n+=b[i]*2**i
    return(n)

print(entier([1, 1, 1, 1, 1, 1, 1, 1]))
