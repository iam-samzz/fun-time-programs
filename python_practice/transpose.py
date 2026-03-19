#transpose.py


matrix = [
			[1,2,3],
			[4,5,6],
			[7,8,9]
		]

matrix2 = []

x = []
current_value = 0


for column in range(0, len(matrix[0])):
	for row in range(0,len(matrix)):

		current_value = matrix[row][column]
		x.append(current_value)



	matrix2.append(x)
	x=[]




print("Transpose Matrix:")
for i in matrix2: 
	print(i)


