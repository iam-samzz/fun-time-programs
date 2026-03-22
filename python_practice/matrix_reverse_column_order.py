#matrix_reverse_column_order


matrix =[
		[1,2,3],
		[4,5,6],
		[7,8,9]
		]


for row in range(0,len(matrix)):
	for column in range(len(matrix[0])-1, -1, -1):
		print(f"{matrix[row][column]} ", end = "")
	print()