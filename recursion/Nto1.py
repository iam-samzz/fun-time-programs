def Nto1(n):

    if n == 1:
        print(1)
        return
    print(n)
    Nto1(n-1)


Nto1(10)