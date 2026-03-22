#count_valid_triplets.py

n = 5
target = int(input("Enter a target(0-12):"))


for i in range(n):
	for j in range(n):
		for k in range(n):
			if i+j+k == target:
				print(f"({i},{j},{k})")
