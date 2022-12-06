# Convertit un entier en binaire base 2

def binaire(n):
    assert n>=0 and n<=255
    b=[0]*8
    i=0
    while n>0:
        b[i]=n%2
        n=n//2
        i+=1
    return b

print(binaire(255))