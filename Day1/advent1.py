from itertools import combinations

# Using readLines
file = open('input.txt', 'r')
Lines = file.readlines()

numbers = []
for line in Lines:
	numbers.append(int(line.strip()))

# Part 1

for x, y in combinations(numbers, 2):
	if(x + y == 2020):
		print(x*y)

# Part 2

for x, y, z in combinations(numbers, 3):
	if(x + y + z == 2020):
		print(x*y*z)