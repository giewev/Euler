import math

def is_right_triangle(a, b, c):
	'Determines whether the three side lengths form a right triangle, where C is the hypotenuse'
	return (a ** 2) + (b ** 2) == c ** 2

def pyth_triplets(perimeter):
	'Generates all the pythagorean triplets with the given perimeter'
	for c in range(1, perimeter / 2):
		for b in range(int(math.ceil((perimeter - c) / 2.0)), perimeter - c):
			a = perimeter - c - b
			if is_right_triangle(a, b, c):
				yield (a, b, c)

print([x[0] * x[1] * x[2] for x in pyth_triplets(1000)])