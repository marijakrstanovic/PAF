import math
import numpy as np
import matplotlib.pyplot as plt

def kosi():
    x0=0
    y0=10
    g0=10
    theta=(60/360)*2*np.pi
    deltat=0.01
    v0=15
    v0x=v0*math.cos(theta)
    v0y=v0*math.sin(theta)
    x=[]
    y=[]
    g=[]
    vx=[]
    vy=[]
    x.append(x0)
    y.append(y0)
    vx.append(v0y)
    vy.append(v0x)
    while y0>0:
        x0=x0+v0x*deltat
        y0=y0+v0y*deltat
        v0x=v0x
        v0y=v0y-g0*deltat
        x.append(x0)
        y.append(y0)
        vx.append(v0x)
        vy.append(v0y)
        if y0<0:
            break

    fig=plt.figure(figsize=(6,4), dpi=200)
    ax=fig.add_axes([0.2, 0.2, 0.6, 0.6])
    ax.plot(x,y,)
    ax.set_xlabel('os-x')
    ax.set_ylabel('os-y')
    ax.set_title("x-y graf")
    plt.show()

    def maksimalna_visina():
        np.max[y]
        return y

    maksimalna_visina()

    def domet():
        while y0>0:
            x0=x0+v0x*deltat
            if y0<0:
                break
            print(x0)
    domet()
    
kosi()


