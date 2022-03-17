import numpy as np
import math
import matplotlib.pyplot as plt


def jednoliko(F,m):  #prilikom poziva funkcije,korisnik definira silu i masu
    deltat=0.01      #definiramo mali pomak kako bismo dobili aproksimaciju limesa 
    t=[]             #prazne liste za vrijednosti dobivenih iznosa,jer poslije crtamo graf
    x=[]
    v=[]
    a=[]
    t0=0             #zadani početni uvjet
    v0=0
    x0=0
    a0=F/m           #jednoliko gibanje,akceleracija konstantna
    a.append(a0)      #u listu stavljamo početne uvjete 
    t.append(t0)
    v.append(v0)
    x.append(x0)
    for i in range(1000):         #raspon 1000 jer je deltat zadana kao vrijednost 0.01
        t0=t0+deltat              #for petlja ide od 0 do 1000,uzima prvu vrijednost,pridodaje deltat i to stavlja u listu,uzima definirani broj njega poveća za deltat i ponovno ga stavlja u listu. to se ponavlja do 1000 koliki nam je zadan range
        v0=v0+a0*deltat
        x0=x0+v0*deltat
        x.append(x0)
        t.append(t0)
        v.append(v0)
        a.append(a0)
    
    figure,axes = plt.subplots(1,3,figsize=(14,4))
    axes[0].plot(t,x)
    axes[0].set_title("x/t GRAF")
    axes[0].set(xlabel="sekunda(s)",ylabel="metar(m)")
    axes[1].plot(t,v)
    axes[1].set_title("v/t GRAF")
    axes[1].set(xlabel="sekunda(s)",ylabel="metar/sekunda(m/s)")
    axes[2].plot(t,a)
    axes[2].set_title("a/t GRAF")
    axes[2].set(xlabel="sekunda(s)",ylabel="akceleracija(m/s^2)")
    
    plt.show()

jednoliko(10,2)
