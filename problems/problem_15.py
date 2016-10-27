import sys
sys.path.insert(0, '../')
from frameworks.comprehensions import factorial

def grid_solve(m, n):
	'Solves the problem by calculating the number of paths to each node'
	grid = [[0] * (n + 1) for x in range(m + 1)]
	for x in range(m + 1):
		grid[x][0] = 1
	for y in range(n + 1):
		grid[0][y] = 1

	for x in range(1, m + 1):
		for y in range(1, n + 1):
			grid[x][y] = grid[x - 1][y] + grid[x][y - 1]

	return grid[-1][-1]

def quick_solve(m, n):
	'Find the number of paths through a grid by modeling it as a combinatorics problem'
	return factorial(m + n) / (factorial(m) * factorial(n))

print(grid_solve(20, 20))
print(quick_solve(20, 20))