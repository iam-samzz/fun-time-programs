#print_even_coordinates.py


matrix =[
		[1,2,3],
		[4,5,6],
		[7,8,9]]



for row in range(0,len(matrix)):
	for column in range(0,len(matrix[0])):
		if (row+column)%2 == 0:
			print(f"({row},{column})")
			