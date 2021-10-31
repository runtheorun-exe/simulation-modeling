from random import randint
import matplotlib.pyplot as plt
import numpy as np



def one_inf_three():
    n = 1000
    nodes = [0] * n
    infectionDone = False
    currentInfected = 1
    infectedPerLoop = 0
    infectionRate = []
    curInf = []
    attempts = []
    x=1
    nodes[randint(0,n-1)] = 1

    while not infectionDone:
        for i in range(n):
            for j in range(3):
                if nodes[i] == 1:
                    target = randint(0,n-1)
                    if nodes[target] == 0:
                        nodes[target] = 1
                        infectedPerLoop+=1
                currentInfected += infectedPerLoop
                curInf.append(currentInfected)
                infectedPerLoop = 0
        infectionRate.append (currentInfected)
        attempts.append(x)
        x+=1
        if currentInfected == n:infectionDone = True 

    xpoints_13 = np.array(attempts)
    ypoints_13 = np.array(infectionRate)
    # plt.plot(xpoints, ypoints)
    # plt.savefig("lab2/infectionrate.jpg")
    # plt.show()

