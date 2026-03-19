#print_border_element


matrix = [
			[1,2,3],
			[4,5,6],
			[7,8,9]
		]



for row in range(0,len(matrix)):
	for column in range(0,len(matrix[0])):
		if (row==0 or row == len(matrix)-1) or (column==0 or column== len(matrix[0])-1):
			print(f"{matrix[row][column]}", end = " ")
		else:
			print("  ",end="")

	print()


#LOGIC:
	#	condition:
		#row should be 1st row 
		# (or) row should be last row

		# (or) column should be 1st column
		# (or) column should last column of the matrix