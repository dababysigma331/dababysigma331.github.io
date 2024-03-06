import sys
import matplotlib
print(matplotlib.__version__)

import matplotlib.pyplot as plt
import numpy as np

global maxx
global maxy
global cords
xlist = []
ylist = []

try: 
    with open('test.txt', "r") as file:

        cords = [line.rstrip() for line in file]
    

except FileNotFoundError:
    print("dumb ahh file not found")
    

for number in cords:
    number = number.replace("," , "")
    number = number.split()
    xlist.append(number[0])
    ylist.append(number[1])

xlist = [int(x) for x in xlist]
ylist = [int(x) for x in ylist]
print(xlist)
print(ylist)

xstuff = np.array(xlist)
ystuff = np.array(ylist)

plt.plot(xstuff, ystuff, marker = "o")
plt.title("sound skibidf")
plt.xlabel("Sigma")
plt.ylabel("oh my gad")
plt.show()

plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
