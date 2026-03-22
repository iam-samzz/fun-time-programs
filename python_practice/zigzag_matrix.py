#zigzag_matrix_print

matrix =[
		[1,2,3],
		[4,5,6],
		[7,8,9]]

direction = True #right = True


for row in range(0,len(matrix)):
	if direction == True:

		for column in range(0,len(matrix[0])):
			print(f"{matrix[row][column]}",end = "")

		print()
		direction = not direction

	elif direction == False:
													#when we use 0, it will only go upto 1
			for column in range(len(matrix[0])-1, -1, -1):
				print(f"{matrix[row][column]}",end = "")

			print()
			direction = not direction
