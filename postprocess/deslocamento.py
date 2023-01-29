import numpy as np
import matplotlib.pyplot as plt
import glob
from matplotlib import colors
from matplotlib.colors import Normalize
from scipy import ndimage
from matplotlib import animation


datas = glob.glob("/home/wsantos/Documentos/dados/gnu_output/*")
datas.sort()
data =  np.loadtxt("/home/wsantos/Documentos/dados/gnu_output/RES-003.dat",skiprows=1) 


plt.tight_layout()
img = [] 
frames = [] 
i = 0

list_of_datas = []


for file in datas:
    data =  np.loadtxt(file,skiprows=1)
    x,y = data[:,0],data[:,1] 
    den1, wall = data[:,3], data[:,7]
    den1 = den1.reshape((int(np.amax(x)),int(np.amax(y)))) # reshape da densidade para array
    wall = wall.reshape((int(np.amax(x)),int(np.amax(y))))# 
    den1 = np.transpose(den1)
    wall = np.transpose(wall)

    for i in range(len(den1)):
        for j in range(len(den1[1])):
            if den1[i,j]==0:
                den1[i,j]=4

    
    list_of_datas.append(wall+den1)

    i+=1
    
fig = plt.figure()
myimages = []

for i in list_of_datas:
    frame = i
    cmap = colors.ListedColormap(['#A3B7EC', '#D0021B','#BE7D42','#FFE19C'])
    bounds=[0.0,0.3, 0.35, 2.0, 4.0]
    norm = colors.BoundaryNorm(bounds, cmap.N)
    plt.title("Densidade 2")
    plt.axis('off')
    imgplot = plt.imshow(frame, interpolation='nearest', origin='lower',cmap=cmap, norm=norm)
    myimages.append([imgplot])

my_anim = animation.ArtistAnimation(fig, myimages, interval=True, blit=False, repeat=True)

f = '/home/wsantos/Documentos/dados/deslocamento.mp4'
writervideo = animation.FFMpegWriter(fps=6)
my_anim.save(f, writer=writervideo)