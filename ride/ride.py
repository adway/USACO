"""
ID: adway
LANG: PYTHON3
PROG: ride
"""

fin = open('ride.in', 'r')
fout = open('ride.out', 'w')

x = list(fin.readline())
y = list(fin.readline())

x.remove('\n')
y.remove('\n')

x_prod = 1
y_prod = 1

for i in range(int(len(x))):
    x_prod *= ord(x[i])-ord('A')+1


for i in range(int(len(y))):
    y_prod *= ord(y[i])-ord('A')+1

if x_prod % 47 == y_prod % 47:
    fout.write('GO\n')
else:
    fout.write('STAY\n')
