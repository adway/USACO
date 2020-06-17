"""
ID: adway1
LANG: PYTHON3
TASK: beads
"""

infile = open("beads.in", "r").readlines()
outfile = open("beads.out", "w")

necklaceStr = infile[1].strip()
necklaceList = list(necklaceStr)
numBeads = infile[0].strip()

maxSum = 0

# Check and make sure necklace isn't all the same
if(len(set(necklaceList)) == 1):
    maxSum = len(necklaceList)
    outfile.write(str(maxSum) + "\n")
else:
    necklaceList = list(necklaceStr+necklaceStr)
    numBeads = len(necklaceList)

    # Let's handle the white beads first

    def setWhiteColor(currentList):
        if currentList == "right":
            for bead in rightList:
                if bead == "r":
                    whiteColor = "r"
                    return whiteColor
                elif bead == "b":
                    whiteColor = "b"
                    return whiteColor
        elif currentList == "left":
            for bead in leftList:
                if bead == "r":
                    whiteColor = "r"
                    return whiteColor
                elif bead == "b":
                    whiteColor = "b"
                    return whiteColor

    def getColorCount(color, currentList):
        rightCount = 0
        leftCount = 0

        if currentList == 'right':
            for bead in rightList:
                if bead == color or bead == "w":
                    rightCount += 1
                else:
                    return rightCount
        if currentList == 'left':
            for bead in leftList:
                if bead == color or bead == "w":
                    leftCount += 1
                else:
                    return leftCount
    rightPos = 1
    leftPos = 1

    for bead in necklaceList:
        rightList = necklaceList[rightPos:]
        if rightList == []:
            rightList.append(0)
        print("right:", rightList)

        if rightList[0] == "r":
            rMax = getColorCount("r", "right")
        elif len(rightList) == 1:
            rMax = 1
        elif rightList[0] == "b":
            rMax = getColorCount("b", "right")
        elif rightList[0] == "w":
            rCurrentColor = None
            rCurrentColor = setWhiteColor("right")
            rMax = getColorCount(rCurrentColor, "right")
        elif rightList[0] == 0:
            rMax = 0

        if rMax == None:
            rMax = 0
        rightPos += 1
        print("rMax:", rMax)

        # Left List

        tempLeftList = necklaceList[:leftPos]
        leftList = tempLeftList[::-1]
        print("left:", leftList)

        if leftList[0] == "r":
            lMax = getColorCount("r", "left")
        elif leftList[0] == "b":
            lMax = getColorCount("b", "left")
        elif leftList[0] == "w":
            lCurrentColor = None
            lCurrentColor = setWhiteColor("left")
            lMax = getColorCount(lCurrentColor, "left")

        if lMax == None:
            lMax = 0
        leftPos += 1
        print("lMax:", lMax)

        # handle max
        maxSum = max(rMax + lMax, maxSum)
        print("max: ", maxSum)
        rMax = 0
        lMax = 0
        if int(maxSum) > int(numBeads):
            maxSum = int(numBeads)

    outfile.write(str(maxSum) + "\n")
    outfile.close()
