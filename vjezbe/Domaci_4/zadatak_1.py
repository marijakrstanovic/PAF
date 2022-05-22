import math
import matplotlib.pyplot as plt
import numpy as np
import Projectile as pr

p1 = pr.Particle()
p1.set_initial_conditions(0.01,1,0.1,10,5,40,0,0,0.001)#(self,R,A,C,v,m,theta,x,y,dt)
p1.lik("kugla",0.3,0.3)

p2 = pr.Particle()
p2.set_initial_conditions(0.01,1,0.1,10,5,40,0,0,0.001)#(self,R,A,C,v,m,theta,x,y,dt)
p2.lik("kugla",0.3,0.3)

xRlista1,yRlista1 = p1.listeR()
xlista2,ylista2 = p2.liste()


p3 = pr.Particle()
p3.set_initial_conditions(0.01,1,0.1,10,5,40,0,0,0.001)#(self,R,A,C,v,m,theta,x,y,dt)
p3.lik("kocka",0.3,0.3)

p4 = pr.Particle()
p4.set_initial_conditions(0.01,1,0.1,10,5,40,0,0,0.001)#(self,R,A,C,v,m,theta,x,y,dt)
p4.lik("kocka",0.3,0.3)

xRlista3,yRlista3 = p3.listeR()
xlista4,ylista4 = p4.liste()


plt.subplot(1,1,1)
plt.plot(xRlista1,yRlista1, 'r',label = "Runge-Kutta")
plt.plot(xlista2,ylista2, 'g', label = "Euler")
plt.legend(loc='upper right')
plt.title("Kugla")

plt.show()

plt.subplot(1,1,1)
plt.plot(xRlista3,yRlista3, 'r',label = "Runge-Kutta")
plt.plot(xlista4,ylista4, 'g', label = "Euler")
plt.legend(loc='upper right')
plt.title("Kocka")

plt.show()