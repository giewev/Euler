with open('../data/problem_13_input.txt', 'r') as f:
	print(str(sum(int(x) for x in f))[:10])