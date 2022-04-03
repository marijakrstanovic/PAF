import matplotlib.pyplot as plt
import numpy as np


def two_step(func,x,h):
    return((func(x+h)-func(x))/h)

def three_step(func,x,h):
    return((func(x+h)-func(x-h))/(2*h))

def derivacija(func,a,b,h,m):
    x_lista=[]
    dx_lista=[]
    for x in np.arange(a,b,h):
        if m == 3:
            rezultat = three_step(func,x,h)
        else:
            rezultat = two_step(func,x,h)
        y = rezultat
        x_lista.append(x)
        dx_lista.append(y)
    return x_lista,dx_lista


def integracija(func,a,b,n):
    gornja = 0
    donja = 0
    h = (b-a)/n
    y = a
    x = a + h
    for i in range(n):
        gornja = gornja + func(x)*h
        donja = donja + func(y)*h
        x = x + h
        y = y + h
    return gornja,donja

def trapez(func, a, b, n):
    h = (b-a)/n
    suma = 0
    x = a
    for i in range(n):
        suma = suma + func(x)
        x = x + h
        trap = suma*h + ((func(b) + func(a))/2)*h
    return trap

