import math
import numpy as np
import matplotlib.pyplot as plt

class Force():
    def __init__(self,m,v,x,dt,func):
        self.m = m
        self.v = v
        self.x = x
        self.dt = dt
        self.t = 0
        self.func = func
        self.f = self.func(self.v,self.x,self.t)


    def move(self,t):
        self.a1 = []
        self.x1 = []
        self.v1 = []
        self.t1 = []
        n = int(t/self.dt)
        for i in range(n):
            self.f = self.func(self.v,self.x,self.t)
            self.a = self.f/self.m
            self.v = self.v + self.a * self.dt
            self.x = self.x + self.v * self.dt
            self.t = self.t + self.dt
            self.a1.append(self.a)
            self.v1.append(self.v)
            self.x1.append(self.x)
            self.t1.append(self.t)
            

    def plot_trajectory(self):
        fig, (ax1, ax2, ax3) = plt.subplots(1, 3)
        ax1.plot(self.t1, self.x1, 'b')
        ax1.set_title('x-t graf')
        ax2.plot(self.t1, self.v1, 'b')
        ax2.set_title('v-t graf')
        ax3.plot(self.t1, self.a1, 'b')
        ax3.set_title('a-t graf')
        plt.show()