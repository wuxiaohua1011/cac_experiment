import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

G = []
S_VI = []
S_VR = []
for g in range(0,100):
    for vi in range(0,100):
        for vr in range(0,100):
            if(g+vr+vi <= 34 and g+vr+vi >= 33):
                S_VI.append(vi)
                S_VR.append(vr)
                G.append(g)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(G, S_VR, S_VI)
ax.set_title("Graph 7: Comparative importance of Gesture in VR and Video Conferencing")
ax.set_xlabel("X=Gesture")
ax.set_ylabel("Y=VR")
ax.set_zlabel("Z=Video Conferencing")
plt.show()
