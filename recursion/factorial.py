def fact(n):

    #base
    if n == 1:
        return 1

    #recursive case
    return n * fact(n-1)


print(fact(5))