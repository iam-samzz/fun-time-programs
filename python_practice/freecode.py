def bucket_fill(grid,pos,new_value):

	#basically..we need to check all 8 boxes around the single element in a matrix
	x = grid[pos[0]][pos[1]]
	grid[pos[0]][pos[1]] = new_value

	if pos[0] != len(grid)-1:
		if grid[pos[0]+1][pos[1]] == x:
			grid[pos[0]+1][pos[1]] = new_value

	if pos[0] != 0:
		if grid[pos[0]-1][pos[1]] == x:
			grid[pos[0]-1][pos[1]] = new_value

	if pos[1] != len(grid[0])-1
		if grid[pos[0]][pos[1]+1] == x:
			grid[pos[0]][pos[1]+1] = new_value

	if pos[1] != 0:
		if grid[pos[0]][pos[1]-1] == x:
			grid[pos[0]][pos[1]-1] = new_value

	if pos[0]!= 0 and pos[1]!=0:
		if grid[pos[0]-1][pos[1]-1] == x:
			grid[pos[0]-1][pos[1]-1] = new_value

	if pos[0] != len(grid)-1 and pos[1] != 0:
		if grid[pos[0]+1][pos[1]-1] == x:
			grid[pos[0]+1][pos[1]-1] = new_value

	if pos[0] != 0 and pos[1] != len(grid[0])-1:
		if grid[pos[0]-1][pos[1]+1] == x:
			grid[pos[0]-1][pos[1]+1] = new_value

	if pos[0] != len[grid]-1 and pos[1] != len(grid[0])-1:
		if grid[pos[0]+1][pos[1]+1] == x:
			grid[pos[0]+1][pos[1]+1 = new_value
	return grid




