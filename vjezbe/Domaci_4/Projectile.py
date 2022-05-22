import numpy as np
import matplotlib.pyplot as plt
import math

class Particle():
    def __init__(self):
        self.xlista = []
        self.ylista = []
        self.vxlista = []
        self.vylista = []
        self.axlista = []
        self.aylista = []
        self.tlista = []
        self.g = -9.81

    def set_initial_conditions(self,R,A,C,v,m,theta,x,y,dt):  #A-povrsina,R-gustoca,C-trenje,m-masa
        self.x = x
        self.y = y
        self.v = v
        self.dt = dt
        self.R = R
        self.A = A
        self.C = C
        self.m = m
        self.t = 0
        self.theta = math.radians(theta)
        self.vx = self.v*math.cos(self.theta)
        self.vy = self.v*math.sin(self.theta)
        self.xlista.append(self.x)
        self.ylista.append(self.y)
        self.vxlista.append(self.vx)
        self.vylista.append(self.vy)
        self.tlista.append(self.t)

    def reset(self):
        self.xlista = [] 
        self.ylista = []
        self.tlista = []

    def __move(self):
        self.t = self.t + self.dt
        self.ax = -(self.R*self.C*self.A/2*self.m)*(self.vx**2)
        self.ay = self.g - (self.R*self.C*self.A/2*self.m)*(self.vy**2)
        self.vx = self.vx + self.ax*self.dt
        self.vy = self.vy + self.ay*self.dt
        self.x = self.x + self.vx*self.dt
        self.y = self.y + self.vy*self.dt
        #self.ay = self.g - (self.R*self.C*self.A/2*self.m)*(self.vy**2)
        #self.vy = self.vy + self.ay*self.dt
        #self.y = self.y + self.vy*self.dt
        self.tlista.append(self.t)
        self.xlista.append(self.x)
        self.ylista.append(self.y)
        self.vxlista.append(self.vx)
        self.vylista.append(self.vy)
        self.axlista.append(self.ax)
        self.aylista.append(self.ay)

    def range(self):
        while self.ylista[-1]>=0:
            self.__move()
        return self.xlista[-1]


    def plot_trajectory(self):
        plt.title("x-y graf")
        plt.xlabel("x[m]")
        plt.ylabel("y[m]")
        plt.plot(self.xlista,self.ylista,"r")
        plt.show()

    #akceleracija

    def _ax(self,x,v,t):
        return -((self.R*self.C*self.A)/(2*self.m))*(self.vxlista[-1])*abs((self.vxlista[-1]))

    def _ay(self,x,v,t):
        return self.g - ((self.R*self.C*self.A)/(2*self.m))*(self.vylista[-1])*abs(self.vylista[-1])

    def _RK(self):
        # x
        self.k1vx = self._ax(self.xlista[-1], self.vxlista[-1], self.tlista[-1])*self.dt
        self.k1x = self.vxlista[-1]*self.dt

        self.k2vx = self._ax((self.xlista[-1] + self.k1x/2), (self.vxlista[-1] + self.k1vx/2), (self.tlista[-1] + (self.dt/2)))*self.dt
        self.k2x = (self.vxlista[-1] + self.k1vx/2)*self.dt

        self.k3vx = self._ax((self.xlista[-1] + self.k2x/2), (self.vxlista[-1] + self.k2vx/2), (self.tlista[-1] + (self.dt/2)))*self.dt
        self.k3x = (self.vxlista[-1] + self.k2vx/2)*self.dt

        self.k4vx = self._ax((self.xlista[-1] + self.k3x), (self.vxlista[-1] + self.k3vx), (self.tlista[-1] + self.dt))* self.dt
        self.k4x = (self.vxlista[-1] + self.k3vx)*self.dt

        self.vxlista.append(self.vxlista[-1] + (1/6)*(self.k1vx + 2*self.k2vx + 2*self.k3vx + self.k4vx))
        self.xlista.append(self.xlista[-1] + (1/6)*(self.k1x + 2*self.k2x + 2*self.k3x + self.k4x))

        # y
        self.k1vy = self._ay(self.ylista[-1], self.vylista[-1], self.tlista[-1])*self.dt
        self.k1y = self.vylista[-1]*self.dt

        self.k2vy = self._ay((self.ylista[-1] + self.k1y/2), (self.vylista[-1] + self.k1vy/2), (self.tlista[-1] + (self.dt/2)))*self.dt
        self.k2y = (self.vylista[-1] + self.k1vy/2)*self.dt

        self.k3vy = self._ay((self.ylista[-1] + self.k2y/2), (self.vylista[-1] + self.k2vy/2), (self.tlista[-1] + self.dt/2))*self.dt
        self.k3y = (self.vylista[-1] + self.k2vy/2)*self.dt

        self.k4vy = self._ay((self.ylista[-1] + self.k3y), (self.vylista[-1] + self.k3vx), (self.tlista[-1] + self.dt))* self.dt
        self.k4y = (self.vylista[-1] + self.k3vx)*self.dt

        self.vylista.append(self.vylista[-1] + (1/6)*(self.k1vy + 2*self.k2vy + 2*self.k3vy + self.k4vy))
        self.ylista.append(self.ylista[-1] + (1/6)*(self.k1y + 2*self.k2y + 2*self.k3y + self.k4y))


    def range_RK(self):
        while self.ylista[-1] >= 0:
            self._RK()
        return self.xlista[-1]

    def plot_trajectory_RK(self):
        plt.title("x-y graf")
        plt.xlabel("x[m]")
        plt.ylabel("y[m]")
        plt.plot(self.xlista,self.ylista,"r")
        plt.show()
        #print(self.xlistaR,self.ylistaR)
        

    def listeR(self):
        while self.ylista[-1] >= 0:
            self._RK()
        return self.xlista,self.ylista

    def liste(self):
        while self.ylista[-1] >= 0:
            self.__move()
        return self.xlista,self.ylista

    def lik(self,lik,r,a):
        if lik == "kugla":
            self.A = r**2*np.pi
        else:
            self.A = a**2

    
    def angle_to_hit_target(self, r, xm, ym, dt, v, m):
        self.r = r
        self.xm = xm
        self.ym = ym
        self.v = 0
        kut1 = 0    #angle_to_hit_target
        kut = 0
        k = True

        while k:
            D = []
            self.reset()
            self.set_initial_conditions(2,0.01,1,v,m,kut,0,0,dt) # v0, theta, x0, y0, rho, Cd, A, m

            while self.ylista[-1] >= 0:
                self._RK()


            for i in range(len(self.ylista)):
                D.append(math.sqrt((ym-self.ylista[i])**2+(xm-self.xlista[i])**2)-r)

            for j in D:
                if j <= 0:
                    kut1 = kut
                    k = False
                    break
            
            kut = kut + 0.1

        krug = plt.Circle((self.xm, self.ym), self.r, fill=False)
        fig, ax = plt.subplots()
        ax.add_patch(krug)
        ax.plot(self.xlista, self.ylista)
        
        plt.show()

        if kut1 > 0:
            print("Početni kut da se pogodi meta je", kut1, "°.")
        else:
            print("Objekt nikada neće pogoditi metu.")
