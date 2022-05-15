import math
import matplotlib.pyplot as plt
import Projectile as pr

p1 = pr.Particle()
p1.set_initial_conditions(0.001,10,0.1,5,5,45,0,0,0.01)#(self,R,A,C,v,m,theta,x,y,dt)
p1.range_RK()
p1.plot_trajectory_RK()


p2 = pr.Particle()
p2.set_initial_conditions(0.001,10,0.1,5,5,45,0,0,0.01)
p2.range()
p2.plot_trajectory()



xRlista,yRlista = p1.listeR()
xlista,ylista = p2.liste()

fig, ax = plt.subplots()

ax.plot(xlista, ylista)
ax.plot(xRlista, yRlista, color="m")
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.legend(["Eulerova metoda", "Runge-Kutta"])

plt.show()