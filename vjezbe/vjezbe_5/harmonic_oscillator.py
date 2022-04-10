import numpy as np
import matplotlib.pyplot as plt
import math

class Harmonic_oscillator():
    def __init__(self):
        self.x = []
        self.v = []
        self.t = []
        self.a = []

    def set_initial_conditions(self,m,k,v,dt):
        self.m = m
        self.k = k
        self.v.append(v)
        self.t.append(0)
        self.a.append(0)
        self.x.append(0)
        self.dt = dt
        

    def reset(self):
        self.__init__()
        self.v = 0
        self.x = 0
        self.a = 0

    def oscillate(self, t):
        # t u zagradi označava vrijeme titranja
        # a=-(k/m)*x
        #v=v+a*dt
        #x=x+v*dt
        n = int(t/self.dt)
        for i in range(n):
            self.a.append((-(self.k/self.m))*self.x[-1])
            self.v.append(self.v[-1]+self.a[-1]*self.dt)
            self.x.append(self.x[-1]+self.v[-1]*self.dt)
            self.t.append(self.t[-1]+self.dt)
        return (self.t,self.x)
        

    def graf(self):
        figure,axes = plt.subplots(1,3,figsize=(14,4))
        axes[0].plot(self.t,self.x)
        axes[0].set_title("x/t GRAF")
        axes[0].set(xlabel="sekunda(s)",ylabel="metar(m)")
        axes[1].plot(self.t,self.v)
        axes[1].set_title("v/t GRAF")
        axes[1].set(xlabel="sekunda(s)",ylabel="metar/sekunda(m/s)")
        axes[2].plot(self.t,self.a)
        axes[2].set_title("a/t GRAF")
        axes[2].set(xlabel="sekunda(s)",ylabel="akceleracija(m/s^2)")
        plt.show()

    

    def period(self,t):
        self.t,self.x = self.oscillate(t)
        g = max(self.x)
        a = self.x.index(g)
        s = min(self.x)
        b = self.x.index(s)
        c = self.t[a]
        d = self.t[b]
        T = abs(c-d)*2
        print("Numericki izracun perioda je {}".format(T))

    def analiticki_period(self):
        T = 2*math.pi*math.sqrt(self.m/self.k)
        print("Analiticki izracun perioda iznosi {}".format(T))