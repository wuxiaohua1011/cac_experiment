import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
M = []
G = []
S_VR = []
for m in range(0,100):
    for g in range(0,100):
        for s_vr in range(100):
            if(2 * m + g - s_vr <= 142 and 2 * m + g - s_vr >= 141):
                M.append(m)
                G.append(g)
                S_VR.append(s_vr)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(M,G,S_VR)
ax.set_title("Graph 4: MicroExpression vs Gesture in VR")
ax.set_xlabel("X=MicroExpression")
ax.set_ylabel("Y=Gesture")
ax.set_zlabel("Z=Virtural Reality")
plt.show()
