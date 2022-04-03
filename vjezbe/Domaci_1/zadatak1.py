import particle as prt

p1 = prt.Particle()
p1.set_initial_conditions(20, 80, 0, 0)
print("Ukupno vrijeme gibanja je {} s.".format(p1.total_time()))
p1.max_speed()
p1.reset()

p1.velocity_to_hit_target(40, 50, 10, 0.1)
p1.reset() 

p1.angle_to_hit_target(40, 50, 10, 0.1)
p1.reset() 