import numpy as np
import matplotlib.pyplot as plt
import glob
from matplotlib import colors
from matplotlib import animation
import pandas as pd

datas = glob.glob("/home/wsantos/documentos/dados/quali/reduzido/placas paralelas/0.00/deslocamento/gnu_output/*")
datas.sort()
data =  np.loadtxt("/home/wsantos/documentos/dados/quali/reduzido/placas paralelas/0.00/deslocamento/gnu_output/RES-003.dat",skiprows=1) 


plt.tight_layout()
img = [] 
frames = [] 
i = 0

list_of_datas = []


for file in datas:
    data =  np.loadtxt(file,skiprows=1)
    x,y = data[:,0],data[:,1] 
    den, wall = data[:,3], data[:,7]
    den = den.reshape((int(np.amax(x)),int(np.amax(y)))) # reshape da densidade para array
    wall = wall.reshape((int(np.amax(x)),int(np.amax(y))))# 
    den = np.transpose(den)
    wall = np.transpose(wall)

    for i in range(len(den)):
        for j in range(len(den[1])):
            if den[i,j]==0:
                den[i,j]=4

    
    list_of_datas.append(wall+den)

    i+=1
    
fig = plt.figure()
myimages = []

for i in list_of_datas:
    frame = i
    cmap = colors.ListedColormap(['#A3B7EC', '#D0021B','#BE7D42','#FFE19C'])
    bounds=[0.0,0.3, 0.35, 2.0, 4.0]
    norm = colors.BoundaryNorm(bounds, cmap.N)
    plt.axis('off')
    imgplot = plt.imshow(frame, interpolation='nearest', origin='lower',cmap=cmap, norm=norm)
    myimages.append([imgplot])

my_anim = animation.ArtistAnimation(fig, myimages, interval=True, blit=False, repeat=True)

f = '/home/wsantos/documentos/dados/quali/reduzido/placas paralelas/0.05/deslocamento/teste1.mp4'
writervideo = animation.FFMpegWriter(fps=6)
my_anim.save(f, writer=writervideo)


#%%

def plotrec(dt, pasta1,pasta2):
        
    font = {'family': 'serif',
            'color':  'black',
            'weight': 'bold',
            'size': 11,
            }
    font2 = {'family': 'serif',
            'color':  'grey',
            'weight': 'normal',
            'size': 8,
            }
    
# High Salinity
    
    time = []
    
    data = glob.glob("/home/wsantos/documentos/dados/quali/reduzido/placas paralelas/0.00/" + str(pasta1) + "/*") # Lista os pathnames terminados em dat
    data.sort() # Organiza os nomes dos caminhos
    list_data = []
    frac = []    
    j = 0
    bt = []
    for file in data:
        dat = np.loadtxt(file, skiprows=1, usecols=[0,1,2,3]) #lê a lista data com os arquivos txt pulando linha do cabeçalho
        den = dat[:, [0,1,2,3]] # cria uma variável com colunas de dat
        df = pd.DataFrame(den) # tranforma em um DataFrame
        df.columns = ["X", "Y", "Den1", "Den2"] # nomea as colunas do DataFrame
        wall_max = df.iloc[ df[ (df["Den1"] == 0) & (df["Den2"] == 0) ].index[-1], 0] # identifica o limite de parede 
        df.drop(df[df["X"] > wall_max].index, inplace = True) # remove todos os valores maiores que wall
        df.drop(df[df["Den1"] == 0].index, inplace = True) # identifica os índices de df com Den1 = 0 e os remove as linhas
        df.drop(df[df["Den2"] == 0].index, inplace = True)  # identifica os índices de df com Den2 = 0 e os remove as linhas
        df["Den"] = df.values[:,3] - df.values[:,2] # Cria uma coluna Den em df cujo valor é a diferença da coluna 3 pela coluna 2 de df
        
        df.loc[df.loc[:, "Den"] < 0, "Den"] = 0 # salmoura - na coluna Den, identifica as linhas cujos valores são negativos e iguala a zero
        df.loc[df.loc[:, "Den"] > 0, "Den"] = 1 # petróleo - na coluna Den, identifica as linhas cujos valores são positivos e iguala a um
        
        counts = df["Den"].value_counts() # Conta quando de cada valor tem na coluna Den (quantos uns e quantos zeros)
        # Aqui surge um erro pois counts deixa de ter duas linhas no final
        if len(counts) == 2:
            oil = float(counts[1])
            list_data.append(oil)
            fracoil = 100*(1-(list_data[j]/list_data[0]))
            frac.append(fracoil)
            time.append(j*dt)
            j += 1
        else:
            bt.append(j)
            oil = 0
            list_data.append(oil)
            fracoil = 100*(1-(list_data[j]/list_data[0]))
            frac.append(fracoil)
            time.append(j*dt)
            j += 1
            
