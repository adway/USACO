"""
ID: adway1
LANG: PYTHON3
TASK: milk2
"""

f = open('milk2.in', 'r')
w = open('milk2.out', 'w')

fileAsArray = (f.read()).split()

del fileAsArray[0]

startTimes = list(map(int, fileAsArray[::2]))
endTimes = list(map(int, fileAsArray[1::2]))
common = startTimes[0]
startTimes[:] = [number - common for number in startTimes]
endTimes[:] = [number - common for number in endTimes]

i = 1
a = 0
minStart = 0
maxEnd = endTimes[0]
timeMilkingArray = []

while i < len(startTimes):
    if startTimes[i] <= maxEnd:
        # Replace end time
        if endTimes[i] >= maxEnd:
            maxEnd = endTimes[i]
    else:
        b = maxEnd-minStart
        minStart = startTimes[i]
        maxEnd = endTimes[i]
    i += 1

print(b)
