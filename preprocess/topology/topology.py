#!/usr/bin/env python3
# -- coding: utf-8 --


import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update(plt.rcParamsDefault)
from skimage.morphology import (
                                square, rectangle, disk, cube,
                                octahedron, ball
                                )
from scipy import ndimage

import pandas as pd
import random
import os
import math
from matplotlib.patches import FancyArrowPatch, FancyArrow
from mpl_toolkits.mplot3d import proj3d
import shutil
#%%
  

###############################  FORMA 1  ################################
def cirreg(
        
        lx, ly, radio1, inlet = 20, name1 = 'cirreg1.dat',
        name2 = 'cirreg2.dat', name3 = 'cirreg3.dat',
        name4 = 'cirreg4.dat' 
           
           ):
    '''
    Topologia de quatro distribuições regulares com mesma porosidade e raios diferentes
    parameters:
    lx: Resolução da caixa no eixo x    
    ly: Resolução da caixa no eixo y    
    returns:
    porosity: porosidade da topologia
    '''
    shutil.rmtree('/home/wsantos/Documentos/cirreg')
    path = os.path.join("/home/wsantos/Documentos", "cirreg" )
    os.mkdir(path)
    
    
    lx2 = int(lx/2)
    lx3 = int(lx2/2)
    lx4 = int(lx3/2)
    listx = [lx, lx2, lx3, lx4]
    
    
    ly2 = int(ly/2)
    ly3 = int(ly2/2)
    ly4 = int(ly3/2)
    listy = [ly, ly2, ly3, ly4]
    
    
    radio2 = int(radio1/2)
    radio3 = int(radio2/2)
    radio4 = int(radio3/2)
    listradio = [radio1, radio2, radio3, radio4 ]
    
    
    sqr1 = np.zeros((ly, lx), dtype=np.uint8)
    sqr2 = np.zeros((ly2, lx2), dtype=np.uint8)
    sqr3 = np.zeros((ly3, lx3), dtype=np.uint8)
    sqr4 = np.zeros((ly4, lx4), dtype=np.uint8)
    listsqr = [sqr1, sqr2, sqr3, sqr4]
    
    circ1 = disk(radio1)
    circ2 = disk(radio2)
    circ3 = disk(radio3)
    circ4 = disk(radio4)
    listcirc = [circ1, circ2, circ3, circ4]
    
    n = [1, 2, 3, 4]

    files = []
    
    pore = []
    
    inlet = 20
    
    for i, rad in enumerate(listradio):
        x = int(listx[i]/2)
        y = int(listy[i]/2)
        
        
        listsqr[i][y-rad:y+rad, x-rad:x+rad] = listcirc[i][:-1,:-1]
        
        x = 0
        y = 0
        
        listsqr[i][y:y+rad, x:x+rad] =  listcirc[i][rad:-1,rad:-1]
        
        
        x = listx[i]
        y = 0
        
        listsqr[i][:rad+1, x-rad+1:x]  = listcirc[i][rad:,1:rad]
        
        
        x = 0
        y = listy[i]
        
        listsqr[i][y-rad+1:y, :rad+1]  = listcirc[i][1:rad, rad:]
        
        x = listx[i]
        y = listy[i]
        
        listsqr[i][y-rad+1:y,  x-rad+1:x]  = listcirc[i][1:rad, 1:rad]
        
        
        listsqr[i] = np.concatenate([listsqr[i]]*n[i], axis = 0) 
        listsqr[i] = np.concatenate([listsqr[i]]*n[i], axis = 1)
        
        sg = np.sum(listsqr[i] == 1)
        sp = np.sum(listsqr[i] == 0)
        porosity = sp/(sp + sg)
        pore.append(porosity)
        
        p = []
    
        for u in range(len(listsqr[i])):
            for v in range(len(listsqr[i][1])):
                if sqr1[u, v] == 1:
                    p.append([v, len(listsqr[i] )-u])
    
        p = np.array(p)
        
        file = path +'/cirreg' + str(i+1) + '.dat'
        np.savetxt(file, p + inlet, fmt='%i')
        files.append(file)
    

    fig, axs = plt.subplots(2, 2)
    
    return ( 

        fig.suptitle(rf'All geometries are shaped with {sqr1.shape[0]}$\times${sqr1.shape[1]} ', fontsize=16),
        axs[0, 0].imshow(listsqr[0], cmap='binary'),
        axs[0, 0].axis('off'),
        axs[0, 0].set_title(rf'por = {round(pore[0], 2)} \\ radio = {listradio[0]}', size =8, color = 'r'),
        
        axs[0, 1].imshow(listsqr[1], cmap='binary'),
        axs[0, 1].axis('off'),
        axs[0, 1].set_title(rf'por = {round(pore[1], 2)} \\ radio = {listradio[1]}', size =8, color = 'r'),
        
        axs[1, 0].imshow(listsqr[2], cmap='binary'),
        axs[1, 0].axis('off'),
        axs[1, 0].set_title(rf'por = {round(pore[2], 2)} \\ radio = {listradio[2]}', size =8, color = 'r'),
        
        axs[1, 1].imshow(listsqr[2], cmap='binary'),
        axs[1, 1].axis('off'),
        axs[1, 1].set_title(rf'por = {round(pore[3], 2)} \\ radio = {listradio[3]}', size =8, color = 'r'),
        plt.savefig('cirreg.png', dpi=300),
        #plt.subplot_tool(),
        plt.show()

        )

