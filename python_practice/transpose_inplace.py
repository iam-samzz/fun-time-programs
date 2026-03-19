#transpose_inplace.py


matrix = [

		[1,2,3],
		[4,5,6],
		[7,8,9]

		]

#when doing transpose, no diagonal will change


temp = 0
for column in range(0,len(matrix[0])):
	for row in range(column+1,len(matrix)):

		temp = matrix[row][column]
		matrix[row][column] = matrix[column][row]
		matrix[column][row] = temp


for i in matrix:
	print(i)

