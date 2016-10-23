def prime_factors(num):
	'Produces all of the prime factors of the input'
	while num % 2 == 0:
		num /= 2
		yield 2

	possible_divisor = 3
	while possible_divisor <= num ** 0.5:
		while num % possible_divisor == 0:
			yield possible_divisor
			num /= possible_divisor

		possible_divisor += 2

	if num != 1:
		yield int(num)

print(max(prime_factors(600851475143)))