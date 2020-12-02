# File IO
file1 = open('input.txt', 'r') 
Lines = file1.readlines() 
  
validPasswordCount = 0

# Parse input line by line
for line in Lines:

	#Parse for range
	rangeDividerIndex = line.find('-')
	rangeStart = int(line[0:rangeDividerIndex])
	rangeEnd = int(line[rangeDividerIndex+1:rangeDividerIndex+3].strip())

	passwordRuleIndex = line.find(':')
	passwordRuleLetter = line[passwordRuleIndex-1:passwordRuleIndex]
	
	password = line[passwordRuleIndex+2:len(line)].strip()

	#Part 1

	# if(rangeStart <= password.count(passwordRuleLetter) <= rangeEnd):
	# 	validPasswordCount += 1

	#Part 2

	#exclusive or
	if((password[rangeStart-1] == passwordRuleLetter) ^ (password[rangeEnd-1] == passwordRuleLetter)):
		validPasswordCount += 1

print(validPasswordCount)

