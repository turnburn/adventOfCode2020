file = open('input.txt', 'r')
Lines = file.readlines()

# Part 1

seenLines = []
loopFound = False
accumulator = 0

def executeNext(index):
	global accumulator
	global loopFound
	global seenLines


	if index in seenLines:
		loopFound = True
		return
	else:
		seenLines.append(index)

	if index == len(Lines):
		return

	string = Lines[index].strip()
	stringLength = len(string)
	if 'nop' in Lines[index]:
		executeNext(index+1)
	elif 'acc' in Lines[index]:
		accumulator += int(string[string.find(" "):stringLength])
		executeNext(index+1)
	else:
		executeNext(index+int(string[string.find(" "):stringLength]))

#executeNext(0)

# Part 2

for x in range(0, len(Lines)):
	if 'jmp' in Lines[x]:
		Lines[x] = Lines[x].replace('jmp', 'nop')
		executeNext(0)
		if loopFound == False:
			print(accumulator)
			exit()
		else:
			Lines[x] = Lines[x].replace('nop', 'jmp')
	elif 'nop' in Lines[x]:
		Lines[x] = Lines[x].replace('nop', 'jmp')
		executeNext(0)
		if loopFound == False:
			print(accumulator)
			exit()
		else:
			Lines[x] = Lines[x].replace('jmp', 'nop')

	seenLines = []
	accumulator = 0
	loopFound = False