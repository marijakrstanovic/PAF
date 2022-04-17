import math

from modul import Force



def f1(v,x,t):
    return 5

def f2(v,x,t):
    k = 3
    return -k*x

h1 = Force(0,0,0,0,f1)
h1.__init__(2,6,0,0.01,f1)
h1.move(5)
h1.plot_trajectory()


h2 = Force(0,0,0,0,f2)
h2.__init__(2,6,0,0.01,f2)
h2.move(5)
h2.plot_trajectory()
