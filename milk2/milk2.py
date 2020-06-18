"""
ID: adway1
LANG: PYTHON3
TASK: milk2
"""

f = open('milk2.in', 'r')
w = open('milk2.out', 'w')

fileAsArray = (f.read()).split()

del fileAsArray[0]


allTimes = []
q = 0
while q < len(fileAsArray):
    allTimes.append([int(fileAsArray[q]), int(fileAsArray[q+1])])
    q += 2

allTimes.sort()

startTimes = []
endTimes = []

q = 0
while q < len(allTimes):
    startTimes.append(allTimes[q][0])
    endTimes.append(allTimes[q][1])
    q += 1


common = startTimes[0]
startTimes[:] = [number for number in startTimes]
endTimes[:] = [number for number in endTimes]


i = 0
a = 0
minStart = startTimes[0]
maxEnd = endTimes[0]
timeMilkingArray = []
timeWithoutMilkingArray = []

while i < len(startTimes):
    if startTimes[i] <= maxEnd:
        if endTimes[i] > maxEnd:
            maxEnd = endTimes[i]
    else:
        timeMilkingArray.append(maxEnd - minStart)
        minStart = startTimes[i]
        timeWithoutMilkingArray.append(minStart - maxEnd)
        maxEnd = endTimes[i]
    i += 1
else:
    timeMilkingArray.append(maxEnd-minStart)

maxWithMilking = 0 if len(timeMilkingArray) == 0 else max(timeMilkingArray)
maxWithoutMilking = 0 if len(
    timeWithoutMilkingArray) == 0 else max(timeWithoutMilkingArray)

output = str(maxWithMilking) + " " + str(maxWithoutMilking) + '\n'
w.write(output)
