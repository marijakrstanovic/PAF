import particle 
import math
import matplotlib.pyplot as plt

def graf_pogreske():
    p1 = particle.Particle()
    p1.set_initial_conditions(10,60,0,0)
    dt = []
    re_pogreska = []

    for i in range(100):
        p1.set_initial_conditions(10,60,0,0)
        dt_i = i*0.001+0.001
        dt.append(dt_i)
        D_A = (10**2)*math.sin(math.radians(60))/9.81
        D_N =p1.range(dt_i)
        error = ((abs(D_A-D_N))/D_A)*100
        re_pogreska.append(error)


    plt.plot(dt,re_pogreska , 'b')
    plt.xlabel("dt [s]")
    plt.ylabel("absolute relative error [%]")
    plt.title("Relativna pogreska")
    plt.show()

graf_pogreske()