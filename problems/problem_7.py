def is_prime(num, primes_so_far):
	'''Tests whether a number is prime.
	Using the primes up to at least the square root of the input allows much faster checking'''
	root = num ** 0.5
	for x in primes_so_far: 
		if x > root:
			return True
		if num % x == 0:
			return False
	return True

def prime_generator():
	'''Generates primes, keeping a reference to the primes generated so far
	This means that this generator will use more memory as primes are generated'''
	primes_so_far = [2, 3]
	yield 2
	yield 3

	six_index = 6
	while True:
		if is_prime(six_index - 1, primes_so_far):
			primes_so_far.append(six_index - 1)
			yield six_index - 1
		if is_prime(six_index + 1, primes_so_far):
			primes_so_far.append(six_index + 1)
			yield six_index + 1

		six_index += 6

prime_maker = prime_generator()
for x in range(10000):
	next(prime_maker)
print(next(prime_maker))