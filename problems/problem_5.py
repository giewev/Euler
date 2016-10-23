def gcd(a, b):
	'Finds the greatest common denominator of the two arguments'
	while 0 not in (a, b):
		if a < b:
			b %= a
		else:
			a %= b

	return max(a, b)

def lcm(*args):
	'Finds the least common multiple of all of the inputs'
	divisor_product = 1
	for x in args:
		divisor_product *= x / gcd(divisor_product, x)

	return divisor_product

print(lcm(*range(1, 21)))