cirreg(lx=400, ly=200, radio1= 40)
#%%

"""
Created on Wed Nov 30 11:45:00 2022

@author: wsantos
"""


def cirrand(lx, ly, prs, r, txtname, figname, cutoff=8, dist=2):
    '''
    Topologia de círculos de mesmo raio distribuídos aleatoriamente 

    parameters:
    lx: Resolução da caixa no eixo x    
    ly: Resolução da caixa no eixo y    
    txtname: nome do arquivo em que é salvo o txt
    figname: nome do arquivo que é salva a imagem
    dist: distância entre cada círculo
    max_radio: o raio máximo que um círculo pode ter    

    returns:
    porosity: porosidade da topologia
    '''
    mradio=math.isqrt(lx)
    sqr = np.zeros((ly, lx), dtype=np.uint8)
    # Porosidade
    sg = np.sum(sqr == 1)
    sp = np.sum(sqr == 0)
    porosity = sp/(sp + sg)
    min_dist = 8  # distância minima entre duas esferas

    # int(input("Esfera de raio máximo"))
    # Discos
    delta_p = 100
    while delta_p >= 0.01:  # critério de convergência
        if sqr.all() != 1:
            y, x = random.randint(0, ly), random.randint(0, lx)
            if (0 < y < (ly)) and (0 < x < (lx)):
                radio = r 
                check_radios, check_center = disk(
                    (y, x), radio + 2, shape=(ly, lx))  # raio de corte
                radios, center = disk((y, x), radio, shape=(ly, lx))
                if np.sum(sqr[check_radios, check_center]) == 0:
                    sqr[radios, center] = 1
                    sg = np.sum(sqr == 1)
                    sp = np.sum(sqr == 0)
                    porosity = sp/(sp + sg)
                    delta_p = abs(porosity - prs)
    p = []

    for i in range(len(sqr)):
        for j in range(len(sqr[0])):
            if sqr[i, j] == 1:
                p.append([j, len(sqr)-i])

    p = np.array(p)
    x_inlet = 20
    file = open(txtname, 'w')

    return (
            
            plt.imshow(sqr, cmap=plt.cm.gray),
            plt.axis('off'),
            plt.title(rf'por = {round(porosity, 2)} \\ radio = {radio} \\ size = {lx}$\times${ly}' , size =12, color = 'r'),
            plt.xlabel(f'Ly = {ly}'),
            plt.savefig(figname, dpi=300),
            np.savetxt(file, p + x_inlet, fmt='%i'),
            
            )


cirrand(lx = 400, ly=200, prs=0.5, r = 20,txtname='cirrand.dat', figname='cirrand.png')
# %%

"""
Created on Wed Nov 30 11:45:00 2022

@author: wsantos
"""


