file = open('input.txt', 'r')
Lines = file.readlines()

#Part 1

def binaryConversion(line):
	line = line.replace("F", '0')
	line = line.replace("L", '0')
	line = line.replace("R", '1')
	line = line.replace("B", '1')
	return int(line, 2)

seatIDSet = []

for line in Lines:
	seatIDSet.append(binaryConversion(line.strip()))

seatIDSet.sort()
lastSeatIndex = len(seatIDSet)-1
print(seatIDSet[lastSeatIndex])

#Part 2

remainingSeats = []

for x in range(seatIDSet[0], seatIDSet[lastSeatIndex]):
	remainingSeats.append(x)

print(set(seatIDSet)^set(remainingSeats))
