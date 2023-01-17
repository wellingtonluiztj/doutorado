#!/usr/bin/env python3
# -- coding: utf-8 --

#%%


import numpy as np
import matplotlib.pyplot as plt
from skimage.morphology import disk
from scipy import ndimage
import pandas as pd



###############################  FORMA 1  ################################


lx=400
ly=200
sqr1 = np.zeros((ly, lx), dtype=np.uint8)

#por = float(input('Porosidade: '))


radio1 = 40
circ1 = disk(radio1)


x = int(lx/2)
y = int(ly/2)

sqr1[y-radio1:y+radio1, x-radio1:x+radio1] = circ1[:-1,:-1]


x = 0
y = 0

sqr1[y:y+radio1, x:x+radio1] = circ1[radio1:-1,radio1:-1]

x = lx-radio1
y = ly-radio1

sqr1[y:y+radio1, x:x+radio1] = circ1[:radio1,:radio1]


x = lx
y = 0

sqr1[:radio1+1, x-radio1+1:x] = circ1[radio1:,1:radio1]

x = 0
y = ly

sqr1[ly-radio1:ly, :radio1] = circ1[:radio1, radio1+1:]

n = 1
sqr1 = np.concatenate([sqr1]*n, axis = 0) 
sqr1 = np.concatenate([sqr1]*n, axis = 1)

############################  FORMA 2   ########################################
lx2=int(lx/2)
ly2=int(ly/2)

sqr2 = np.zeros((ly2, lx2), dtype=np.uint8)

radio2 = int(radio1/2)
circ2 = disk(radio2)


x = int(lx2/2)
y = int(ly2/2)
sqr2[y-radio2:y+radio2, x-radio2:x+radio2] = circ2[:-1,:-1]


x = 0
y = 0

sqr2[y:y+radio2, x:x+radio2] = circ2[radio2:-1,radio2:-1]

x = lx2-radio2
y = ly2-radio2

sqr2[y:y+radio2, x:x+radio2] = circ2[:radio2,:radio2]


x = lx2
y = 0

sqr2[:radio2+1, x-radio2+1:x] = circ2[radio2:,1:radio2]

x = 0
y = ly2

sqr2[ly2-radio2:ly2, :radio2] = circ2[:radio2, radio2+1:]


sqr2 = np.concatenate([sqr2]*2*n, axis = 0) 
sqr2 = np.concatenate([sqr2]*2*n, axis = 1)

############################  FORMA 3   ########################################
lx3=int(lx2/2)
ly3=int(ly2/2)

sqr3 = np.zeros((ly3, lx3), dtype=np.uint8)

radio3 = int(radio2/2)
circ3 = disk(radio3)


x = int(lx3/2)
y = int(ly3/2)
sqr3[y-radio3:y+radio3, x-radio3:x+radio3] = circ3[:-1,:-1]


x = 0
y = 0

sqr3[y:y+radio3, x:x+radio3] = circ3[radio3:-1,radio3:-1]

x = lx3-radio3
y = ly3-radio3

sqr3[y:y+radio3, x:x+radio3] = circ3[:radio3,:radio3]


x = lx3
y = 0

sqr3[:radio3+1, x-radio3+1:x] = circ3[radio3:,1:radio3]

x = 0
y = ly3

sqr3[ly3-radio3:ly3, :radio3] = circ3[:radio3, radio3+1:]


sqr3 = np.concatenate([sqr3]*4*n, axis = 0) 
sqr3 = np.concatenate([sqr3]*4*n, axis = 1)

############################  FORMA 4   ########################################
lx4=int((lx3)/2)
ly4=int(ly3/2)

sqr4 = np.zeros((ly4, lx4), dtype=np.uint8)

radio4 = int(radio3/2) 
circ4 = disk(radio4) 


x = int(lx4/2)
y = int(ly4/2)
sqr4[y-radio4:y+radio4, x-radio4:x+radio4] = circ4[:-1,:-1]


x = 0
y = 0

sqr4[y:y+radio4, x:x+radio4] = circ4[radio4:-1,radio4:-1]

x = lx4-radio4
y = ly4-radio4

sqr4[y:y+radio4, x:x+radio4] = circ4[:radio4,:radio4]


x = lx4
y = 0

sqr4[:radio4+1, x-radio4+1:x] = circ4[radio4:,1:radio4]

x = 0
y = ly4

sqr4[ly4-radio4:ly4, :radio4] = circ4[:radio4, radio4+1:]


sqr4 = np.concatenate([sqr4]*8*n, axis = 0) 
sqr4 = np.concatenate([sqr4]*8*n, axis = 1)

############################     PLOT    ##################################
sg1 = np.sum(sqr1 == 1)
sp1 = np.sum(sqr1 == 0)
porosity1 = sp1/(sp1 + sg1)

