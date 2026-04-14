x = "samaran"

def func(str):

    #bsae case.
    if len(str) == 1:
        return str

    #recursive case..
    reverse = str[-1] + func(str[0:-1])
    return reverse

print(x)
print(func(x))