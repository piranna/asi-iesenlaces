def menor(a,b):
    if a < b:
        return a
    else:
        return b
    
def mayor(a,b):
    if a > b:
        return a
    else:
        return b
    
def mcd(m,n):
    elmenor = menor(m,n)
    elmayor = mayor(m,n)
    resto = elmayor % elmenor
    if resto == 0:
        return elmenor
    else:
        return mcd(elmenor, resto)

print mcd(120,15)



