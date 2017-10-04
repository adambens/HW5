import re
hand = open('DataC.txt')
lines = hand.read()
lis = []
x = re.findall('[0-9]+', lines)
for number in x:
	lis.append(int(number))
print(sum(lis))