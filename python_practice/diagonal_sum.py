#diagonal_sum

matrix = [
			[1,2,3,6],
			[4,5,6,8],
			[7,8,9,0],
			[4,6,9,20]
		]

c = len(matrix[0])
r = len(matrix)

x = 0
for column in range(0,c):
	print(matrix[x][column])
	x += 1
	

