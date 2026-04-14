def oneToN(n):
    n1 = n
    #base case
    if n == 0:
        return
    
    #prints last only...in stack
    oneToN(n-1)
    print(n)

oneToN(10)