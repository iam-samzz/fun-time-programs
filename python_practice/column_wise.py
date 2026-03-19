#column_wise

matrix =[
		[1,2,3],
		[4,5,6],
		[7,8,9]
		] 


#column wise

no_of_row = len(matrix)

no_of_column = len(matrix[0])

for column in range(0,no_of_column):
	for row in range(0,no_of_row):
		print(f"{matrix[row][column]}",end = " ")
	print()