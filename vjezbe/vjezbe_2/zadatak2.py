import math
import matplotlib.pyplot as plt
import numpy as np

def kosi_hitac(v0, theta):
    v0x=v0*math.cos((theta/360)*2*np.pi)
    v0y=v0*math.sin((theta/360)*2*np.pi)
    deltat=0.01
    g0=10
    x0=0
    y0=0
    t0=0
    vx=v0x
    vy=[v0y]
    x=[x0]
    y=[y0]
    t=[t0]
    g=[g0]
    for i in range(1000):
        t0=t0+deltat
        x0=x0+v0x*deltat
        v0y=v0y-g0*deltat
        y0=y0+v0y*deltat
        vy.append(v0y)
        x.append(x0)
        y.append(y0)
        t.append(t0)
    
#x(t)=v0x*t
#y(t)=-1/2*g*t**2+v0y*t+h0
#h0 visina s koje je bačeno tijelo
#u x smjeru nema sile
#u y smjeru tijelo ubrzava g

    figure,axes = plt.subplots(1,3,figsize=(14,4))
    axes[0].plot(x,y)
    axes[0].set_title("x/y GRAF")
    axes[0].set(xlabel="metar(m)",ylabel="metar(m)")
    axes[1].plot(t,x)
    axes[1].set_title("x/t GRAF")
    axes[1].set(xlabel="sekunda(s)",ylabel="metar(m)")
    axes[2].plot(t,y)
    axes[2].set_title("y/t GRAF")
    axes[2].set(xlabel="sekunda(s)",ylabel="metar(m)")
    
    plt.show()

kosi_hitac(5,60)