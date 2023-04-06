import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import glob
import matplotlib.pyplot as plt


# Escala característica

l = 0.000000174 #float(input('Lenght: '))
mu = 0.597#float(input('Dynamic Viscosity: '))
dx = 617e-7
dm = 2133-11 
dt = 308e-9 
dv = dx/dt


datas = glob.glob("/home/wsantos/documentos/dados/teste1/*")#cria uma lista com os nomes dos arquivos de dados
datas.sort()#organiza os nomes dos arquivos de dados


list_data = [] # lista


for file in datas: # para os arquivos dentro de datas
    data =  np.loadtxt(file,skiprows=1) # Lê cada um dos arquivos pulando a primeira linha
    x,y = data[:,0],data[:,1] # atribui a x e y os valores das duas primeiras colunas de dados
    velx, vely = data[:,4], data[:,5] # atribui os valores de velocidade às colunas 4 e 5
    press = data[:,6] # atribui os valores de pressão da coluna 6 à variável press
    
    
    velx = np.transpose(velx.reshape((int(np.amax(x)),int(np.amax(y))))) # faz um resize da coluna de velocidades na dimensão de x,y.
    x = np.transpose(x.reshape((int(np.amax(x)),int(np.amax(y))))) # faz um resize  
    y = np.transpose(y.reshape((int(np.amax(x)),int(np.amax(y)))))
    press = np.transpose(press.reshape(int(np.amax(x)), int(np.amax(y))))
    
    

    press1, press2 = press[:,0], press[:,-1]
    sumpress = sum(press1 - press2)
    sumvelx = sum(sum(velx))
    k = mu*sumvelx/sumpress
print(k*dx)               


plt.imshow(velx)

