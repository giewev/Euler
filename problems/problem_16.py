def digit_sum(n):
	'Calculates the sum of the digits in a number'
	return sum(int(x) for x in str(n))

print(digit_sum(2 ** 1000))