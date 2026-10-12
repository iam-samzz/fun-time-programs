#column_sum

matrix = [
			[1,2,3],
			[4,5,6],
			[7,8,9]]


r = len(matrix)
c = len(matrix[0])


for column in range(0,c):
    s = 0
    for row in range(0,r):
        s += matrix[row][column]
    print(s)