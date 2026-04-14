def multip(a,b):
    if b == 0 or a == 0:
        return 0
    elif b == 1:
        return a
    return (a + multip(a,b-1))

print(multip(10,20))