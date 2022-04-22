import ProjectileDrop as pd
import matplotlib.pyplot as plt

ob = pd.ProjectileDrop(2000,200)
ob.padanje(0.01)
print("Vrijeme padanja iznosi {} s.".format(ob.t))