def cirrand(ly, lx, prs, txtname, figname, cutoff=8, dist=2):
    '''
    Topologia de círculos de diferentea raios distribuídos aleatoriamente 

    parameters:
    lx: Resolução da caixa no eixo x    
    ly: Resolução da caixa no eixo y    
    txtname: nome do arquivo em que é salvo o txt
    figname: nome do arquivo que é salva a imagem
    dist: distância entre cada círculo
    max_radio: o raio máximo que um círculo pode ter    

    returns:
    porosity: porosidade da topologia
    '''
    mradio=math.isqrt(ly)
    sqr = np.zeros((ly, lx), dtype=np.uint8)
    # Porosidade
    sg = np.sum(sqr == 1)
    sp = np.sum(sqr == 0)
    porosity = sp/(sp + sg)
    min_dist = 8  # distância minima entre duas esferas

    # int(input("Esfera de raio máximo"))
    # Discos
    delta_p = 100
    while delta_p >= 0.01:  # critério de convergência
        if sqr.all() != 1:
            y, x= random.randint(0, ly), random.randint(0, lx)
            if (0 < y < (ly)) and (0 < x < (lx)):
                radio = random.randint(4, cutoff)
                check_radios, check_center = disk(
                    (y, x), radio + 2, shape=(ly, lx))  # raio de corte
                radios, center = disk((y, x), radio, shape=(ly, lx))
                if np.sum(sqr[check_radios, check_center]) == 0:
                    sqr[radios, center] = 1
                    sg = np.sum(sqr == 1)
                    sp = np.sum(sqr == 0)
                    porosity = sp/(sp + sg)
                    delta_p = abs(porosity - prs)
    p = []

    for i in range(len(sqr)):
        for j in range(len(sqr[0])):
            if sqr[i, j] == 1:
                p.append([j, len(sqr)-i])

    p = np.array(p)
    x_inlet = 20
    file = open(txtname, 'w')

    return(
        plt.imshow(sqr, cmap=plt.cm.gray), plt.axis('off'),
        plt.title(rf'por = {round(porosity, 2)} \\ radio = {radio} \\ size = {lx}$\times${ly}' , size =12, color = 'r'),
        plt.savefig(figname, dpi=300), np.savetxt(file, p + x_inlet, fmt='%i'),
        print(f'A porosidade é {porosity}.')
)

cirrand(lx=400, ly=200, prs=0.61, txtname='data', figname='figure.png')


#%%

