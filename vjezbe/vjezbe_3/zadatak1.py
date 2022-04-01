import particle as prt 

p1 = prt.Particle()
p1.set_initial_conditions(25, 60, 0, 0)
p1.range(0.01)
p1.plot_trajectory()
p1.reset()

p1.set_initial_conditions(10, 60, 0, 0)
p1.range(0.01)
p1.plot_trajectory()
p1.reset()  


