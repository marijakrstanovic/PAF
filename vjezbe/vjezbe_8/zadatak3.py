import Projectile as prt
import matplotlib.pyplot as plt

C_lista = []

for i in range(1000):
    C = i * 0.001
    C_lista.append(C)

m_lista = []

for i in range(1000):
    m = 0.005 * (i+1)
    m_lista.append(m)

range_list1 = []
range_list2 = []

p1 = prt.Particle()

for element in C_lista:
    p1.C = element
    p1.set_initial_conditions(1, 1, element, 40, 2, 60, 0, 0,0.01)#(self,R,A,C,v,m,theta,x,y,dt)   
    range_list1.append(p1.range_RK())
    p1.reset()

plt.plot(C_lista,range_list1)
plt.xlabel("Cd")
plt.ylabel("range [m]")
plt.show()


C = 0.1
for element in m_lista:
    p1.m = element
    p1.set_initial_conditions(1, 1, C, 40, element, 60, 0, 0,0.01)
    range_list2.append(p1.range_RK())
    p1.reset()

plt.plot(m_lista,range_list2)
plt.xlabel("m [kg]")
plt.ylabel("range [m]")
plt.show()