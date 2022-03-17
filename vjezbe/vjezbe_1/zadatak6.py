import math
import matplotlib.pyplot as plt
import numpy

def kruznica():
    x=int(input("unesite x: ")) #xkoordinata tocke
    y=int(input('unesi y: ')) #ykoordinata tocke
    a=int(input('unesi a: ')) #xkoordinata sredista
    b=int(input('unesi b: ')) #ykoordinata sredista
    r=int(input('unesi r: ')) #radijus kruznice
    udaljenost= math.sqrt((a-x)**2+(b-y)**2) #od sredista kruznice
    udaljena=math.sqrt((a-x)**2+(b-y)**2)-r #od kruznice

    if udaljenost < r:
        print('Unutar kruznice,udaljena {} '.format(abs(udaljena)))
    elif udaljenost == r:
        print('Tocka je na kruznici!')
    else:
        print('udaljena od kruznice na udaljenosti {}'.format(udaljena))

    slika = plt.Circle((x,y),r)
    fig,ax=plt.subplots()
    ax.add_patch(slika)
    ax.set_aspect("equal",adjustable = "datalim")
    ax.plot(a,b,"r*")
    ax.plot

    prikaz = input('P-prikaz,S-spremit:  ')
    if prikaz == 'P':
        plt.show()
    elif prikaz == "S":
        slika=input('ime slike: ')
        plt.savefig(slika)
    else:
        print('Krivi odabir')

kruznica()
