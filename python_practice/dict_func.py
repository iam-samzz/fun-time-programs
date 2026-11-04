h = {
    "a" : 10,
    "b" : 99,
    "c" : 2903
}

x = h.items()

x = sorted(x , key = lambda inner_tuple : inner_tuple[1], reverse= True)
print(x)

#note: sort is method for list objects,  and sorted is a build in function
