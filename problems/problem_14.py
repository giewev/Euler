def next_collatz(n):
	'Generates the next number in the collatz sequence after n'
	if n % 2 == 0:
		return n / 2
	else:
		return 3 * n + 1

def collatz_length(n, cache):
	'Calculates the length of the collatz sequence starting from n'
	sequence = [n]
	while sequence[-1] not in cache:
		sequence.append(next_collatz(sequence[-1]))

	end_length = cache[sequence[-1]]
	while len(sequence) > 0:
		next_value = sequence.pop(0)
		cache[next_value] = len(sequence) + end_length
	return cache[n]

collatz_length_cache = { 0 : 0, 1 : 0 }
upper_count = 1000000
lower_bound = int(upper_count / 2) # Any number N less than half the limit would be bested by 2N
path_lengths = [collatz_length(x, collatz_length_cache) for x in range(lower_bound, upper_count)]
print(path_lengths.index(max(path_lengths)) + lower_bound)