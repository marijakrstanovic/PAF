import numpy as np
import math
import matplotlib.pyplot as plt

class ProjectileDrop():
    def __init__(self,h0,vx0):
        self.h = h0
        self.vx = vx0
        self.t = 0
        self.vy = 0
        self.y = h0
        self.x = 0
        self.hlist = []
        self.vxlist = []
        self.tlist = []
        self.vylist = []
        self.ylist = []
        self.xlist = []
        self.hlist.append(self.h)
        self.vxlist.append(self.vx)
        self.tlist.append(self.t)
        self.ylist.append(self.y)
        self.vylist.append(self.vy)
        self.xlist.append(self.x)
        print("Objekt je uspjesno stvoren.")
        print("Njegova pocetna visina je {} m, a pocetna brzina je {} m\s.".format(self.h,self.vx))

    
    def promjena_visine(self,h0):
        self.h = h0

    def promjena_brzine(self,vx0):
        self.vx = vx0
    
    def reset(self):
        self.h = self.hlist[0]
        self.v = self.vxlist[0]
        self.t = 0
        self.hlist = []
        self.vxlist = []
        self.tlist = []
        self.hlist.append(self.h)
        self.vxlist.append(self.v)
        self.tlist.append(self.t)


    def __move(self,dt):
        self.vy = self.vy - 9.81*dt
        self.vx = self.vx 
        self.y = self.y + self.vy*dt
        self.x = self.x + self.vx*dt
        self.t = self.t + dt
        self.vylist.append(abs(self.vy))
        self.ylist.append(self.y)
        self.tlist.append(self.t)
        self.xlist.append(self.x)

    def run(self,dt):
        while self.y > 0:
            self.__move(dt)
        return self.vylist,self.ylist,self.xlist,self.tlist

    def padanje(self,dt):
        while self.y > 0:
            self.__move(dt)
        return self.t

    def __move_vjetar(self,k,dt):
        self.vy = self.vy - 9.81*dt
        a = -9.81 - k*self.vx
        self.vx = self.vx + a*dt
        self.y = self.y + self.vy*dt
        self.x = self.x + self.vx*dt
        self.t = self.t + dt
        self.vylist.append(self.vy)
        self.vxlist.append(self.vx)
        self.ylist.append(self.y)
        self.xlist.append(self.x)
        self.tlist.append(self.t)

    def meta(self,p,r,k,dt):
        self.p = p
        self.r = r
        t = 0
        vrijeme = 0
        udaljenost = []
        while self.y > 0:
            self.__move_vjetar(k,dt)

            for i in range(len(self.ylist)):
                udaljenost.append(math.sqrt((p-self.xlist[i])*2+(0-self.ylist[i])*2)-r)

            for el in udaljenost:
                if el <= 0:
                    vrijeme = t 
                    break

            vrijeme = vrijeme +  0.1

        return self.xlist,self.ylist,self.p,self.r
        
        krug = plt.Circle((self.p, 0), self.r, fill=False)
        fig, ax = plt.subplots()
        ax.add_patch(krug)
        ax.plot(self.xlist, self.ylist)
        
        plt.show()




