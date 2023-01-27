import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
import glob
from matplotlib.colors import Normalize
from scipy import ndimage

font = {'family': 'serif',
        'color':  'white',
        'weight': 'normal',
        'size': 8,
        }

class Bubble:
    def __init__(self, cross, plus, timestep = 100, dt = 0.000089):
        self.cross = cross
        self.plus = plus
        self.timestep = timestep
    def angcont(self, cross, plus, timestep = 100, dt = 0.000089):
        '''
        Medida o ângulo de contato da Gota de óleo circundada com água.
    cross: eixo da esquerda    
    plus: eixo da direita
    timestep: tempo de simulação [0,100]
    
    returns:
    theta: ângulo de contato
        '''
        
        datas = glob.glob("gnu_output/*")
        datas.sort()
        if timestep >= 0 and timestep < 10:
            number = 'gnu_output/RES-00'+ str(timestep) + '.dat'
        elif timestep >= 10 and timestep <= 99:
            number = 'gnu_output/RES-0'+ str(timestep) + '.dat'
        else:
            number = 'gnu_output/RES-'+ str(timestep) + '.dat'
        data =  np.loadtxt(number,skiprows=1) 
        x,y = data[:,0],data[:,1]
        
        den1, wall = data[:,3], data[:,7]
        
        den1 = den1.reshape((int(np.amax(x)),int(np.amax(y)))) 
        wall = wall.reshape((int(np.amax(x)),int(np.amax(y))))# 
        den1 = np.transpose(den1)
        wall = np.transpose(wall)
        
        for i in range(len(den1)):
            for j in range(len(den1[1])):
                if den1[i,j]==0:
                    den1[i,j]=4
            
        meiox = int(np.shape(den1)[0]/2)
        
        plt.figure()
         
        h = (cross+plus) - cross
        w = np.shape(den1)[0]
        R_m = (h**2 + (w/2)**2)/(2*h)
        theta = np.arcsin((w/2)/R_m)
        PI=3.14
        theta = theta*(180/PI)
        theta = 90 - theta
        cmap = colors.ListedColormap(['#A3B7EC', '#D0021B','#BE7D42','#FFE19C'])
        bounds=[0.0,0.3, 0.5, 2.0, 4.0]
        norm = colors.BoundaryNorm(bounds, cmap.N)
        
        
        return (plt.title(rf"$\theta$ = {round(theta, 2)}"),
        plt.axis('off'),
        plt.hlines(y=meiox, xmin=cross, xmax=cross+plus, color='r'),
        plt.vlines(x=cross, ymin=0.0, ymax=np.shape(den1)[0], color='r'),
        plt.text(cross + plus/2, w/2 + 4, r'$h$', fontdict=font),
        plt.text(cross -10 , w - 10, r'$w$', fontdict=font),
        plt.text(10 , 10, rf'$tempo = {dt*timestep} s$', fontdict=font),
        plt.vlines(x=cross+plus, ymin=0.0, ymax=np.shape(den1)[0], color='r'),
        plt.imshow(den1, interpolation='nearest', origin='lower',cmap=cmap, norm=norm),
        theta
        )
    