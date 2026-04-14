#Find the Maximum Element: 
# Recursively traverse an array to find the largest number.

arr = [9,4,22,6,2]

def func(arr):
    
    #base case
    if len(arr) == 1:
        return arr[0]

    m = func(arr[0:-1])
    
    if arr[-1] > m:
        return arr[-1]
    else:
        return m
    
print(func(arr))