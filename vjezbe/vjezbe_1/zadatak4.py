import math
import matplotlib as plt
import numpy

def pravac(x1,x2,y1,y2):
    if x2!=x1:
        k=((y2-y1)/(x2-x1))
        l=(y1-k*x1)
        print("y={}x+{}".format(k,l))
    else:
        k=((y2-y1)/(x2-x1))
        l=(y1-k*x1)
        print("y={}x+{}".format(k,l))
pravac(2.5,3,2.5,3)