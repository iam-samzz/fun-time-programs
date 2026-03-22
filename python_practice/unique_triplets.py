#unique_triplets
#Print all triplets (i, j, k) such that:
		# condition: 0 ≤ i < j < k < n

iterations = 4

for i in range(iterations):  # n+1 times
	#anything inside a for loop run n times
	for j in range(iterations): # (n * n+1)
		#inside: n * n
		for k in range(iterations): # (n^2 * n+1)
			# inside: n*n*n
			if i!=j and i!=k and j!=k:
				print(f"({i},{j},{k})")



