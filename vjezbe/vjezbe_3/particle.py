class Particle:
    def __init__(self ,mass, x_0):
        self.mass = mass
        self.x_0 = x_0

    def printInfo(self):
        print("cestica ima masu {} i u pocetnom trenutku nalazi se na polozaju {}".format(self.mass, self.x_0))

p1 = Particle(10 , -5)
p1.printInfo()
