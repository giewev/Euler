single_digits = { 	'1' : 'one',
					'2' : 'two',
					'3' : 'three',
					'4' : 'four',
					'5' : 'five',
					'6' : 'six',
					'7' : 'seven',
					'8' : 'eight',
					'9' : 'nine'}

ten_digits = 	{	'2' : 'twenty',
					'3' : 'thirty',
					'4' : 'forty',
					'5' : 'fifty',
					'6' : 'sixty',
					'7' : 'seventy',
					'8' : 'eighty',
					'9' : 'ninety'}

teens = 		{ 	'10' : 'ten',
					'11' : 'eleven',
					'12' : 'twelve',
					'13' : 'thirteen',
					'14' : 'fourteen',
					'15' : 'fifteen',
					'16' : 'sixteen',
					'17' : 'seventeen',
					'18' : 'eighteen',
					'19' : 'nineteen'}

def english_word(num):
	'Expresses an integer from 1-1000 in english'
	if num == 1000:
		return 'one thousand'

	word = ''
	if num >= 100:
		word += single_digits[str(num)[0]] + ' hundred'
		num %= 100
		if num > 0:
			word += ' and '

	if num >= 20:
		word += ten_digits[str(num)[-2]] + ' '
		if num % 10 > 0:
			word += single_digits[str(num)[-1]]
	elif num >= 10:
		word += teens[str(num)[-2:]]

	if 0 < num < 10:
		word += single_digits[str(num)[-1]]

	return word

print(sum(len(english_word(x).replace(' ', '')) for x in range(1, 1001)))