def sphreg(lx, ly, lz, radio1):
    
    
    
    
    
    shutil.rmtree('/home/wsantos/Documentos/sphreg')
    path = os.path.join("/home/wsantos/Documentos", "sphreg" )
    os.mkdir(path)
    
    
    lx2 = int(lx/2)
    lx3 = int(lx2/2)
    lx4 = int(lx3/2)
    listx = [lx, lx2, lx3, lx4]
    
    
    ly2 = int(ly/2)
    ly3 = int(ly2/2)
    ly4 = int(ly3/2)
    listy = [ly, ly2, ly3, ly4]
    
    
    lz2 = int(lz/2)
    lz3 = int(lz2/2)
    lz4 = int(lz3/2)
    listz = [lz, lz2, lz3, lz4]
    
    radio2 = int(radio1/2)
    radio3 = int(radio2/2)
    radio4 = int(radio3/2)
    listradio = [radio1, radio2, radio3, radio4 ]
    
    
    sqr1 = np.zeros((lz, ly, lx), dtype=np.uint8)
    sqr2 = np.zeros((lz2, ly2, lx2), dtype=np.uint8)
    sqr3 = np.zeros((lz3, ly3, lx3), dtype=np.uint8)
    sqr4 = np.zeros((lz4, ly4, lx4), dtype=np.uint8)
    listsqr = [sqr1, sqr2, sqr3, sqr4]
    
    sph1 = ball(radio1)
    sph2 = ball(radio2)
    sph3 = ball(radio3)
    sph4 = ball(radio4)
    listsph = [sph1, sph2, sph3, sph4]
    
    n = [1, 2, 3, 4]
    
    files = []
    
    pore = []
    

    
    
    for i, rad in enumerate(listradio):
        x = int(listx[i]/2)
        y = int(listy[i]/2)
        z = int(listz[i]/2)
        
        listsqr[i][z-rad:z+rad, y-rad:y+rad, x-rad:x+rad] = listsph[i][:-1,:-1,:-1]
        
         
        x = 0
        y = 0
        z = 0
        
        listsqr[i][z: z+rad, y:y+rad, x:x+rad] =  listsph[i][rad:-1,rad:-1,rad:-1]
        
        
        x = listx[i]
        y = 0
        z = listz[i]
        listsqr[i][z-rad+1:z,:rad+1, x-rad+1:x] = listsph[i][1:rad,rad:,1:rad]
        
        
        x = listx[i]
        y = 0
        z = 0
        listsqr[i][:rad+1,:rad+1, x-rad+1:x] = listsph[i][rad:,rad:,1:rad]
        
        
        x = listx[i]
        y = listy[i]
        z = 0
        listsqr[i][:rad+1,y-rad+1:y, x-rad+1:x] = listsph[i][rad:,1:rad,1:rad]
        
        
        x = 0
        y = 0
        z = listz[i]
        
        listsqr[i][z-rad:z+1,:rad+1, :rad+1] = listsph[i][:rad,rad:,rad:]
        
        
        x = 0
        y = 0
        z = listz[i]
        
        listsqr[i][z-rad:z+1,:rad+1, :rad+1] = listsph[i][:rad,rad:,rad:]
        
        
        x = 0
        y = listy[i]
        z = 0
        
        listsqr[i][:rad+1,y-rad:y+1, :rad+1] = listsph[i][rad:,:rad, rad:]
        
        x = listx[i]
        y = listy[i]
        z = listz[i]
        
        listsqr[i][z-rad:z+1,y-rad:y+1,x-rad:x+1] = listsph[i][:rad,:rad, :rad]
        
        
        x = 0
        y = listy[i]
        z = listz[i]
        
        listsqr[i][z-rad:z+1,y-rad:y+1,:rad+1] = listsph[i][:rad,:rad, rad:]
        
        
        listsqr[i] = np.concatenate([listsqr[i]]*n[i], axis = 0)
        listsqr[i] = np.concatenate([listsqr[i]]*n[i], axis = 1)
        listsqr[i] = np.concatenate([listsqr[i]]*n[i], axis = 2)
    
        sg = np.sum(listsqr[i] == 1)
        sp = np.sum(listsqr[i] == 0)
        porosity = sp/(sp + sg)
        pore.append(porosity)
    
        p = []
        for u in range(len(listsqr[i])):
            for v in range(len(listsqr[i])):
                for w in range(len(listsqr[i])):
                    if listsqr[i][w, v, u] == 1:
                        p.append([w, v, u])
        
        file = path +'/sphreg' + str(i+1) + '.dat'
        np.savetxt(file, p, fmt='%i')
        files.append(file)

    
    
    fig, ax = plt.subplots(2, 2, figsize=(5, 5),
                            subplot_kw=dict(projection="3d",
                                            proj_type='ortho'))
    return(
    fig.suptitle(rf'All geometries are shaped with {sqr1.shape[0]}$\times${sqr1.shape[1]} ', fontsize=16),
    ax[0,0].voxels(listsqr[0], facecolors=[0, 0, 0, 0], edgecolors='k'),
    ax[0,0].set_title(rf'por = {round(pore[0], 2)} \\ radio = {listradio[0]}', size =8, color = 'r'),
    
    
    ax[0,1].voxels(listsqr[1], facecolors=[0, 0, 0, 0], edgecolors='k'),
    ax[0,1].set_title(rf'por = {round(pore[1], 2)} \\ radio = {listradio[1]}', size =8, color = 'r'),
    
    
    ax[1,0].voxels(listsqr[2], facecolors=[0, 0, 0, 0], edgecolors='k'),
    ax[1,0].set_title(rf'por = {round(pore[2], 2)} \\ radio = {listradio[2]}', size =8, color = 'r'),
    
    
    ax[1,1].voxels(listsqr[3], facecolors=[0, 0, 0, 0], edgecolors='k'),
    ax[1,1].set_title(rf'por = {round(pore[3], 2)} \\ radio = {listradio[3]}', size =8, color = 'r'),
    
    plt.savefig('sphreg.png', bpm=300),
    
    
    plt.show()

)

