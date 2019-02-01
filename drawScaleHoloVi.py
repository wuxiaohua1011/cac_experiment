import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

S = []
S_VI = []
Holo = []
for s in range(0,100):
    for vi in range(0,100):
        for holo in range(0,100):
            if(vi-holo-s >=11 and vi-holo-s <=12):
                S_VI.append(vi)
                Holo.append(holo)
                S.append(s)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(S,S_VI,Holo)
ax.set_title("Graph 8: Comparative importance of Scale in Video and Holographic Conferencing")
ax.set_xlabel("X=S")
ax.set_ylabel("Y=S_VI")
ax.set_zlabel("Z=Holo")
plt.show()
