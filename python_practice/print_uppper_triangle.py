#print_uppper_triangle

matrix =[
		[1,2,3],
		[4,5,6],
		[7,8,9]
		]


for row in range(0,len(matrix)):
	for column in range(row+1, len(matrix[0])):

		#from (row+1) after crossing the element in diagonal.
		#to end of the row

		print(f"{matrix[row][column]}",end ="")

	print()



#or 

for row in range(0,len(matrix)):
	for column in range(0,len(matrix[0])):
		if column>row:
			print(f"{matrix[row][column]}", end ="")

	print()