import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
M = []
H = []
S_VR = []
for m in range(0,100):
    for h in range(0,100):
        for s_vr in range(100):
            if(m-h-s_vr >= 11 and m-h-s_vr <=12):
                M.append(m)
                H.append(h)
                S_VR.append(s_vr)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(M,H,S_VR)
ax.set_title("MicroExpression vs Headpose in VR")
ax.set_xlabel("X = MicroExpression")
ax.set_ylabel("Y = Headpose")
ax.set_zlabel("Z = Virtural Reality")
plt.show()
