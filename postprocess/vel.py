import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import glob
from matplotlib import animation
from matplotlib import colors
import matplotlib as mpl

font = {'family': 'serif',
        'color':  'white',
        'weight': 'bold',
        'size': 7,
        }


#def velgraph(time)
dt = 308e-9
dx = 617e-7
dm = 2133-11 
dv = dx/dt


time = 100


def velfield(time):
    if time >=0 and time <10:
        datas = glob.glob("/home/wsantos/documentos/dados/teste1/RES-00" + str(time) + ".dat")
    elif time >=10 and time <99:
        datas = glob.glob("/home/wsantos/documentos/dados/teste1/RES-0" + str(time) + ".dat")
    else:
        datas = glob.glob("/home/wsantos/documentos/dados/teste1/RES-" + str(time) + ".dat")
    
    
    data =  np.loadtxt(datas[0],skiprows=1)
    x,y = data[:,0],data[:,1] 
    velx, vely = data[:,4], data[:,5]
    
    velx = velx.reshape((int(np.amax(x)),int(np.amax(y)))) 
    vely = vely.reshape((int(np.amax(x)),int(np.amax(y))))
    x = x.reshape((int(np.amax(x)),int(np.amax(y)))) 
    y = y.reshape((int(np.amax(x)),int(np.amax(y))))
    
    velx = np.transpose(velx)
    vely = np.transpose(vely)
    x = np.transpose(x)
    y = np.transpose(y)
    vel = (velx**2 + vely**2)**(1/2) 
    
    a = np.shape(vel)[0]
    b = np.shape(vel[1])[0]
    
    X, Y = np.meshgrid(np.arange(0,b, 1), np.arange(0,a,1))
    
    M = plt.imshow(vel,cmap = 'inferno', interpolation='nearest', origin='lower')
    Q = plt.quiver(X, Y, velx, vely, scale=0.27, width=0.0012)
    norm = mpl.colors.Normalize(vmin=0, vmax= np.max(vel*dv))
    return (
        plt.text( a-16, b-20,  rf'tempo = ${time*dt}\,s$', fontdict=font),
    plt.axis('off'),
    plt.colorbar(mpl.cm.ScalarMappable(cmap='inferno', norm = norm),
                  orientation='vertical')
)

velfield(time = 40)