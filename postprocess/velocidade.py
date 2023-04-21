import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import glob
from matplotlib import animation
from matplotlib import colors


def velanim(pasta):
    dx = 26e-6
    dm = 1.5e-11 
    dt = 8e-6
    dv = dx/dt
    
    
    datas = glob.glob("/home/wsantos/documentos/dados/quali/reduzido/placas paralelas/0.00/" + str(pasta) +"/*")
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
    
    
    norma = mpl.colors.Normalize(vmin=0, vmax=0.20) #np.max(list_data)*dv
    fig = plt.figure()
    myimages = []

    
    for i in list_data:
        imgplot = plt.imshow(i, cmap='plasma', interpolation='nearest', origin='lower')
        plt.axis('off')
        myimages.append([imgplot])
        
        
    plt.colorbar(plt.cm.ScalarMappable(cmap='plasma', norm = norma),
                  orientation='vertical')
    my_anim = animation.ArtistAnimation(fig, myimages, interval=True, blit=False, repeat=True)
    
    video = '/home/wsantos/documentos/dados/quali/reduzido/placas paralelas/0.00/velocity.mp4'
    writervideo = animation.FFMpegWriter(fps=6)

    
    figura = '/home/wsantos/documentos/dados/quali/reduzido/placas paralelas/0.00/velocity.png'
    
    return(
        plt.savefig(figura, dpi = 300),
        my_anim.save(video, writer=writervideo)    
        ) 


velanim('gnu_output')