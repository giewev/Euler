def multiple_sum(multiple_cap, *args):
	'''	Calculates the sum of the multiples of the provided arguments
		All multiples in [1, multiple_cap) will be considered'''
	return sum(x for x in range(1, multiple_cap) if any(x % y == 0 for y in args))

print(multiple_sum(1000, 3, 5))