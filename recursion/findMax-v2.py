def func(arr,n):
    #n si the len of list
    #arr is the list

    #base 
    if n == 1:
        return arr[0]
    
    #instead of slicing, we are reducing the n value
    m = func(arr,n-1)
    
    if arr[n-1] > m:
        return arr[n-1]
    else:
        return m
    
    
nums = [1,90,20,40]
print(func(nums,len(nums)))
