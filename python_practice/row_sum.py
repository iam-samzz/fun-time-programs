#row_sum

matrix =[
		[1,2,3],
		[4,5,6],
		[7,8,9]]

current_sum = 0
for row in range(0,len(matrix)):
	for column in range(0,len(matrix[0])):
			current_sum = current_sum + matrix[row][column]
	print(current_sum)
	current_sum = 0