sg2 = np.sum(sqr2 == 1)
sp2 = np.sum(sqr2 == 0)
porosity2 = sp2/(sp2 + sg2)

sg3 = np.sum(sqr3 == 1)
sp3 = np.sum(sqr3 == 0)
porosity3 = sp3/(sp3 + sg3)

sg4 = np.sum(sqr4 == 1)
sp4 = np.sum(sqr4 == 0)
porosity4 = sp4/(sp4 + sg4)



# Plot
fig, axs = plt.subplots(2, 2)
axs[0, 0].imshow(sqr1, cmap=plt.cm.gray)
axs[0, 0].axis('off')
axs[0, 0].title.set_text(f'por = {round(porosity1, 2)},{sqr1.shape[0]}X{sqr1.shape[1]}')
axs[0, 1].imshow(sqr2, cmap=plt.cm.gray)
axs[0, 1].axis('off')
axs[0, 1].title.set_text(f'por = {round(porosity2, 2)},{sqr2.shape[0]}X{sqr2.shape[1]}')
axs[1, 0].imshow(sqr3, cmap=plt.cm.gray)
axs[1, 0].axis('off')
axs[1, 0].title.set_text(f'por = {round(porosity3, 2)}, {sqr3.shape[0]}X{sqr3.shape[1]}')
axs[1, 1].imshow(sqr4, cmap=plt.cm.gray)
axs[1, 1].axis('off')
axs[1, 1].title.set_text(f'por = {round(porosity4, 2)},{sqr4.shape[0]}X{sqr4.shape[1]}')

plt.subplot_tool()
plt.show()
#%%

"""
Created on Wed Nov 30 11:45:00 2022

@author: wsantos
"""

from skimage.morphology import (cube)
from skimage.morphology import (octahedron)
from skimage.morphology import (ball)
from skimage.morphology import square
import numpy as np
from skimage.draw import disk
import matplotlib.pyplot as plt
import random
import os
import math


###############################################################################
########################## Círculos aleatórios ################################
###############################################################################


def cirrand(lx, ly, prs, r, txtname, figname, cutoff=8, dist=2, mradio=math.isqrt(lx)):
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

    return plt.imshow(sqr, cmap=plt.cm.gray), plt.axis('off'), plt.title(f'ly = {ly}, lx = {lx}, porosity = {round(porosity, 2)}'), plt.xlabel(f'Ly = {ly}'),plt.savefig(figname, dpi=300), np.savetxt(file, p + x_inlet, fmt='%i'), print(f'A porosidade é {porosity}.')


cirrand(lx=400, ly=200, prs=0.5, r = 20,txtname='cirrand.dat', figname='cirrand.png')
# %%


#!/usr/bin/env python3
# -- coding: utf-8 --
"""
Created on Wed Nov 30 11:45:00 2022

@author: wsantos
"""


###############################################################################
########################## Círculos aleatórios ################################
###############################################################################

def cirrand(lx, ly, prs, txtname, figname, cutoff=8, dist=2, mradio=math.isqrt(ly)):
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
    sqr = np.zeros((lx, ly), dtype=np.uint8)
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
            x, y = random.randint(0, lx), random.randint(0, ly)
            if (0 < x < (lx)) and (0 < y < (ly)):
                radio = random.randint(4, cutoff)
                check_radios, check_center = disk(
                    (x, y), radio + 2, shape=(lx, ly))  # raio de corte
                radios, center = disk((x, y), radio, shape=(lx, ly))
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

    return plt.imshow(sqr, cmap=plt.cm.gray), plt.axis('off'), plt.title(f'ly = {lx}, lx = {ly}, porosity = {round(porosity, 2)}'), plt.savefig(figname, dpi=300), np.savetxt(file, p + x_inlet, fmt='%i'), print(f'A porosidade é {porosity}.')


cirrand(lx=200, ly=500, prs=0.61, txtname='data', figname='figure.png')


#%%


def sphreg(r, sep, txtname='sphreg.dat', figname="sphreg.png"):

    shape1 = (sep, 2*r + 1, 2*r + 1)
    img1 = np.zeros(shape1, dtype=np.uint8)
    sphere1 = ball(r)
    u = np.concatenate([sphere1, img1, sphere1, img1, sphere1, img1], axis=0)

    shape2 = (len(u), sep, 2*r + 1)
    img2 = np.zeros(shape2, dtype=np.uint8)
    w = np.concatenate([u, img2, u, img2, u, img2], axis=1)

    shape3 = (len(u), len(u), sep)
    img3 = np.zeros(shape3, dtype=np.uint8)
    z = np.concatenate([w, img3, w, img3, w, img3], axis=2)

    fig = plt.figure()
    ax = plt.figure().add_subplot(projection='3d')

    p = []
    for k in range(len(z)):
        for j in range(len(z)):
            for i in range(len(z)):
                if z[i, j, k] == 0:
                    p.append([i, j, k])

    p = np.array(p)

    soma_rock = np.sum(p == 1)
    soma_vac = np.sum(p == 0)
    porosity = soma_vac/(soma_vac + soma_rock)

    return ax.voxels(z), ax.set(xlabel='r', ylabel='g', zlabel='b'), ax.set_aspect('auto'), plt.show(), np.savetxt(txtname, p, fmt='%i'), plt.savefig(figname, bpm=300), porosity


