import Particle as pr
import numpy as np
import matplotlib.pyplot as plt

def E(t):
    E = np.array([0,0,0])
    return E

def B(t):
    B = np.array([0,0,0.1])
    return B

def E1(t):
    #Ez = t/10
    E1 = np.array([0,0,t/10])
    return E1

def B1(t):
    #Bz = t/10
    B1 = np.array([0,0,t/10])
    return B1


#elektron
p1 = pr.Particle()
p1.set_initial_conditions(B,E,1,-1,np.array((0.1,0.1,0.1)),0.01)#(self,B,E,m,q,v,dt)


#elektron
p2 = pr.Particle()
p2.set_initial_conditions(B1,E1,1,-1,np.array((0.1,0.1,0.1)),0.01)

#pozitron
p3 = pr.Particle()
p3.set_initial_conditions(B1,E1,1,1,np.array((0.1,0.1,0.1)),0.01)

lista1,lista2,lista3 = p1.range(10)
lista4,lista5,lista6 = p2.range(10)
lista7,lista8,lista9 = p3.range(10)

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot3D(lista1,lista2,lista3,"r",label="B=const.")
ax.plot3D(lista4,lista5,lista6, "b",label="B=B(t)")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.view_init(30,30)
plt.legend()
plt.show()


fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot3D(lista4,lista5,lista6,"r",label="elektron")
ax.plot3D(lista7,lista8,lista9, "b",label="pozitron")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.view_init(30,30)
plt.legend()
plt.show()