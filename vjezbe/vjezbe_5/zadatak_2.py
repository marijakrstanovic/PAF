import math
import matplotlib.pyplot as plt
import harmonic_oscillator 
from harmonic_oscillator import Harmonic_oscillator

h1 = Harmonic_oscillator()
h1.set_initial_conditions(2,10,5,0.01)
h1.oscillate(5)
h1.period(5)
h1.reset()


h2 = Harmonic_oscillator()
h2.set_initial_conditions(2,10,5,0.001)
h2.oscillate(5)
h2.period(5)
h2.reset()

h3 = Harmonic_oscillator()
h3.set_initial_conditions(2,10,5,0.0001)
h3.oscillate(5)
h3.period(5)
h3.reset()


h1.analiticki_period()