def maximum_path_sum(triangle):
	'Calculates the maximum path from the top of a triangular array to the bottom'
	while len(triangle) > 1:
		for index, x in enumerate(triangle[-2]):
			triangle[-2][index] += max(triangle[-1][index], triangle[-1][index + 1])
		triangle = triangle[:-1]
	return triangle[0][0]

with open('../data/problem_18_input.txt', 'r') as f:
	triangle = [[int(y) for y in x.rstrip('\n').split(' ')] for x in f]

print(maximum_path_sum(triangle))