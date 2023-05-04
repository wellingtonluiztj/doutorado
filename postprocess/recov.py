import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import glob
from tqdm import tqdm



dt =  1.110e-08
pasta1 = '0.00'
pasta2 = '0.05'
pasta3 = '1.72' 
    

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

'''
Concentração de Na igual a 0.00
'''
time = []
data = glob.glob( str(pasta1) + "/gnu_output/*.dat") # Lista os pathnames terminados em dat
data.sort() # Organiza os nomes dos caminhos
list_data = []
frac = []    
j = 0
bt1 = []


for file in tqdm(data):
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
        fracoil = 100*(1-(list_data[j]/sum(counts)))
        frac.append(fracoil)

        j += 1
    else:
        bt1.append(j)
        oil = 0
        list_data.append(oil)
        fracoil = 100*(1-(list_data[j]/sum(counts)))
        frac.append(fracoil)
 
        j += 1
        
      

'''
Concentração de Na igual a 0.05
'''
data2 = glob.glob( str(pasta2) + "/gnu_output/*.dat") # Lista os pathnames terminados em dat
frac2 = []    
bt2 = []
list_data2 = []
j = 0
for file2 in tqdm(data2):
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
        fracoil2 = 100*(1-(list_data2[j]/sum(counts2)))
        frac2.append(fracoil2)

        j += 1
    else:
        bt2.append(j)
        oil2 = 0
        list_data2.append(oil2)
        fracoil2 = 100*(1-(list_data2[j]/sum(counts2)))
        frac2.append(fracoil2)

        j += 1
'''
Concentração de Na igual a 1.72
'''
data3 = glob.glob( str(pasta3) + "/gnu_output/*.dat") # Lista os pathnames terminados em dat
frac3 = []    
bt3 = []
list_data3 = []
j = 0

for file in tqdm(data3):
    dat3 = np.loadtxt(file, skiprows=1, usecols=[0,1,2,3]) #lê a lista data com os arquivos txt pulando linha do cabeçalho
    den3 = dat3[:, [0,1,2,3]] # cria uma variável com colunas de dat
    df3 = pd.DataFrame(den3) # tranforma em um DataFrame
    df3.columns = ["X", "Y", "Den1", "Den2"] # nomea as colunas do DataFrame
    wall_max3 = df3.iloc[ df3[ (df3["Den1"] == 0) & (df3["Den2"] == 0) ].index[-1], 0] # identifica o limite de parede 
    df3.drop(df3[df3["X"] > wall_max3].index, inplace = True) # remove todos os valores maiores que wall
    df3.drop(df3[df3["Den1"] == 0].index, inplace = True) # identifica os índices de df com Den1 = 0 e os remove as linhas
    df3.drop(df3[df3["Den2"] == 0].index, inplace = True)  # identifica os índices de df com Den2 = 0 e os remove as linhas
    df3["Den"] = df3.values[:,3] - df3.values[:,2] # Cria uma coluna Den em df cujo valor é a diferença da coluna 3 pela coluna 2 de df
    df3.loc[df3.loc[:, "Den"] < 0, "Den"] = 0 # salmoura - na coluna Den, identifica as linhas cujos valores são negativos e iguala a zero
    df3.loc[df3.loc[:, "Den"] > 0, "Den"] = 1 # petróleo - na coluna Den, identifica as linhas cujos valores são positivos e iguala a um
    counts3 = df3["Den"].value_counts() # Conta quando de cada valor tem na coluna Den (quantos uns e quantos zeros)
    # Aqui surge um erro pois counts deixa de ter duas linhas no final
    if len(counts3) == 2:
        oil3 = float(counts3[1])
        list_data3.append(oil3)
        fracoil3 = 100*(1-(list_data3[j]/sum(counts3)))
        frac3.append(fracoil3)
        time.append(j*dt)
        j += 1
    else:
        bt3.append(j)
        oil3 = 0
        list_data3.append(oil3)
        fracoil3 = 100*(1-(list_data3[j]/sum(counts3)))
        frac3.append(fracoil3)
        time.append(j*dt)
        j += 1
 



plt.ylabel(rf'Oil Extraction($\%$ oil displaced)',fontdict = font)
plt.xlabel(rf'Time(s)', fontdict = font)
plt.plot(time,frac,'b',label = 'NaCl(0.00)',linewidth=1, linestyle='dotted')
plt.axvline(time[len(list_data)-1], color = 'y', label = 'breakthrough',linestyle='dashed', linewidth=1, markersize=10)
plt.text(time[len(list_data)-1], frac[int(len(frac)/2)], rf'${round(dt*time[-1],5)} s$', fontdict=font2)

plt.plot(time,frac2,'r',label = 'NaCl(0.05)',linewidth=1, linestyle='dotted')
plt.axvline(time[len(list_data2)-1], color = 'y', label = 'breakthrough',linestyle='dashed', linewidth=1, markersize=10)
plt.text(time[len(list_data2)-1], frac[int(len(frac2)/2)], rf'${round(dt*time[-1],5)} s$', fontdict=font2)

plt.plot(time,frac3,'-g',label = 'NaCl(1.72)',linewidth=1, linestyle='dotted')
plt.axvline(time[len(list_data3)-1], color = 'y', label = 'breakthrough',linestyle='dashed', linewidth=1, markersize=10)
plt.text(time[len(list_data3)-1], frac[int(len(frac3)/2)], rf'${round(dt*time[-1],5)} s$', fontdict=font2)


plt.legend(loc = "lower right")
plt.savefig("reicoveryfactor.png",dpi=300)
plt.show()

        
    
