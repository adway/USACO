"""
ID: adway
LANG: PYTHON3
PROG: friday
"""

fin = open('friday.in', 'r')
fout = open('friday.out', 'w')

# Initialize variables
months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = [0, 0, 0, 0, 0, 0, 0]
dayOfTheWeek = 2

years = int(fin.read())

for yr in range(1900, 1900+years):
    if (yr % 400 == 0 and yr % 100 == 0) or (yr % 4 == 0 and yr % 100 != 0):
        months[1] = 29
    else:
        months[1] = 28
    for month in range(0, 12):
        for day in range(0, months[month]):
            if day == 12:
                days[dayOfTheWeek] += 1
            if dayOfTheWeek == 6:
                dayOfTheWeek = 0
            else:
                dayOfTheWeek += 1


output = ""

output = str(days[0]) + " " + str(days[1]) + " " + str(days[2]) + " " + \
    str(days[3]) + " " + str(days[4]) + " " + \
    str(days[5]) + " " + str(days[6]) + "\n"

fout.write(output)
