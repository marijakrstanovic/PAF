import particle as prt
import math
import matplotlib.pyplot as plt

p1=prt.Particle()
kut_lista = []
domet = []
vrijeme_trajanja = []

for kut in range(180):
    p1.set_initial_conditions(20,kut,0,0)
    dx = p1.range(0.01)
    t = p1.total_time()
    kut_lista.append(kut)
    domet.append(dx)
    vrijeme_trajanja.append(t)

figure,axes = plt.subplots(1,2,figsize=(14,4))

axes[0].plot(kut_lista,domet)
axes[0].set_title("GRAF")
axes[0].set(xlabel="radiani",ylabel="metar(m)")
axes[1].plot(kut_lista,vrijeme_trajanja)
axes[1].set_title("GRAF")
axes[1].set(xlabel="radiani",ylabel="sekunda(s)")

plt.show()

