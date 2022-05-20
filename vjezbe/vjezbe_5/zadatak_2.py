import math
import matplotlib.pyplot as plt
import harmonic_oscillator 
from harmonic_oscillator import Harmonic_oscillator

h1 = Harmonic_oscillator()
h1.set_initial_conditions(2,15,10,5,0.1)
h1.oscillate(5)
h1.period(5)



h2 = Harmonic_oscillator()
h2.set_initial_conditions(2,15,10,5,0.01)#(m,k,x,v,dt)
h2.oscillate(5)
h2.period(5)


h3 = Harmonic_oscillator()
h3.set_initial_conditions(2,15,10,5,0.001)
h3.oscillate(5)
h3.period(5)



h1.analiticki_period()