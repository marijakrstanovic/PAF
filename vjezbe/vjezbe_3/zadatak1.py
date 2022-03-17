from numpy import void0
import numpy as np
import math

class Particle():
    def __init__(self):
        self.vx=[]
        self.vy=[]
        self.t=[]
        self.x=[]
        self.y=[]
        self.theta=[]
        g0=10
        g=[g0]
        deltat=0.01
        N=1000
        for i in range(0,N):
            self.t.append((deltat/N)*i)

    def set_initial_conditions(self,v0,theta1,x0,y0):
        self.vx.append(v0*math.cos((theta1/360)*2*np.pi))
        self.vy.append(v0*math.sin((theta1/360)*2*np.pi))
        self.x.append(x0)
        self.y.append(y0)
        self.theta.append((theta1/360)*2*np.pi)

    def reset(self):
        del(self.v0)
        del(self.x0)
        del(self.y0)
        del(self.theta)

    
