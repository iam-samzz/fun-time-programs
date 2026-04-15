l = [10,10,10,20,20,9,9]
target = 10
i = 0

def func(arr,target,i):
    
    #base case
    if i == len(arr):
        return 0

    if arr[i] == target:
        count = 1 + func(arr,target,i+1)

        return count
    else:
        count = 0 + func(arr,target,i+1)
        return count


print(func(l,target,i))