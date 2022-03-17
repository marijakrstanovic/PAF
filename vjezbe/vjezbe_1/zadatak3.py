import numpy as np
import matplotlib as plt
import math

x1=float(input("unesi x1: "))
y1=float(input("unesi y1: "))
x2=float(input("unesi x2: "))
y2=float(input("unesi y2: "))

if x2!=x1:
    k=(y2-y1)/(x2-x1)
    l=(y1-k*x1)
    print("y={}x+{}".format(k,l))
else:
    x1=float(input("unesi x1: "))
    y1=float(input("unesi y1: "))
    x2=float(input("unesi x2: "))
    y2=float(input("unesi y2: "))

    k=(y2-y1/x2-x1)
    l=(y1-k*x1)
    print("y={}x+{}".format(k,l))


