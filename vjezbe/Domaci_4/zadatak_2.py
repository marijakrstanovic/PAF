import math
import matplotlib.pyplot as plt
import numpy as np
import Projectile as pr

p1 = pr.Particle()
p1.set_initial_conditions(0.01,1,0.1,30,5,40,0,0,0.001)#(self,R,A,C,v,m,theta,x,y,dt)
p1.range()
xlista,ylista = p1.liste()
p1.angle_to_hit_target(5,10,10,0.01,30,5)


p2 = pr.Particle()
p2.set_initial_conditions(0.01,1,0.1,20,5,40,0,0,0.001)#(self,R,A,C,v,m,theta,x,y,dt)
p2.range()
xlista,ylista = p2.liste()
p2.angle_to_hit_target(1,5,5,0.01,20,5)


p3 = pr.Particle()
p3.set_initial_conditions(0.01,1,0.1,30,5,40,0,0,0.001)#(self,R,A,C,v,m,theta,x,y,dt)
p3.range()
xlista,ylista = p3.liste()
p3.angle_to_hit_target(5,15,10,0.01,30,5)
