#replace_element_with_i+j


matrix = [
			[1,2,3],
			[4,5,6],
			[7,8,9]]



for row in range(0,len(matrix)):
	for column in range(0,len(matrix[0])):

		matrix[row][column] = row+column


	print(matrix[row])

