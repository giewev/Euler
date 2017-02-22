def proper_divisors(num):
	'Generates all numbers less than the input which divide the input evenly'
	return [x for x in range(1, num) if num % x == 0]

def is_amicable(n, divisor_sums):
	return divisor_sums[n] in divisor_sums and divisor_sums[n] != n and divisor_sums[divisor_sums[n]] == n

divisor_sums = { x : sum(proper_divisors(x)) for x in range(1, 10000) }
print(sum(x for x in divisor_sums if is_amicable(x, divisor_sums)))