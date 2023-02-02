import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import glob
from matplotlib import animation
from matplotlib import colors


font = {'family': 'serif',
        'color':  'white',
        'weight': 'bold',
        'size': 7,
        }


l = 0.000000174 #float(input('Lenght: '))
mu = 0.597#float(input('Dynamic Viscosity: '))
dx = 617e-7
dm = 2133-11 
dt = 308e-9 
dv = dx/dt

datas = glob.glob("/home/wsantos/Documentos/dados/gnu_output/RES-100.dat")


data =  np.loadtxt(datas[0],skiprows=1)
x,y = data[:,0],data[:,1] 
velx, vely = data[:,4], data[:,5]
vel = (velx**2 + vely**2)**(1/2) 



fig = plt.figure()
myimages = []
cmap = plt.colormaps['inferno']


plt.scatter(x*dx, vel*dv, alpha=0.5)
plt.xlabel(fr'Posição $x(m/s)$', fontdict=font)
plt.ylabel(fr'Velocity $v(m/s)$', fontdict=font)
plt.show()
