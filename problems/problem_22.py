import sys
sys.path.insert(0, '../')
from frameworks.comprehensions import flatten_once

def character_index(character):
	'Calculates the index (based 1) of the given character in the alphabet'
	if not character.isalpha() or len(character) != 1:
		raise ValueError("Character was not a letter: " + character)

	if ord(character) > 96:
		return ord(character) - 96
	else:
		return ord(character) - 64

def name_score(name, index):
	'''Calculates the "Score" of a name
		Which is defined as the sum of the alphabet indices of the letters, 
		multiplied by the index in the list of names'''
	return sum(character_index(c) for c in name) * index

def build_name_list(source_file):
	'Parses a list of names from a file containing a comma delimited list of quoted names'
	lines = [line.replace('\n', '') for line in source_file.readlines()]
	line_names = [line.replace('\"', '').split(",") for line in lines]
	return flatten_once(line_names)

name_file = open("../data/problem_22_input.txt")
name_list = build_name_list(name_file)
name_list = sorted(name_list)
print(sum(name_score(name, index + 1) for index, name in enumerate(name_list)))