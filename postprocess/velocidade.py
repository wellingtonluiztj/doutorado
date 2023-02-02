import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import glob
from matplotlib import animation
from matplotlib import colors



l = 0.000000174 #float(input('Lenght: '))
mu = 0.597#float(input('Dynamic Viscosity: '))
#====Convertion Factor====
dx = 617e-7
dm = 2133-11 
dt = 308e-9 
dv = dx/dt

datas = glob.glob("/home/wsantos/Documentos/dados/gnu_output/*")
datas.sort()

list_data = []

for file in datas:
    data =  np.loadtxt(file,skiprows=1)
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
    list_data.append((velx**2 + vely**2)**(1/2)) 




fig = plt.figure()
myimages = []
cmap = plt.colormaps['inferno']

for i in list_data:
    imgplot = plt.imshow(i, cmap=cmap, interpolation='nearest', origin='lower')
    plt.axis('off')
    myimages.append([imgplot])
plt.colorbar(plt.cm.ScalarMappable(cmap=cmap),
              orientation='vertical', label='Some Units')
my_anim = animation.ArtistAnimation(fig, myimages, interval=True, blit=False, repeat=True)

video = '/home/wsantos/Documentos/dados/velocidade.mp4'
writervideo = animation.FFMpegWriter(fps=6)
my_anim.save(video, writer=writervideo)

figura = '/home/wsantos/Documentos/dados/velocidade.png'