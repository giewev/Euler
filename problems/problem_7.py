import sys
sys.path.insert(0, '../')
from frameworks import primes

prime_maker = primes.prime_generator()
for x in range(10000):
	next(prime_maker)
print(next(prime_maker))