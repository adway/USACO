"""
ID: adway
LANG: PYTHON3
PROG: gift1
"""

fin = open('gift1.in', 'r')
fout = open('gift1.out', 'w')

file = fin.read()
file = file.split('\n')

people = []

for person in range(int(file[0])):
    people.append([file[person + 1], 0, 0, 0])

del file[0:int(file[0])+1]
del file[-1]

for person in range(int(len(people))):
    # How much each person gives
    giver = file[0]
    info = file[1].split(" ")
    giving = int(info[0])
    num_shared = int(info[1])

    # People actually getting the money
    recepients = file[2:2 + num_shared]

    del file[0:2 + num_shared]

    if giving > 0:
        rem = giving % num_shared
    else:
        rem = 0

    for person in range(int(len(people))):
        if people[person][0] == giver:
            people[person][1] -= giving
            people[person][2] += rem
        if people[person][0] in recepients:
            people[person][3] += giving // num_shared


output = ""

for person in range(int(len(people))):
    output += people[person][0] + " " + \
        str(people[person][1]+people[person][2]+people[person][3]) + "\n"

fout.write(output)
