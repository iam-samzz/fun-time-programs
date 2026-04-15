x = "aabbaa"


def func(string,left,right):

    #base case
    if left >= right:
        return True #program can reach base case only if it is palindrome

    if string[left] == string[right]:
        #recursive case
        y = func(string,left+1,right-1)
        
        return y

    return False



print(func(x,0,len(x)-1))
