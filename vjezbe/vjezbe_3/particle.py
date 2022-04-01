import numpy as np
import matplotlib.pyplot as plt
import math

class Particle():
    def __init__(self):
        self.xlista = []
        self.ylista = []
        self.vxlista = []
        self.vylista = []
        self.t = []
        self.ax = []
        self.g = -9.81

    def set_initial_conditions(self,v0,theta_t,x0,y0):
        self.k = theta_t
        self.theta = math.radians(theta_t)
        self.v0 = v0
        self.x0 = x0
        self.y0 = y0
        self.v0y = self.v0*math.sin(self.theta)
        self.v0x = self.v0*math.cos(self.theta)
        self.t.append(0)
        self.ax.append(0)
        self.xlista.append(0)
        self.ylista.append(0)
        self.vylista.append(self.v0y)
        self.vxlista.append(self.v0x)

    def reset(self):
        self.__init__()
        self.v0 = 0
        self.x0 = 0
        self.y0 = 0
        self.theta = 0

    def __move(self, dt):
        self.t.append(self.t[-1]+dt)
        self.vylista.append(self.vylista[-1]+self.g*dt)
        self.vxlista.append(self.vxlista[-1]+self.ax[-1]*dt)
        self.xlista.append(self.xlista[-1]+self.vxlista[-1]*dt)
        self.ylista.append(self.ylista[-1]+self.vylista[-1]*dt)
        

    def range(self,dt):
        while self.ylista[-1]>=0:
            self.__move(dt)
        return self.xlista[-1]
        

    def range_analitic(self):
        g = 9.81
        self.kut = math.sin(2*self.theta)
        self.X = ((self.v0**2)*self.kut) / g

    
    def printInfo(self):
        while self.ylista[-1]>=0:
            self.__move()
        print("Za v={} i kut {}, domet je {}.".format(self.v0,self.k,self.xlista[-1]))


    def plot_trajectory(self):
        plt.plot(self.xlista,self.ylista,"r")
        plt.show()
        
    
        