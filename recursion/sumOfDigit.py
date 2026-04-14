def func(integer):

    #base case
    if integer == 0:
        return 0
    
    #recursive case
    s = (integer%10) + func(integer//10)
    return s

print(func(125))