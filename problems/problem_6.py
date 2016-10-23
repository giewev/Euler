def square_of_sum(*args):
	return sum(args) ** 2

def sum_of_squares(*args):
	return sum(x ** 2 for x in args)

print(square_of_sum(*range(1, 101)) - sum_of_squares(*range(1, 101)))