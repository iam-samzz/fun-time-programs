#matrix_multiplication


matrix1 =[
		[1,2,3],
		[4,5,6],
		[7,8,9]]

matrix2 =[
		[1,2,3,6],
		[4,5,6,9],
		[7,8,9,5]
		]


for row in range(0,len(matrix1)):
	for column in range(0,len(matrix2[0])):

		for k in range(0,len(matrix1[0])):
