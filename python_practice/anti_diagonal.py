#anti_diagonal

matrix = [
			[1,2,3,6],
			[4,5,6,8],
			[7,8,9,0],
			[4,6,9,20]
		]

#for each row:
	#the anti diagonal element will be: => (len(matrix)-1 - i)

print("Diagonal of the Matrix: ")
for row in range(0,len(matrix)):
	print(matrix[row][row])

print("Anti Diagonal Of the Matrix: ")



for row in range(0,len(matrix)):
	print(matrix[row][len(matrix[0])-1 - row])


	