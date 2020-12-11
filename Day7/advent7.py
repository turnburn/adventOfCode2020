file = open('input.txt', 'r')
Lines = file.readlines()

bagDictionary = {}

for line in Lines:
	bagName = line[0:line.strip().find(" contain")-1]
	contentsString = line[line.strip().find("contain ")+8:len(line)-2]

	bagContains = {}

	for bagString in contentsString.split(", "):

		if(bagString[len(bagString)-1:len(bagString)] == "s"):
			formattedBagString = bagString[2:len(bagString)-1]
		else:
			formattedBagString = bagString[2:len(bagString)]

		if 'no other bag' not in bagString:
			bagContains[formattedBagString] = int(bagString[0:1])
		

	bagDictionary[bagName] = bagContains

#Part 1

seenBags = set()

def checkBags(originalBag, bagList, keyword):
	for bag in bagDictionary[bagList].keys():
		if keyword == bag:
			seenBags.add(originalBag)
			break
		checkBags(originalBag, bag, keyword)

def findBag(keyword):
	for bag in bagDictionary.keys():
		checkBags(bag, bag, keyword)

findBag("shiny gold bag")
print(len(seenBags))

#Part 2


count = 0
# Part Two
def countTotalBags(keyword):
    global count
    count += sum(bagDictionary[keyword].values())
    for bag, numBags in bagDictionary[keyword].items():
        for x in range(numBags):
            countTotalBags(bag)

countTotalBags("shiny gold bag")
print(count)
