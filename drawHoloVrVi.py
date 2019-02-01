import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

EHolo = []
EVr = []
EVi = []
for M in range(0,100):
    for G in range(0,100):
        for S in range(0,100):
            for Hp in range(0,100):
                if(M+G+S+Hp == 100): # equation 4
                    EHolo.append(M+G+S - 76.55) #Equation 1
                    EVr.append(G+S+Hp - 45.83) #Equation 2
                    EVi.append(M+G-87.66)#Equation 3

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
# ax.plot(EHolo, EVr, EVi, '-b')
ax.set_title("Graph 3: S_Holo vs S_VR vs S_Vi")
ax.plot(EHolo, EVr, EVi)
ax.set_xlabel("X=S_Holo")
ax.set_ylabel("Y=S_VR")
ax.set_zlabel("Z=S_Vi")

plt.show()