sphreg(lx = 90, ly = 90, lz = 90, radio1 = 30)
# %%


def cubreg(lx, ly, lz, radio1):
    
    
    
    
    
    shutil.rmtree('/home/wsantos/Documentos/cubreg')
    path = os.path.join("/home/wsantos/Documentos", "cubreg" )
    os.mkdir(path)
     
    
    
    lx2 = int(lx/2)
    lx3 = int(lx2/2)
    lx4 = int(lx3/2)
    listx = [lx, lx2, lx3, lx4]
    
    
    ly2 = int(ly/2)
    ly3 = int(ly2/2)
    ly4 = int(ly3/2)
    listy = [ly, ly2, ly3, ly4]
    
    
    lz2 = int(lz/2)
    lz3 = int(lz2/2)
    lz4 = int(lz3/2)
    listz = [lz, lz2, lz3, lz4]
    
    radio2 = int(radio1/2)
    radio3 = int(radio2/2)
    radio4 = int(radio3/2)
    listradio = [radio1, radio2, radio3, radio4 ]
    
    
    sqr1 = np.zeros((lz, ly, lx), dtype=np.uint8)
    sqr2 = np.zeros((lz2, ly2, lx2), dtype=np.uint8)
    sqr3 = np.zeros((lz3, ly3, lx3), dtype=np.uint8)
    sqr4 = np.zeros((lz4, ly4, lx4), dtype=np.uint8)
    listsqr = [sqr1, sqr2, sqr3, sqr4]
    
    sph1 = cube(int(radio1*2) + 1)
    sph2 = cube(int(radio2*2)+ 1)
    sph3 = cube(int(radio3*2)+ 1)
    sph4 = cube(int(radio4*2)+ 1)
    listsph = [sph1, sph2, sph3, sph4]
    
    n = [1, 2, 3, 4]
    
    files = []
    
    pore = []
    

    
    
    for i, rad in enumerate(listradio):
        x = int(listx[i]/2)
        y = int(listy[i]/2)
        z = int(listz[i]/2)
        
        listsqr[i][z-rad:z+rad, y-rad:y+rad, x-rad:x+rad] = listsph[i][:-1,:-1,:-1]
        
         
        x = 0
        y = 0
        z = 0
        
        listsqr[i][z: z+rad, y:y+rad, x:x+rad] =  listsph[i][rad:-1,rad:-1,rad:-1]
        
        
        x = listx[i]
        y = 0
        z = listz[i]
        listsqr[i][z-rad+1:z,:rad+1, x-rad+1:x] = listsph[i][1:rad,rad:,1:rad]
        
        
        x = listx[i]
        y = 0
        z = 0
        listsqr[i][:rad+1,:rad+1, x-rad+1:x] = listsph[i][rad:,rad:,1:rad]
        
        
        x = listx[i]
        y = listy[i]
        z = 0
        listsqr[i][:rad+1,y-rad+1:y, x-rad+1:x] = listsph[i][rad:,1:rad,1:rad]
        
        
        x = 0
        y = 0
        z = listz[i]
        
        listsqr[i][z-rad:z+1,:rad+1, :rad+1] = listsph[i][:rad,rad:,rad:]
        
        
        x = 0
        y = 0
        z = listz[i]
        
        listsqr[i][z-rad:z+1,:rad+1, :rad+1] = listsph[i][:rad,rad:,rad:]
        
        
        x = 0
        y = listy[i]
        z = 0
        
        listsqr[i][:rad+1,y-rad:y+1, :rad+1] = listsph[i][rad:,:rad, rad:]
        
        x = listx[i]
        y = listy[i]
        z = listz[i]
        
        listsqr[i][z-rad:z+1,y-rad:y+1,x-rad:x+1] = listsph[i][:rad,:rad, :rad]
        
        
        x = 0
        y = listy[i]
        z = listz[i]
        
        listsqr[i][z-rad:z+1,y-rad:y+1,:rad+1] = listsph[i][:rad,:rad, rad:]
        
        
        listsqr[i] = np.concatenate([listsqr[i]]*n[i], axis = 0)
        listsqr[i] = np.concatenate([listsqr[i]]*n[i], axis = 1)
        listsqr[i] = np.concatenate([listsqr[i]]*n[i], axis = 2)
    
        sg = np.sum(listsqr[i] == 1)
        sp = np.sum(listsqr[i] == 0)
        porosity = sp/(sp + sg)
        pore.append(porosity)
    
        p = []
        for u in range(len(listsqr[i])):
            for v in range(len(listsqr[i])):
                for w in range(len(listsqr[i])):
                    if listsqr[i][w, v, u] == 1:
                        p.append([w, v, u])
        
        file = path +'/cubreg' + str(i+1) + '.dat'
        np.savetxt(file, p, fmt='%i')
        files.append(file)

    
    
    fig, ax = plt.subplots(2, 2, figsize=(5, 5),
                            subplot_kw=dict(projection="3d",
                                            proj_type='ortho'))
    return(
    fig.suptitle(rf'All geometries are shaped with {sqr1.shape[0]}$\times${sqr1.shape[1]} ', fontsize=16),
    ax[0,0].voxels(listsqr[0], facecolors=[0, 0, 0, 0], edgecolors='k'),
    ax[0,0].set_title(rf'por = {round(pore[0], 2)} \\ radio = {listradio[0]}', size =8, color = 'r'),
    
    
    ax[0,1].voxels(listsqr[1], facecolors=[0, 0, 0, 0], edgecolors='k'),
    ax[0,1].set_title(rf'por = {round(pore[1], 2)} \\ radio = {listradio[1]}', size =8, color = 'r'),
    
    
    ax[1,0].voxels(listsqr[2], facecolors=[0, 0, 0, 0], edgecolors='k'),
    ax[1,0].set_title(rf'por = {round(pore[2], 2)} \\ radio = {listradio[2]}', size =8, color = 'r'),
    
    
    ax[1,1].voxels(listsqr[3], facecolors=[0, 0, 0, 0], edgecolors='k'),
    ax[1,1].set_title(rf'por = {round(pore[3], 2)} \\ radio = {listradio[3]}', size =8, color = 'r'),
    
    plt.savefig('sphreg.png', bpm=300),
    
    
    plt.show()

)

