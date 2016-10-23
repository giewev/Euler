from itertools import takewhile

def fibonacci():
	'A generator of the fibonacci sequence: 1, 2, 3, 5...'
	yield 1
	yield 2

	a = 1
	b = 2

	while True:
		c = a + b
		yield c
		a = b
		b = c

print(sum(y for y in takewhile(lambda x: x <= 4e6, fibonacci()) if y % 2 == 0))