sphreg(r=12, sep=8)
# %%


def octreg(r, sep, txtname='octreg.dat', figname="octreg.png"):

    shape1 = (sep, 2*r + 1, 2*r + 1)
    img1 = np.zeros(shape1, dtype=np.uint8)
    octa1 = octahedron(r)
    u = np.concatenate([octa1, img1, octa1, img1, octa1, img1], axis=0)

    shape2 = (len(u), sep, 2*r + 1)
    img2 = np.zeros(shape2, dtype=np.uint8)
    w = np.concatenate([u, img2, u, img2, u, img2], axis=1)

    shape3 = (len(u), len(u), sep)
    img3 = np.zeros(shape3, dtype=np.uint8)
    z = np.concatenate([w, img3, w, img3, w, img3], axis=2)

    fig = plt.figure()
    ax = plt.figure().add_subplot(projection='3d')

    p = []
    for k in range(len(z)):
        for j in range(len(z)):
            for i in range(len(z)):
                if z[i, j, k] == 1:
                    p.append([i, j, k])

    p = np.array(p)

    soma_rock = np.sum(p == 1)
    soma_vac = np.sum(p == 0)
    porosity = soma_vac/(soma_vac + soma_rock)

    return ax.voxels(z), ax.set(xlabel='r', ylabel='g', zlabel='b'), ax.set_aspect('auto'), plt.show(), np.savetxt(txtname, p, fmt='%i'), plt.savefig(figname, bpm=200), porosity


octreg(r=12, sep=8)
# %%


def cubreg(r, sep, txtname='cubreg.dat', figname="cubreg.png"):

    shape1 = (sep, r, r)
    img1 = np.zeros(shape1, dtype=np.uint8)
    cube1 = cube(r)
    u = np.concatenate([cube1, img1, cube1, img1, cube1, img1], axis=0)

    shape2 = (len(u), sep, r)
    img2 = np.zeros(shape2, dtype=np.uint8)
    w = np.concatenate([u, img2, u, img2, u, img2], axis=1)

    shape3 = (len(u), len(u), sep)
    img3 = np.zeros(shape3, dtype=np.uint8)
    z = np.concatenate([w, img3, w, img3, w, img3], axis=2)

    fig = plt.figure()
    ax = plt.figure().add_subplot(projection='3d')

    p = []
    for k in range(len(z)):
        for j in range(len(z)):
            for i in range(len(z)):
                if z[i, j, k] == 1:
                    p.append([i, j, k])

    p = np.array(p)

    soma_rock = np.sum(p == 1)
    soma_vac = np.sum(p == 0)
    porosity = soma_vac/(soma_vac + soma_rock)

    return ax.voxels(z), ax.set(xlabel='r', ylabel='g', zlabel='b'), ax.set_aspect('auto'), plt.show(), np.savetxt(txtname, p, fmt='%i'), plt.savefig(figname, bpm=200), porosity


cubreg(r=12, sep=8)



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
import numpy as np
import matplotlib.pyplot as plt
import random
from skimage.morphology import cube
    
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

#!/usr/bin/env python3
# -- coding: utf-8 --
"""
Created on Wed Nov 30 11:45:00 2022

@author: wsantos
"""



###############################################################################
################################# Teste #######################################
###############################################################################
lx=200 
ly=400 
prs=0.64 

cutoff=8
sqr = np.zeros((lx, ly), dtype=np.uint8)

# Porosidade
sg = np.sum(sqr == 1)
sp = np.sum(sqr == 0)
porosity = sp/(sp + sg)
min_dist = 8  # distância minima entre duas esferas
r = 10
# int(input("Esfera de raio máximo"))
# Discos
px = list(range(r,lx,3*r))
py = list(range(r,ly,3*r))

for i in px:
    for j in py:
        x, y = i, j
        radio = r
        radios, center = disk((x, y), radio, shape=(lx, ly))
        sqr[radios, center] = 1
        sg = np.sum(sqr == 1)
        sp = np.sum(sqr == 0)
        porosity = sp/(sp + sg)
        delta_p = abs(porosity - prs)

            
print(f'y = {x},x = {y}.')


p = []

