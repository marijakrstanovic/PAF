import numpy as np
import matplotlib.pyplot as plt
import math
import numpy as np

class Particle():
    def __init__(self):
        #Zemlja
        self.xlista1 = []
        self.ylista1 = []
        self.vlista1 = []
        self.alista1 = []
        #Sunce
        self.xlista2 = []
        self.ylista2 = []
        self.vlista2 = []
        self.alista2 = []

        self.tlista = []
        self.G = 6.67408*10**(-11)
        self.tuk = 365.242*24*3600
        

    def set_initial_conditions(self,r1,r2,m1,m2,v1,v2,dt):  
        self.r1 = r1
        self.r2 = r2
        self.xlista1.append(1.486*10**(11))
        self.ylista1.append(0)
        self.xlista2.append(0)
        self.ylista2.append(0)
        self.v1 = v1
        self.v2 = v2
        self.m1 = m1
        self.m2 = m2
        self.t = 0
        self.dt = dt
        

    def reset(self):
        self.__init__()
        

    def __move(self):
        b1 = (self.r1-self.r2)**2
        b2 = (self.r2-self.r1)**2
        c1 = math.sqrt(b1[0]+b1[1])
        c2 = math.sqrt(b2[0]+b2[1])

        self.t = self.t + self.dt

        
        self.a1 = -self.G*(self.m2/np.abs(c1**3)*(self.r1-self.r2))
        self.a2 = -self.G*(self.m1/np.abs(c2**3)*(self.r2-self.r1))
        self.v1= self.v1 + self.a1*self.dt
        self.v2 = self.v2 + self.a2*self.dt
        self.r1 = self.r1 + self.v1*self.dt
        self.r2 = self.r2 + self.v2*self.dt

       
        self.xlista1.append(self.r1[0])
        self.ylista1.append(self.r1[1])
        self.xlista2.append(self.r2[0])
        self.ylista2.append(self.r2[1])
        
    def range(self):
        while self.t <= self.tuk:
            self.__move()
        return self.xlista1,self.ylista1,self.xlista2,self.ylista2

    def plot_trajectory(self):
        plt.figure(figsize=(5.5,5.5))
        plt.title("x-y graf")
        plt.plot(self.xlista1,self.ylista1,"r",label="Zemlja")
        plt.plot(self.xlista2,self.ylista2,"b",label="Sunce")
        plt.legend()
        plt.show()

        
    