import ProjectileDrop as pd

ob = pd.ProjectileDrop(50,60)

ob.promjena_visine(40)
ob.promjena_brzine(40)

print("Nova pocetna visina je {} m,a nova pocetna visina  je {} m\s.".format(ob.h,ob.vx))