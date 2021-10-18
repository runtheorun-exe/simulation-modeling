from random import randint
import matplotlib.pyplot as plt
import numpy as np
n = 1000
nodes = [0] * n
infectionDone = False
currentInfected = 1
infectedPerLoop = 0
infectionRate = []
attempts = []
x=1

nodes[randint(0,n-1)] = 1

while infectionDone == False:
    for i in range(n):
        if nodes[i] == 1:
            target = randint(0,n-1)
            if nodes[target] == 0:
                nodes[target] = 1
                infectedPerLoop+=1
        currentInfected += infectedPerLoop
        infectionRate.append (currentInfected)
        attempts.append(x)
        x+=1
        infectedPerLoop = 0
        
    if currentInfected == n: 
        print(currentInfected)
        infectionDone = True 
        print ("Done")


xpoints = np.array(attempts)
ypoints = np.array(infectionRate)
plt.plot(xpoints,ypoints)
plt.show()
plt.savefig("infectionrate.jpg")