# File IO
file = open('input.txt', 'r')
Lines = file.readlines()

#Fill the 2D Array

treeMap = []
xLength = len(Lines[0].strip())
yLength = len(Lines)

for line in Lines:
	treeLine = []
	for letter in line.strip():
		treeLine.append(letter)
	treeMap.append(treeLine)

def treesHit(rightCount, downCount):
	xCoord = 0
	yCoord = 0

	hitTrees = 0

	while yCoord < yLength - 1:
		yCoord += downCount
		xCoord += rightCount
		#If you extend beyond the map, move it back one line width
		if(xCoord > xLength - 1):
			xCoord -= xLength

		if(treeMap[yCoord][xCoord] == '#'):
			hitTrees += 1

	return hitTrees

#Part 1

print(treesHit(3, 1))

#Part 2

print(treesHit(1, 1)*treesHit(3, 1)*treesHit(5, 1)*treesHit(7, 1)*treesHit(1, 2))