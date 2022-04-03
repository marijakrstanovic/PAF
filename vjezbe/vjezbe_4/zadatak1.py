import math
import matplotlib.pyplot as plt
import numpy as np
import calculus as cal


def f(x):
    return x**3

def f_der(x):
    return 3*x**2

def f1(x):
    return math.sin(x)

def f1_der(x):
    return math.cos(x)


lista1,lista2=cal.derivacija(f,-5,5,0.01,2)
lista3,lista4=cal.derivacija(f,-5,5,0.1,2)
list1,list2=cal.derivacija(f1,-5,5,0.01,2)
list3,list4=cal.derivacija(f1,-5,5,0.1,2)

lista = []
for x in lista1:
    y = f_der(x)
    lista.append(y)


list= []
for x in list1:
    y = f1_der(x)
    list.append(y)

s=[2]
plt.scatter(lista1,lista2,s,"r")
plt.scatter(lista3,lista4,s,"b")
plt.plot(lista1,lista,'g')
plt.legend(["dt=0.01","dt=0.1","analiticki"],loc = 'best')
plt.title("f(x)=x**3")
plt.show()

plt.clf()

plt.scatter(list1, list2, s, 'r')
plt.scatter(list3, list4, s, 'b')
plt.plot(lista1,list,'g')
plt.legend(["dt=0.01","dt=0.1","analitiski"],loc = 'best')
plt.title("f(x) = sin(x)")
plt.show()