cubreg(lx = 90, ly = 90, lz = 90, radio1 = 30)
# %%

########################ESFERAS ALEATÓRIOS####################################
import numpy as np
import matplotlib.pyplot as plt
import random
from skimage.morphology import ball

def sphran(la, lb, lc, prs, cutoff = 6, txtname='sphran.dat', figname='sphran.png' ):
    '''
    Esta função cria uma topologia de cubos em posições e diametros aleatórios

    parameters:
    la: eixo x da caixa
    lb: eixo y da caixa
    lc: eixo z da caixa
    cutoff: raio de corte
    prs: porosidade desejada da caixa
    txtname: nome do arquivo de texto
    figname: nome do arquivo de imagem

    returns:
    porosity: porosidade da topologia
    '''
    
    
    a = np.zeros(shape=(la, lb, lc), dtype=np.uint8)
    sg = np.sum(a == 1)
    sp = np.sum(a == 0)
    porosity = sp/(sp + sg)
    
    
    # int(input("Esfera de raio máximo"))
    # Discos
    delta_p = 100
    while delta_p >= 0.01: 
        radio = random.randint(5, 8)
        originx = random.randint(radio, la-radio)
        originy = random.randint(radio, lb-radio)
        originz = random.randint(radio, lc-radio)
        if a[(originx-radio)-cutoff: (originx + radio + cutoff), 
             (originy-radio)-cutoff: (originy + radio + cutoff),
             (originz-radio)-cutoff: (originz + radio + cutoff)
             ].all() == 0:
            b = ball(radio)
            a[originx-radio:(originx+radio)+1,
              originy-radio:(originy+radio)+1,
              originz-radio:(originz+radio)+1] = b
            sg = np.sum(a == 1)
            sp = np.sum(a == 0)
            porosity = sp/(sp + sg)
            delta_p = abs(porosity - prs)
    
    p = []
    for k in range(len(a)):
        for j in range(len(a[1])):
            for i in range(len(a[2])):
                if a[i, j, k] == 1:
                    p.append([i, j, k])
    
    p = np.array(p)
    
    
    fig = plt.figure()
    ax = plt.figure().add_subplot(projection='3d')
    
    
   
    x_inlet = 20
    file = open(txtname, 'w')
    return ax.voxels(a), ax.set(xlabel='r', ylabel='g', zlabel='b'), ax.set_aspect('auto'), plt.show(),  plt.savefig(figname, dpi=300), np.savetxt(file, p + x_inlet, fmt='%i')

