#rotate_matrix_90deg 



matrix =[
		[1,2,3],
		[4,5,6],
		[7,8,9]]

matrix2=[[1,1,1],[1,1,1],[1,1,1]]

for row in range(len(matrix)-1, -1 ,-1):
	for column in range(0, len(matrix[0])):
		for row2 in range(0,len(matrix)):

			#current-coordinates(rowc,columnc)

			matrix2[column][row2] = matrix[row][column]


for i in matrix2:
	print(i)


