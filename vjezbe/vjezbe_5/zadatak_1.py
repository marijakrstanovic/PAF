import math
import matplotlib.pyplot as plt
from harmonic_oscillator import Harmonic_oscillator

h1=Harmonic_oscillator()
h1.set_initial_conditions(2,10,5,0.01)
h1.oscillate(5)
h1.graf()


plt.clf()

h1.set_initial_conditions(2,10,5,0.01)
h1.oscillate(5)
plt.scatter(h1.t,h1.x,s = 2,c="r", label="dt=0.01")


h1.set_initial_conditions(2,10,0,5,0.1)
h1.oscillate(5)
plt.scatter(h1.t,h1.x, s = 2, c = "b", label = "dt = 0.1")


h1.set_initial_conditions(2,10,0,5,0.05)
h1.oscillate(5)
plt.scatter(h1.t,h1.x, s = 2, c = "g", label = "dt = 0.05")


plt.xlabel("t [s]")
plt.ylabel("x [m]")
plt.title("PRECIZNOST")
plt.legend(loc = "lower right")
plt.show()