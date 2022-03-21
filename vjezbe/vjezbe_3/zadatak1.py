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
        self.ax = []
        self.ay = []
        self.deltat = 0.1

    def set_initial_conditions(self,v0,theta1,x0,y0):
        self.t.append(0)
        self.vx.append(v0*math.cos((theta1/360)*2*np.pi))
        self.vy.append(v0*math.sin((theta1/360)*2*np.pi))
        self.x.append(x0)
        self.y.append(y0)
        self.ax.append(self.ax1)
        self.ay.append(self.ay1)
        self.theta.append((theta1/360)*2*np.pi)

    def reset(self):
        self.__init__()

    def __move(self):
        self.t.append(self.t[-1]+self.deltat)
        self.ax.append(self.ax)
        self.ay.append(self.ay)
        self.x.append(self.x[-1]+self.vx[-1]*self.deltat)
        self.y.append(self.y[-1]-self.ay[-1]*self.deltat)
        self.vx.append(self.vx)
        self.vy.append(self.vy[-1]-self.ay[-1]*self.deltat)
        
    def range(self):
        while self.y[-1] > 0:
            self.__move()
        return self.x[-1]

p1 = Particle(0,0,15,40)