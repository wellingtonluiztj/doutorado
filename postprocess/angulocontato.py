import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
import glob
from matplotlib.colors import Normalize
from scipy import ndimage
from matplotlib import animation

font = {'family': 'serif',
        'color':  'white',
        'weight': 'normal',
        'size': 8,
        }

class Bubble:
    '''
    Medida o ângulo de contato da Gota de óleo circundada com água.
    parameters:
    cross: eixo da esquerda    
    plus: eixo da direita
    pasta: nome da pasta de arquivos
    timestep: tempo de simulação [0,100]
    '''
    
    
    def __init__(self, timestep = 100, dt = 0.000089):
        self.timestep = timestep
        self.dt = dt
    def angcont(self, cross, plus, pasta, timestep = 100, dt = 0.000089):
        '''
        Medida o ângulo de contato da Gota de óleo circundada com água.
        parameters:
        cross: eixo da esquerda    
        plus: eixo da direita
        pasta: nome da pasta de arquivos
        timestep: tempo de simulação [0,100]
    
        returns:
        theta: ângulo de contato
        '''
        

        datas = glob.glob("/home/wsantos/Documentos/dados" + str(pasta) + "/*")
        datas.sort()
        if self.timestep >= 0 and self.timestep < 10:
            number = '/home/wsantos/Documentos/dados/teste1/RES-00'+ str(self.timestep) + '.dat'
        elif self.timestep >= 10 and self.timestep <= 99:
            number = '/home/wsantos/Documentos/dados/teste1/RES-0'+ str(self.timestep) + '.dat'
        else:
            number = '/home/wsantos/Documentos/dados/teste1/RES-'+ str(self.timestep) + '.dat'
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
        plt.text(10 , 10, rf'$tempo = {self.dt*self.timestep} s$', fontdict=font),
        plt.vlines(x=cross+plus, ymin=0.0, ymax=np.shape(den1)[0], color='r'),
        plt.imshow(den1, interpolation='nearest', origin='lower',cmap=cmap, norm=norm),
        theta
        )
        
    def anganim(self, g, pasta, timestep = 100, dt = 0.000089):
        
        datas = glob.glob("/home/wsantos/Documentos/dados" + str(pasta) + "/*")
        datas.sort()
       
        plt.tight_layout()
        
        img = [] # some array of images
        frames = [] # for storing the generated images
        i = 0
        
        list_of_datas = []
        for file in datas:
            
            data =  np.loadtxt(file,skiprows=1)
        
            x,y = data[:,0],data[:,1]
        
            den1, wall = data[:,3], data[:,7]

        
            den1 = den1.reshape((int(np.amax(x)),int(np.amax(y))))
            
            wall = wall.reshape((int(np.amax(x)),int(np.amax(y))))
        
        
            for i in range(len(den1)):
                for j in range(len(den1[1])):
                    if den1[i,j]==0:
                        den1[i,j]=4
            den1 = np.transpose(den1)
            wall = np.transpose(wall)
            list_of_datas.append(wall + den1) # adiciona quem virará vídeo
        
            i+=1
            
        fig = plt.figure()
        myimages = []
        
        for i in list_of_datas:
            frame = i
            cmap = colors.ListedColormap(['#A3B7EC', '#D0021B','#BE7D42','#FFE19C'])
            bounds=[0.0,0.3, 0.5, 2.0, 4.0]
            norm = colors.BoundaryNorm(bounds, cmap.N)
            plt.title(rf'$g^R_o$ = {g}')
            plt.text(10 , 10, rf'$tempo = {dt*timestep} s$', fontdict=font),
            plt.axis('off')
            imgplot = plt.imshow(frame, interpolation='nearest', origin='lower',cmap=cmap, norm=norm)
            myimages.append([imgplot])
        
        #plt.colorbar()
        
        #interval -> tanto faz
        my_anim = animation.ArtistAnimation(fig, myimages, interval=True, blit=False, repeat=True)
        
        savevideo = 'angulo' + str(g) + '.mp4'
        f = savevideo
        writervideo = animation.FFMpegWriter(fps=6)
        cmap = colors.ListedColormap(['#A3B7EC', '#D0021B','#BE7D42','#FFE19C'])
        bounds=[0.0,0.3, 0.5, 2.0, 4.0]
        norm = colors.BoundaryNorm(bounds, cmap.N)
        return (my_anim.save(f, writer=writervideo),
                plt.imshow(list_of_datas[-1],interpolation='nearest', origin='lower',cmap=cmap, norm=norm),
                plt.title(rf'$g^R_o$ = {g}'),
                plt.axis('off'),
                plt.savefig('angulo.png')
                )