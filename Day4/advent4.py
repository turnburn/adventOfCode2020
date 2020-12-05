file = open('input.txt', 'r')
Lines = file.readlines()
Lines.append("")

#Part 1

fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
fieldIsPresent = [False, False, False, False, False, False, False]

# def isFound(fieldString, flag, line):
# 	if(flag == True):
# 		return True
# 	else:
# 		if(fieldString in line):
# 			return True
# 		else:
# 			return False


def resetFields():
	for x in range(0, len(fieldIsPresent)):
		fieldIsPresent[x] = False

def isValid():
	for field in fieldIsPresent:
		if(field == False):
			return False
	return True

validPassports = 0

#Part 2

eyeColours = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

def parseEntry(entry):
	valueStart = entry.find(':')
	value = entry[valueStart+1:len(entry)]

	if "byr" in entry:
		if(1920 <= int(value) <= 2002):
			fieldIsPresent[0] = True

	if "iyr" in entry:
		if(2010 <= int(value) <= 2020):
			fieldIsPresent[1] = True

	if "eyr" in entry:
		if(2010 <= int(value) <= 2030):
			fieldIsPresent[2] = True

	if "hgt" in entry:
		if("cm" == value[len(value)-2:len(value)]):
			cmValue = value[0:len(value)-2]
			if(150 <= int(cmValue) <= 193):
				fieldIsPresent[3] = True

		if("in" == value[len(value)-2:len(value)]):
			inValue = value[0:len(value)-2]
			if(59 <= int(inValue) <= 76):
				fieldIsPresent[3] = True

	if "hcl" in entry:
		if(value.find("#") == 0 and len(value) == 7):
			for x in range(1, 7):
				if(48 <= ord(value[x]) <= 57 or 97 <= ord(value[x]) <= 102):
					fieldIsPresent[4] = True

	if "ecl" in entry:
		if value in eyeColours:
			fieldIsPresent[5] = True

	if "pid" in entry:
		if unicode(value, 'utf-8').isnumeric() and len(value) == 9:
			fieldIsPresent[6] = True


for line in Lines:
	if not line.strip():
		if(isValid()):
			validPassports += 1
		resetFields()

	#for x in range(0, len(fields)):
		#fieldIsPresent[x] = isFound(fields[x], fieldIsPresent[x], line.strip())

	entries = line.strip().split()
	for entry in entries:
		parseEntry(entry)

print(validPassports)
