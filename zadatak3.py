import numpy as np
import matplotlib as plt
import math

x1=int(input("unesi x1: "))
y1=int(input("unesi y1: "))
x2=int(input("unesi x2: "))
y2=int(input("unesi y2: "))

if x2!=x1:
    k=round(y2-y1/x2-x1)
    l=round(y1-k*x1)
    print("y={}x+{}".format(k,l))
else:
    x1=int(input("unesi x1: "))
    y1=int(input("unesi y1: "))
    x2=int(input("unesi x2: "))
    y2=int(input("unesi y2: "))

    k=round(y2-y1/x2-x1)
    l=round(y1-k*x1)
    print("y={}x+{}".format(k,l))


