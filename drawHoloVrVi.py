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
                    EHolo.append(M+G+S - 87.66) #Equation 1
                    EVr.append(G+S+Hp - 76.55) #Equation 2
                    EVi.append(M+G - 45.83)#Equation 3

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
# ax.plot(EHolo, EVr, EVi, '-b')
ax.set_title("EHolo vs EVr vs EVi")
ax.plot(EHolo, EVr, EVi)
ax.set_xlabel("X=EHolo")
ax.set_ylabel("Y=EVr")
ax.set_zlabel("Z=EVi")

plt.show()
