#eg : 0,1,1,2,3,5,8,..

def func(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    fib = func(n-1) + func(n-2)
    return fib


print(func(10))