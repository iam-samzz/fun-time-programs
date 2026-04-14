arr = [2,3,4]

def func(arr):
    
    #base case
    if len(arr) == 0:
        return 0


    #recursive
    s = arr[-1] + func(arr[0:-1])

    return s

print(func(arr))