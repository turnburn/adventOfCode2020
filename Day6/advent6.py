#Python3 only

file = open('input.txt', 'r')
Lines = file.readlines()
Lines.append("")

groupAnswers = []

def resetGroup():
	groupAnswers.clear()

#Part 1
def getCountUnion():
	#Rolling Union to get unique items in the 2D Group Array
	noRepeatList = []
	for x in range(0, len(groupAnswers)):
		noRepeatList = list(set(noRepeatList) | set(groupAnswers[x]))
	return len(noRepeatList)

#Part 2
def getCountIntersection():
	noRepeatList = set.intersection(*map(set,groupAnswers))
	return len(noRepeatList)

fullCount = 0

for line in Lines:
	#New Person
	if not line.strip():
		fullCount += getCountIntersection()
		resetGroup()
	else:
		#Log answers
		personAnswer = line.strip()
		groupAnswers.append(list(personAnswer))

print(fullCount)