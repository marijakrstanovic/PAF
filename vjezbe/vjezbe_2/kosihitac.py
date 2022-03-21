import math
from tkinter import N
import numpy as np
import matplotlib.pyplot as plt

def putanja_gibanja(v0,theta):
    v0x=v0*math.cos((theta/360)*2*np.pi)
    v0y=v0*math.sin((theta/360)*2*np.pi)
    deltat=0.01
    g=-9.81
    x0=0
    y0=0
    t0=0
    x=[]
    y=[]
    
    for i in range(1000):
        x0 = x0 + v0x * deltat
        v0y = v0y + g * deltat
        y0 = y0 + v0y*deltat
        x.append(x0)
        y.append(y0)
        if y0 <= 0:
            break

    plt.plot(x,y)
    plt.show()

def maksimalna_visina(v0,theta):
    v0y=v0*math.sin((theta/360)*2*np.pi)
    deltat = 0.01
    g=-9.81
    y0 = 0
    y = []
    for i in range(1000):
        v0y=v0y + g*deltat
        y0=y0+v0y*deltat
        y.append(y0)
        if y0<=0:
            break
    y.sort()
    print("Maksimalna visina:{}m".format(y[-1]))

def domet(v0,theta):
    v0x=v0*math.cos((theta/360)*2*np.pi)
    v0y=v0*math.sin((theta/360)*2*np.pi)
    deltat = 0.01
    g=-9.81
    y0=0
    x0=0
    x=[]

    for i in range(1000):
        x0 = x0 + v0x*deltat
        v0y = v0y + g*deltat
        y0 = y0 + v0y*deltat
        x.append(x0)
        if y0<=0:
            break
    print("Domet:{}m.".format(x[-1]))


def maksimalna_brzina(v0 , theta):
    v0x=v0*math.cos((theta/360)*2*np.pi)
    v0y=v0*math.sin((theta/360)*2*np.pi)
    deltat=0.01
    g=-9.81
    y0=0
    vx = []
    vy = []
    for i in range(1000):
        v0x = v0*math.cos((theta/360)*2*np.pi)
        v0y = v0y + g*deltat
        y0 = y0 +v0y*deltat
        vx.append(v0x)
        vy.append(v0y)
        if y0<=0:
            break
    vx.sort()
    vy.sort()
    print("Maksimalna brzina:{}m/s.".format(math.sqrt((vx[-1])**2 + (vy[-1])**2)))


def meta(theta,v0,t,p,q,r):
    v0x=v0*math.cos((theta/360)*2*np.pi)
    v0y=v0*math.sin((theta/360)*2*np.pi)
    deltat=0.01
    x0=0
    y0=0
    g=-9.81
    x=[]
    y=[]
    lst=[]
    for i in range(1000):
        x0 = x0 +v0x*deltat
        v0y = v0y + g*deltat
        y0 = y0 + v0y*deltat
        x.append(x0)
        y.append(y0)
        if y0 <= 0 :
            break
        for j in range(i):
            R = r**2
            D = math.sqrt((p-x0)**2 + (q-y0)**2)
            d = D-R
            lst.append(d)

    def lst1(lst,minimum):
        if min(lst) <= minimum:
            print("Meta je pogodena.")
        else:
            print("Meta nije pogodena. Najmanja udaljenost iznosi {}.".format(min(lst)))
    
    lst1(lst,0)
    krug=plt.Circle((p,q),r,fill=False)
    plt.figure(figsize=(6,6))
    plt.gca().add_patch(krug)
    plt.plot()
    plt.plot(x,y)
    plt.scatter(p,q,s=2)
    plt.show()


    
    