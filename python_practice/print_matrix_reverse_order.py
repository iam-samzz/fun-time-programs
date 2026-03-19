#print_matrix_reverse_order


matrix =[
		[1,2,3],
		[4,5,6],
		[7,8,9]]



for row in range(len(matrix)-1, -1, -1):
	for column in range(0,len(matrix[0])):
		print(f"{matrix[row][column]} ",end="")

	print()
