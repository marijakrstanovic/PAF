import matplotlib.pyplot as plt
import os
import numpy as np

def pravac(x1,x2,y1,y2):
    
    xkoordinate=[x1,x2]
    ykoordinate=[y1,y2]

    k=((y2-y1)/(x2-x1))
    if x1<x2:
        x=np.linspace(x1-2,x2+2,1000)
    else:
        x=np.linespace(x1+2,x2-2,1000)
    y=k*(x-x1)+y1
    
    graf=input("naslova grafa: ")

    a=[i for i in xkoordinate]
    b=[i for i in ykoordinate]
    fig=plt.figure(figsize=(6,4), dpi=200)
    ax=fig.add_axes([0.2, 0.2, 0.6, 0.6])
    ax.plot(a,b,'r*')
    ax.plot(x,y,'b')
    ax.set_xlabel('os-x')
    ax.set_ylabel('os-y')
    ax.set_title(graf)

    
    nacin_prikaza=input('O za prikaz na ekranu,P za prokaz u PDFu')
    if nacin_prikaza == 'O':
        prikaz = plt.show()
    elif nacin_prikaza=='P':
        izaberi_ime=input('Ime koje zelis dati svom grafu je: ')
        prikaz = fig.savefig(os.path.join('{}.pdf'.format(izaberi_ime)))
    else:
        print('Kriv odabir')

    return nacin_prikaza

pravac(2.5,3,2.5,3)