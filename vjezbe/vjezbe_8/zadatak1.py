import math
import matplotlib.pyplot as plt
import Projectile as pr

p1 = pr.Particle()
p1.set_initial_conditions(0.01,1,0.1,10,5,40,0,0,0.001)#(self,R,A,C,v,m,theta,x,y,dt)
p1.range()
p1.plot_trajectory()
p1.reset()