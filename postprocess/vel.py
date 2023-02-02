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


#def velgraph(time)
dt = 308e-9 
time = 23



if time >=0 and time <10:
    datas = glob.glob("/home/wsantos/Documentos/dados/gnu_output/RES-00" + str(time) + ".dat")
elif time >=10 and time <99:
    datas = glob.glob("/home/wsantos/Documentos/dados/gnu_output/RES-0" + str(time) + ".dat")
else:
    datas = glob.glob("/home/wsantos/Documentos/dados/gnu_output/RES-" + str(time) + ".dat")


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
cmap = plt.colormaps['inferno']
plt.text( a-16, b-20,  rf'tempo = ${time*dt}\,s$', fontdict=font)
M = plt.imshow(vel,cmap = cmap, interpolation='nearest', origin='lower')
Q = plt.quiver(X, Y, velx, vely, scale=0.37, width=0.00127)
plt.axis('off')
plt.colorbar(plt.cm.ScalarMappable(cmap=cmap),
              orientation='vertical')
