import math
import Particle as pr
import matplotlib.pyplot as plt
import numpy as np


p1 = pr.Particle()
p1.set_initial_conditions(np.array((1.496*10**(11),0)),np.array((0.1,0.1)),5.9742*10**(24),1.989*10**(30),np.array((0,29783)),np.array((0,0)),100)#(r1,r2,m1,m2,v1,v2,dt)
p1.range()
p1.plot_trajectory()