sphran(la = 100, lb = 100, lc = 100, prs = 0.96)
# %%

    
###############################CUBOS ALEATÓRIOS################################


def cubran(la, lb, lc, prs, cutoff = 4, txtname='sqrreg.dat', figname='cubran.png' ):
    '''
    Esta função cria uma topologia de cubos em posições e diametros aleatórios

    parameters:
    la: eixo x da caixa
    lb: eixo y da caixa
    lc: eixo z da caixa
    cutoff: raio de corte
    prs: porosidade desejada da caixa
    txtname: nome do arquivo de texto
    figname: nome do arquivo de imagem

    returns:
    porosity: porosidade da topologia
    '''
    
    
    a = np.zeros(shape=(la, lb, lc), dtype=np.uint8)
    sg = np.sum(a == 1)
    sp = np.sum(a == 0)
    porosity = sp/(sp + sg)
    
    
    # int(input("Esfera de raio máximo"))
    # Discos
    delta_p = 100
    while delta_p >= 0.01: 
        diam = random.randint(5, 20)
        originx = random.randint(cutoff, la-diam)
        originy = random.randint(cutoff, lb-diam)
        originz = random.randint(cutoff, lc-diam)
        if a[originx-cutoff: (originx + diam + cutoff), originy-cutoff: (originy + diam + cutoff),
             originz-cutoff: (originz + diam + cutoff)
             ].all() == 0:
            b = cube(diam)
            a[originx:(originx+diam), originy:(originy+diam), originz:(originz+diam)] = b
            sg = np.sum(a == 1)
            sp = np.sum(a == 0)
            porosity = sp/(sp + sg)
            delta_p = abs(porosity - prs)
    
    p = []
    for k in range(len(a)):
        for j in range(len(a[1])):
            for i in range(len(a[2])):
                if a[i, j, k] == 1:
                    p.append([i, j, k])
    
    p = np.array(p)
    
    
    fig = plt.figure()
    ax = plt.figure().add_subplot(projection='3d')
    
    
   
    x_inlet = 20
    file = open(txtname, 'w')
    return ax.voxels(a), ax.set(xlabel='r', ylabel='g', zlabel='b'), ax.set_aspect('auto'), plt.show(),  plt.savefig(figname, dpi=300), np.savetxt(file, p + x_inlet, fmt='%i')

cubran(la = 140, lb = 100, lc = 200, prs = 0.84)

# %%
from matplotlib import pyplot as plt
import numpy as np
import math


sand = np.fromfile('berea-sandstone.raw')
sand[np.isnan(sand)] = 0
sqr = np.zeros(shape=(100, 100, 100), dtype=np.uint8)
# sqr = sqr + abs(min(sqr))   

# 

# sqr = [ int(x) for x in sqr ]

# sqr = np.array(sqr)


amin, amax = min(sand), max(sand)
for i, val in enumerate(sand):
    sand[i] = 500*(val-amin) / (amax-amin)
    if sand[i] > 1:
        sand[i] = 0
    else:
        sand[i] = 1


sand = sand.reshape(125,1000,1000)



rad = 100
sqr[:rad, :rad, :rad] = sand[:rad,:rad:,:rad]

#sqr = np.rint(sqr) 
#sg = np.sum(sqr != 0)
#print(sg)




p = []
for k in range(len(sqr[2])):
    for j in range(len(sqr[1])):
        for i in range(len(sqr[0])):
            if sqr[i,j,k] == 1:
                p.append([i, j, k])
       
p = np.array(p)
np.savetxt("sand.dat", p, fmt='%i')

  
fig = plt.figure()
ax = plt.figure().add_subplot(projection='3d')
ax.voxels(sqr, facecolors=[0, 0, 0, 0], edgecolors='k')
plt.show()

