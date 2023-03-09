from __future__ import print_function
import sys

lastWord = None
sum = 0
mostFreq=[]
currentMax=-1

for line in sys.stdin:
    count, word = line.strip().split('\t', 1)
    count = float(count)
    if count>currentMax:
        currentMax=count
        mostFreq=[word]
    elif count==currentMax:
        mostFreq.append(word)
for word in mostFreq:
    print('%s\t%s'%(word,currentMax))