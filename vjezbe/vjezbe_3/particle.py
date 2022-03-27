import numpy as np
import matplotlib.pyplot as plt
import math

class Particle():
    def __init__(self):
        self.dt = 0.01
        self.deltat = []
        self.xlista = []
        self.ylista = []
        self.vxlista = []
        self.vylista = []
        self.g = -9.81
        self.deltat.append(self.dt)

    def set_initial_conditions(self,v0,theta_t,x0,y0):
        self.k = theta_t
        self.theta = math.radians(theta_t)
        self.v0 = v0
        self.x0 = x0
        self.y0 = y0

    def reset(self):
        self.__init__()
        self.v0 = 0
        self.x0 = 0
        self.y0 = 0
        self.theta = 0

    def __move(self):
        self.v0x = self.v0*math.cos(self.theta)
        self.v0y = self.v0*math.sin(self.theta)
        for i in range(1000):
            self.x0 = self.x0 + self.v0x*self.dt
            self.v0y = self.v0y + self.g*self.dt
            self.y0 = self.y0 + self.v0y*self.dt
            if self.y0<=0:
                break
            self.xlista.append(self.x0)
            self.ylista.append(self.y0)

    def range(self):
        x = self.x0
        v = self.v0
        self.__move()
        self.d = self.x0 - x
        print("Za v={} i kut{} domet je{}".format(v,self.k,(self.d)))


    def range_analitic(self):
        g = 9.81
        self.kut = math.sin(2*self.theta)
        self.X = ((self.v0**2)*self.kut) / g

    def relative_error(self):
        self.range_analitic()
        self.range()
        E = ((self.X - self.d)/self.X)*100
        print("Relativna pogreska je {}".format(E))

    def Relative_error(self):
        v = self.v0
        k = self.theta
        vy = self.v0 * math.sin(self.theta)
        vx = self.v0 * math.cos(self.theta)
        x = self.x0 
        y = self.y0
        x_lista = []
        self.Dt = 0
        self.T = []
        self.re = []
        for i in range(1000):
            self.Dt = self.Dt + self.dt
            x = x + vx*self.Dt
            vy = vy + self.g*self.Dt
            y = y + vy*self.Dt
            if y <= 0:
               break
            self.T.append(self.Dt)
            x_lista.append(x)
        self.range_analitic()
        a = self.x0
        self.__move()
        x_lista = [x - a for x in x_lista]
        x_lista = [-x for x in x_lista]
        self.re = list(map(lambda x: x - self.X, x_lista))
        self.re = list(map(lambda x: x/self.X, self.re))
        self.re = [-x for x in self.re]
        self.re = list(map(lambda x: x*100, self.re))
        
    def plot_trajectory(self):
        plt.plot(self.xlista,self.ylista,"r")
        plt.show()
        
    def plot_trayectory1(self):
        plt.plot(self.T, self.re, 'b')
        plt.xlabel("dt [s]")
        plt.ylabel("absolute relative error [%]")
        plt.title("Relativna pogreska")
        plt.show()