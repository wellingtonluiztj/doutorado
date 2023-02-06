import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
import glob
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

    
    def __init__(self, timestep = 100, dt = 11e-6):
        self.timestep = timestep
        self.dt = dt
    def angcont(self, plus, pasta, timestep = 100, dt = 11e-6):
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
        

        datas = glob.glob("/home/wsantos/Documentos/dados/angulo-contato/" + str(pasta) + "/*")
        datas.sort()
        if self.timestep >= 0 and self.timestep < 10:
            number = '/home/wsantos/Documentos/dados/angulo-contato/' + str(pasta) + 'RES-00'+ str(self.timestep) + '.dat'
        elif self.timestep >= 10 and self.timestep <= 99:
            number = '/home/wsantos/Documentos/dados/angulo-contato/' + str(pasta) + '/RES-0'+ str(self.timestep) + '.dat'
        else:
            number = '/home/wsantos/Documentos/dados/angulo-contato/' + str(pasta) + '/RES-'+ str(self.timestep) + '.dat'
        data =  np.loadtxt(number,skiprows=1) 
        x,y = data[:,0],data[:,1]
        
        den, wall = data[:,3], data[:,7]
        
        den = den.reshape((int(np.amax(x)),int(np.amax(y)))) 
        wall = wall.reshape((int(np.amax(x)),int(np.amax(y))))# 
        den = np.transpose(den)
        wall = np.transpose(wall)
        
        for i in range(len(den)):
            for j in range(len(den[1])):
                if den[i,j]==0:
                    den[i,j]=4
            
        meiox = int(np.shape(den)[0]/2)
        cross = int(np.shape(den)[1]/2)
        
        plt.figure()
         
        h = (cross+plus) - cross
        w = np.shape(den)[0]
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
        plt.vlines(x=cross, ymin=0.0, ymax=np.shape(den)[0], color='r'),
        plt.text(cross + plus/2, w/2 + 4, r'$h$', fontdict=font),
        plt.text(cross -10 , w - 10, r'$w$', fontdict=font),
        plt.text(10 , 10, rf'$tempo = {self.dt*self.timestep} s$', fontdict=font),
        plt.vlines(x=cross+plus, ymin=0.0, ymax=np.shape(den)[0], color='r'),
        plt.imshow(den, interpolation='nearest', origin='lower',cmap=cmap, norm=norm),
        theta
        )
        
    def anganim(self, g, pasta, timestep = 100, dt = 11e-6):
        '''
        Animação em vídeo Gota de óleo circundada com água.
        parameters:
        g: força de interfaces    
        pasta: nome da pasta de arquivos da simulação
        timestep: tempo de simulação [0,100]
        dt: intervalo de tempo da escala característica
    
        returns:
        theta: ângulo de contato
        '''
        
        datas = glob.glob("/home/wsantos/Documentos/dados/angulo-contato/" + str(pasta) + "/*")
        datas.sort()
       
        plt.tight_layout()
        
        img = []
        frames = [] 
        i = 0
        
        list_of_datas = []
        for file in datas:
            
            data =  np.loadtxt(file,skiprows=1)
        
            x,y = data[:,0],data[:,1]
        
            den, wall = data[:,3], data[:,7]

        
            den = den.reshape((int(np.amax(x)),int(np.amax(y))))
            
            wall = wall.reshape((int(np.amax(x)),int(np.amax(y))))
        
        
            for i in range(len(den)):
                for j in range(len(den[1])):
                    if den[i,j]==0:
                        den[i,j]=4
            den = np.transpose(den)
            wall = np.transpose(wall)
            list_of_datas.append(wall + den) # adiciona quem virará vídeo
        
            i+=1
            
        fig = plt.figure()
        myimages = []

        for i in list_of_datas:
            frame = i
            cmap = colors.ListedColormap(['#A3B7EC', '#D0021B','#BE7D42','#FFE19C'])
            bounds=[0.0,0.3, 0.5, 2.0, 4.0]
            norm = colors.BoundaryNorm(bounds, cmap.N)
            plt.title(rf'$g^R_o$ = {g}')
            plt.text(10 , 5, rf'$tempo = {self.dt*self.timestep} s$', fontdict=font),
            plt.axis('off')
            imgplot = plt.imshow(frame, interpolation='nearest', origin='lower',cmap=cmap, norm=norm)
            myimages.append([imgplot])
        
        #plt.colorbar()
        
        #interval -> tanto faz
        my_anim = animation.ArtistAnimation(fig, myimages, interval=True, blit=False, repeat=True)
        
        savevideo = 'angulo' + str(g) + '.mp4'
        savefigure = 'angulo' + str(g) + '.png'
        writervideo = animation.FFMpegWriter(fps=6)
        cmap = colors.ListedColormap(['#A3B7EC', '#D0021B','#BE7D42','#FFE19C'])
        bounds=[0.0,0.3, 0.5, 2.0, 4.0]
        norm = colors.BoundaryNorm(bounds, cmap.N)
        return (my_anim.save('/home/wsantos/Documentos/dados/angulo-contato/' + savevideo, writer=writervideo),
                plt.imshow(list_of_datas[-1],interpolation='nearest', origin='lower',cmap=cmap, norm=norm),
                plt.title(rf'$g^R_o$ = {g}'),
                plt.axis('off'),
                plt.savefig('/home/wsantos/Documentos/dados/angulo-contato/' + savefigure, dpi = 300)
                )