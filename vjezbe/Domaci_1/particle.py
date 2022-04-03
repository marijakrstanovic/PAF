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
        self.xlista = []
        self.ylista = []
        self.t = []
        self.vxlista = []
        self.vylista = []
        self.ax = []
        theta = math.radians(theta_t) 
        self.v0 = v0
        self.x0 = x0
        self.y0 = y0
        self.v0y = self.v0*math.sin(theta)
        self.v0x = self.v0*math.cos(theta)
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
        return abs(self.xlista[-1])
        

    def range_analitic(self):
        g = 9.81
        self.kut = math.sin(2*self.theta)
        self.X = ((self.v0**2)*self.kut) / g
        return self.X
    
    def printInfo(self):
        while self.ylista[-1]>=0:
            self.__move(0.1)
        print("Za v={} i kut {}, domet je {}.".format(self.v0,self.k,self.xlista[-1]))


    def plot_trajectory(self):
        plt.plot(self.xlista,self.ylista,"r")
        plt.show()
        
    def total_time(self):
        while self.ylista[-1]>=0:
            self.__move(0.1)
        return (self.t[-1])

    def max_speed(self):
        while self.ylista[-1] >=0:
            self.__move(0.1)
        self.vylista.sort()
        self.vxlista.sort()
        print("Maksimalna brzina:{}m/s.".format(math.sqrt((self.vxlista[-1])**2 + (self.vylista[-1])**2)))

    def velocity_to_hit_target(self,p,q,r,dt):
        self.p = p
        self.q = q
        self.r = r
        self.v0 = 0
        brzina1 = 0
        brzina2 = 0
        b = True

        while b:
            D = []
            self.set_initial_conditions(brzina1, 30, 0, 0)

            while self.ylista[-1]>=0:
                self.__move(dt)

            for i in range(len(self.ylista)):
                D.append(math.sqrt((p-self.xlista[i])**2 + (q-self.ylista[i])**2 )-r)
            for d in D:
                if d <= 0 :
                    brzina2 = brzina1
                    b = False
                    break

            brzina1 = brzina1 + 0.1

        print("Pocetna brzina je {} m/s.".format(brzina2))


    def angle_to_hit_target(self,p,q,r,dt):
        self.p = p
        self.q = q
        self.r = r
        self.v0 = 0
        kut1 = 0
        kut2 = 0
        k = True
        while k:
            D = []
            self.set_initial_conditions(50, kut1,0,0)

            while self.ylista[-1]>=0:
                self.__move(dt)

            for i in range(len(self.ylista)):
                D.append(math.sqrt((p-self.xlista[i])**2 +(q - self.ylista[i])**2 )-r)
            for d in D:
                if d <= r :
                    kut2 = kut1
                    k = False 
                    break
            kut1 = kut1 + 0.1

        print("Pocetni kut je {} °.".format(kut2))



    