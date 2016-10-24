import sys
sys.path.insert(0, '../')
from frameworks import primes
from collections import Counter
from itertools import combinations

def triangle_numbers():
	'Generator of the triangle numbers: 1, 3, 6, 10...'
	so_far = 0
	index = 1
	while True:
		so_far += index
		index += 1
		yield so_far

def divisor_count(prime_divisors):
	'Counts the divisors of a number given the prime divisors'
	return sum(len(set(combinations(prime_divisors, x))) for x in range(len(prime_divisors) + 1))

prime_generator = primes.prime_generator()
prime_source = [next(prime_generator)]
triangle_generator = triangle_numbers()
current_triangle = next(triangle_generator)

while divisor_count(primes.prime_divisors(current_triangle, prime_source)) < 500:
	current_triangle = next(triangle_generator)
	while prime_source[-1] < current_triangle ** 0.5:
		prime_source.append(next(prime_generator))

print(current_triangle)