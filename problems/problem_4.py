def is_palindrome(num):
	return str(num) == str(num)[::-1]

palindromes = []
for x in range(999, 99, -1):
	for y in range(x, 99, -1):
		if is_palindrome(x * y):
			palindromes.append(x * y)
			break

print(max(palindromes))