import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
M = []
G = []
S_VI = []
for m in range(0,100):
    for g in range(0,100):
        for s_vi in range(100):
            if(m + g + s_vi <= 88 and m + g + s_vi >= 87):
                M.append(m)
                G.append(g)
                S_VI.append(s_vi)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(M,G,S_VI)
ax.set_title("Graph 4: MicroExpression vs Gesture in Video Conferencing")
ax.set_xlabel("X=MicroExpression")
ax.set_ylabel("Y=Gesture")
ax.set_zlabel("Z=Video Conferencing")
plt.show()
