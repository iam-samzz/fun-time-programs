#multipication


X = [[1,2,3],
     [4,5,6],
     [7,8,9]]

Y = [[1,1,1],
     [1,1,1],
     [1,1,1]]


#X(column) == Y(rows)

def mul(X,Y):
    xc = len(X[0])
    yr = len(Y)
 
    c = [[0,0,0],[0,0,0],[0,0,0]]

    if xc != yr:
        print("Cannot Multiply")
        return -1
    
    for i in range(0,len(X)):
        for j in range(0,len(Y[i])):
            for k in range(0,len(Y)):
                c[i][j] = c[i][j] + X[i][k]* Y[k][i]

    return c 

print(mul(X,Y))
