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