import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import glob
from matplotlib import animation
from matplotlib import colors


font1 = {'family': 'serif',
        'color':  'black',
        'weight': 'bold',
        'size': 12
        }

def poiseulee():

    l = 0.000000174 #float(input('Lenght: '))
    mu = 0.597#float(input('Dynamic Viscosity: '))
    dx = 617e-7
    dm = 2133-11 
    dt = 308e-9 
    dv = dx/dt
    
    time = 100
    
    if time >= 0 and time < 10:
        datas = glob.glob("/gnu_output/RES-00" + str(time) +".dat")
    elif time >= 10 and time <= 99:
        datas = glob.glob("/gnu_output/RES-0" + str(time) + ".dat")
    else:
        datas = glob.glob("/gnu_output/RES-" + str(time) + ".dat")
        
        
    data =  np.loadtxt(datas[0],skiprows=1)
    x,y = data[:,0],data[:,1] 
    velx, vely = data[:,4], data[:,5]
    vel = (velx**2 + vely**2)**(1/2) 
    vel = vel.reshape(int(np.amax(x)), int(np.amax(y)))
    
    listmean = [ ]
    for i in range(len(vel)):
        avg = np.mean(vel[i])
        listmean.append(avg)
    velavg = np.array(listmean)
    
    X = list(range(0,75,1))
    X = np.array(X)
    
    fig = plt.figure()
    myimages = []
    
    figura = 'poiseuille.png'
    return(
    plt.plot(X, velavg*dv, 'o', alpha=0.4),
    plt.xlabel(fr'Posição $x(m/s)$', fontdict = font1),
    plt.ylabel(fr'Velocity $v(m/s)$', fontdict = font1),
    plt.savefig(figura, dpi = 300),
    plt.show()
    )