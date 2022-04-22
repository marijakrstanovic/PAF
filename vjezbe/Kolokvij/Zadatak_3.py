import ProjectileDrop as pd
import matplotlib.pyplot as plt

dt = 0.001
ob = pd.ProjectileDrop(2000,200)
vylista,ylista,xlista,tlista=ob.run(dt)

fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.plot(xlista, ylista)
ax1.set(xlabel='t [s]', ylabel='y [m]')
ax2.plot(tlista, vylista)
ax2.set(xlabel='t [s]', ylabel='v [m\s]')
plt.show()