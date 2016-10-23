import sys
sys.path.insert(0, '../')
from frameworks import primes
from itertools import takewhile

print(sum(takewhile(lambda x: x < 2e6, primes.prime_generator())))