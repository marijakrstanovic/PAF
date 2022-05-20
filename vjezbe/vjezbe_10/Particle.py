import numpy as np
import math
import matplotlib.pyplot as plt

class Particle():
    def __init__(self):
        self.xlista = []
        self.ylista = []
        self.zlista = []
        self.tlista = []
        self.xlista.append(0)
        self.ylista.append(0)
        self.zlista.append(0)
        self.tlista.append(0)
        

    def set_initial_conditions(self,B,E,m,q,v,dt):  #B-magnetno polje,E-elektricno polje,m-masa cestice,q-naboj,v-pocetna brzina,mora biti razlicita od nule za sve tri komponente
        self.B = B
        self.v = v
        self.E = E
        self.t = 0
        self.m = m
        self.q = q
        self.dt = dt
        self.tlista.append(self.t)

    def reset(self):
        self.__init__()
        self.set_initial_conditions(0,0,0,0,0,0)
       

    def __move(self):
        self.tlista.append(self.tlista[-1] + self.dt)

        self.a = ((self.q/self.m)*(self.E+np.cross(self.v,self.B)))

        self.v += self.a*self.dt

        self.xlista.append(self.xlista[-1]+self.v[0]*self.dt)
        self.ylista.append(self.ylista[-1]+self.v[1]*self.dt)
        self.zlista.append(self.zlista[-1]+self.v[2]*self.dt)
        
    def range(self,tuk):
        while self.tlista[-1]<=tuk:
            self.__move()
        return self.xlista,self.ylista,self.zlista

    def plot_trajectory(self):
        fig = plt.figure()
        ax = plt.axes(projection='3d')
        ax.plot3D(self.xlista,self.ylista,self.zlista,"r")
        plt.show()


    def __move_RK(self):
        self.tlista.append(self.tlista[-1] + self.dt)
        
        self.k1v = ((self.q/self.m)*(self.E+np.cross(self.v,self.B)))*self.dt
        self.k1 = self.v*self.dt

        self.k2v = ((self.q/self.m)*(self.E+np.cross(self.v+self.k1v/2,self.B)))*self.dt
        self.k2 = (self.v + self.k1v/2)*self.dt

        self.k3v =((self.q/self.m)*(self.E+np.cross(self.v+self.k2v/2,self.B)))*self.dt
        self.k3 = (self.v + self.k2v/2)*self.dt

        self.k4v = ((self.q/self.m)*(self.E+np.cross(self.v+self.k3v,self.B)))* self.dt
        self.k4 = (self.v + self.k3v)*self.dt

        self.v = (self.v + (1/6)*(self.k1v + 2*self.k2v + 2*self.k3v + self.k4v))
        self.xlista.append(self.xlista[-1] + (1/6)*(self.k1[0] + 2*self.k2[0] + 2*self.k3[0] + self.k4[0]))
        self.ylista.append(self.ylista[-1] + (1/6)*(self.k1[1] + 2*self.k2[1] + 2*self.k3[1] + self.k4[1]))
        self.zlista.append(self.zlista[-1] + (1/6)*(self.k1[2] + 2*self.k2[2] + 2*self.k3[2] + self.k4[2]))

    def range_RK(self,tuk):
        while self.tlista[-1]<=tuk:
            self.__move_RK()
        return self.xlista,self.ylista,self.zlista