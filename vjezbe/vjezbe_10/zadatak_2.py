import Particle as pr
import numpy as np
import matplotlib.pyplot as plt

p1 = pr.Particle()
p1.set_initial_conditions(np.array((0,0,1)),np.array((0,0,0)),1,1,np.array((0.1,0.1,0.1)),0.01)#(self,B,E,m,q,v,dt)


p2 = pr.Particle()
p2.set_initial_conditions(np.array((0,0,1)),np.array((0,0,0)),1,1,np.array((0.1,0.1,0.1)),0.01)


lista1,lista2,lista3 = p1.range(18)
lista4,lista5,lista6 = p2.range_RK(18)

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot3D(lista1,lista2,lista3,"r",label="Euler")
ax.plot3D(lista4,lista5,lista6, "b",label="Runge-Kutta")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.view_init(30,30)
plt.legend()
plt.show()