for i in range(len(sqr)):
    for j in range(len(sqr[0])):
        if sqr[i, j] == 1:
            p.append([j, len(sqr)-i])



p = np.array(p)
x_inlet = 20
txtname='teste.dat'
file = open(txtname, 'w')
figname='figure.png'

plt.imshow(sqr, cmap=plt.cm.gray)
plt.axis('off')
plt.title(f'ly = {lx}, lx = {ly}, porosity = {round(porosity, 2)}') 
plt.savefig(figname, dpi=300) 
np.savetxt(file, p + x_inlet, fmt='%i')
print(f'A porosidade é {porosity}.')
 

#%%
###############################################################################
################################# Teste #######################################
###############################################################################
import numpy as np
import matplotlib.pyplot as plt
from skimage.morphology import disk


interval = 3
lx=200 
ly=400
# it works just for 6, 11,13, 16, 22, 31, 32, 33, 58, 59, 60, 61, 62, 63, 64, 65, 66
radio = 13
cutoff = radio*interval


sqr = np.zeros((lx, ly), dtype=np.uint8)
circ = disk(radio)


px = list(range(radio, lx + 4*radio , cutoff ))
py = list(range(radio, ly + 4*radio, cutoff ))


for i in px:
    for j in py:
        x, y = i, j
        if x <= (lx-radio) and y <= (ly-radio):
            sqr[x-radio:x+radio, y-radio:y+radio] = circ[:-1,:-1]
        elif y > (ly-radio)  and x < (lx - radio) <= lx:
            sqr[(x-radio):x+radio, y-radio:ly] = circ[:-1,:(radio-(y-ly))]
        elif x  > (lx-radio) and y < (ly - radio) <= ly:
            sqr[x-radio:lx,y-radio:y+radio] = circ[:(radio-(x-lx)),:-1]  
        elif x > (lx - radio) and y > (ly - radio):
            sqr[x-radio:lx, y-radio:ly] = circ[:(radio-(x-lx)),:(radio-(y-ly))]
        elif y > ly and x < lx:
            sqr[(x-radio):x+radio, y-radio:ly] = circ[:-1,:(radio-(y-ly))]
        elif x  > lx and y < ly:
            sqr[x-radio:lx,y-radio:y+radio] = circ[:(radio-(x-lx)),:-1] 

            
sg = np.sum(sqr == 1)
sp = np.sum(sqr == 0)
porosity = sp/(sp + sg)


p = []

for i in range(len(sqr)):
    for j in range(len(sqr[0])):
        if sqr[i, j] == 1:
            p.append([j, len(sqr)-i])


p = np.array(p)
x_inlet = 20
txtname='teste.dat'
file = open(txtname, 'w')
figname='figure.png'

plt.imshow(sqr, cmap=plt.cm.gray)
plt.axis('off')
plt.title(f'ly = {lx}, lx = {ly}, porosity = {round(porosity, 2)}') 
plt.savefig(figname, dpi=300) 
np.savetxt(file, p + x_inlet, fmt='%i')
print(f'A porosidade é {porosity}.')


#%%

import numpy as np
import matplotlib.pyplot as plt
from skimage.morphology import disk
from scipy import ndimage


lx=100
ly=100


sqr = np.zeros((ly, lx), dtype=np.uint8)
# it works just for 6, 11,13, 16, 22, 31, 32, 33, 58, 59, 60, 61, 62, 63, 64, 65, 66
radio = 24
circ = disk(radio)
#############################BLOCO DE MATRIZES##############################

x = int(lx/2)
y = int(ly/2)

sqr[y-radio:y+radio, x-radio:x+radio] = circ[:-1,:-1]


x = 0
y = 0

sqr[y:y+radio, x:x+radio] = circ[radio:-1,radio:-1]

x = lx-radio
y = ly-radio

sqr[y:y+radio, x:x+radio] = circ[:radio,:radio]


x = lx
y = 0

sqr[:radio+1, x-radio+1:x] = circ[radio:,1:radio]

x = 0
y = ly

sqr[ly-radio:ly, :radio] = circ[:radio, radio+1:]
#############################BLOCO DE CONC#####################################
n = int(radio/5)
sqr = np.concatenate([sqr]*n, axis = 0) 
sqr = np.concatenate([sqr]*n, axis = 1)


############################POROSIDADE E PLOT##################################
sg = np.sum(sqr == 1)
sp = np.sum(sqr == 0)
porosity = sp/(sp + sg)
# Plot
plt.imshow(sqr, cmap=plt.cm.gray)
plt.axis('off')
plt.title(f'radio = {radio}, esferas = {n*n}, {sqr.shape[1]} X {sqr.shape[1]}, porosity = {round(porosity, 2)}')  
print(f'O raio é {radio}.')

