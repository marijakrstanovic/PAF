import matplotlib
import math
import matplotlib.pyplot as plt
import calculus as cal

def f1(x):
    return 5*x**3 - 2*x**2 + 2*x -3

def f1_int(x):
    return (5/4)*(x**4) - (2/3)*(x**3) + x**2 - 3*x

dn = 100
nlista = []
glista = []
dlista = []
anlc = []
trap =  []

for i in range(1, 20):
    n = i*dn
    nlista.append(n)
    gornja, donja = cal.integracija(f1, 0, 10, n)
    c = f1_int(10) - f1_int(0)
    trapez = cal.trapez(f1, 0, 10, n)
    glista.append(gornja)
    dlista.append(donja)
    anlc.append(c)
    trap.append(trapez)

s = [5]
plt.scatter(nlista, glista, s, 'b') 
plt.scatter(nlista, dlista, s, 'r')
plt.scatter(nlista, trap, s, 'g')
plt.plot(nlista, anlc, 'orange')
plt.legend(["gornja međa","donja međa","trapez","analiticki"],loc = 'best')
plt.title("f(x) = 5x^3 - 2x^2 + 2x - 3")
plt.show()