# Low salinity

    
    time = []
    
    data2 = glob.glob("/home/wsantos/documentos/dados/quali/reduzido/placas paralelas/0.00/" + str(pasta2) + "/*") # Lista os pathnames terminados em dat
    data2.sort() # Organiza os nomes dos caminhos
    list_data2 = []
    frac2 = []    
    j2 = 0
    bt2 = []
    for file in data2:
        dat2 = np.loadtxt(file, skiprows=1, usecols=[0,1,2,3]) #lê a lista data com os arquivos txt pulando linha do cabeçalho
        den2 = dat2[:, [0,1,2,3]] # cria uma variável com colunas de dat
        df2 = pd.DataFrame(den2) # tranforma em um DataFrame
        df2.columns = ["X", "Y", "Den1", "Den2"] # nomea as colunas do DataFrame
        wall_max2 = df2.iloc[ df2[ (df2["Den1"] == 0) & (df2["Den2"] == 0) ].index[-1], 0] # identifica o limite de parede 
        df2.drop(df2[df2["X"] > wall_max2].index, inplace = True) # remove todos os valores maiores que wall
        df2.drop(df2[df2["Den1"] == 0].index, inplace = True) # identifica os índices de df com Den1 = 0 e os remove as linhas
        df2.drop(df2[df2["Den2"] == 0].index, inplace = True)  # identifica os índices de df com Den2 = 0 e os remove as linhas
        df2["Den"] = df2.values[:,3] - df2.values[:,2] # Cria uma coluna Den em df cujo valor é a diferença da coluna 3 pela coluna 2 de df
        
        df2.loc[df2.loc[:, "Den"] < 0, "Den"] = 0 # salmoura - na coluna Den, identifica as linhas cujos valores são negativos e iguala a zero
        df2.loc[df2.loc[:, "Den"] > 0, "Den"] = 1 # petróleo - na coluna Den, identifica as linhas cujos valores são positivos e iguala a um
        
        counts2 = df2["Den"].value_counts() # Conta quando de cada valor tem na coluna Den (quantos uns e quantos zeros)
        # Aqui surge um erro pois counts deixa de ter duas linhas no final
        if len(counts2) == 2:
            oil2 = float(counts2[1])
            list_data2.append(oil2)
            fracoil2 = 100*(1-(list_data2[j2]/list_data2[0]))
            frac2.append(fracoil2)
            
            time.append(j2*dt)
            j2 += 1
        else:
            bt2.append(j2)
            oil2 = 0
            list_data2.append(oil2)
            fracoil2 = 100*(1-(list_data2[j2]/list_data2[0]))
            
            frac2.append(fracoil2)
            time.append(j2*dt)
            j2 += 1
    
    
    f = '/home/wsantos/documentos/dados/quali/reduzido/placas paralelas/0.00/'
          
    return (
    plt.ylabel(rf'Oil Extraction($\%$ oil displaced)',fontdict = font),
    plt.xlabel(rf'Time(s)', fontdict = font2),
    plt.plot(time,frac,'b',label = 'High Slinity (100620 ppm)',linewidth=1),
    plt.plot(time,frac2,'r',label = 'Low Slinity (29250 ppm)',linewidth=1),
    plt.axvline(x = bt[0]*dt, color = 'y', label = 'breakthrough',linestyle='dashed',
     linewidth=1, markersize=10),
    plt.text( 1.11*dt*bt[0], 70,  rf'${round(dt*bt[0],5)} s$', fontdict=font2),
    plt.legend(loc = "lower right"),
    plt.savefig(str(f) + "reicoveryfactor.png",dpi=300),
    plt.show()
    
    )
        
    
plotrec(dt =  5.23e-06, pasta1 = 'high', pasta2 = 'low')