def sliding_window(indexable, window_size):
	'Generates a sliding window of slices from some indexable object'
	while len(indexable) >= window_size:
		yield indexable[:window_size]
		indexable = indexable[1:]

def product(iterable):
	'Generates the product of enumeration provided'
	prod = 1
	for x in iterable:
		prod *= int(x)
	return prod

def factorial(n):
	'Calculates the factorial of a value'
	return product(x for x in range(1, n + 1)) if n > 0 else 1

def digit_sum(n):
	'Calculates the sum of the digits in a number'
	return sum(int(x) for x in str(n))