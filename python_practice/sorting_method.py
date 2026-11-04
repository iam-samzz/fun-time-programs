l = [[99,50],[40,60],[70,60]]

sort_func = lambda y : y[0]
l.sort(key = sort_func)

# or

l.sort(key = lambda inner_list: inner_list[0])

print(l)
