#3D_pattern_condition


for i in range(5):
	for j in range(5):
		for k in range(5):
			if i==j or j==k or k==i:
				print(f"({i},{j},{k})")