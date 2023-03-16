import sys

total = [0] * 2
for line in sys.stdin:
	curNumber, curCount = line.strip().split('\t')
	print(curNumber)
	total[int(curNumber) % 2] += int(curCount)
print('Even count:\t', str(total[0]))
print('Odd count:\t', str(total[1]))