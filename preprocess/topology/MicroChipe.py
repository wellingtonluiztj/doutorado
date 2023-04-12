#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 15:07:31 2021
@author: wsantos
This file.py extract the digital points from an image to use as a rock model
fluid dynamics simulation. 
In the end we need to have the same porosity
"""
#====packages====
import cv2
import numpy as np
import time
from tqdm import tqdm
import os
import pandas as pd
import seaborn as sea
import matplotlib.pyplot as plt


img = cv2.imread("MicroChipe.png")


#Resize Resolution
cv2.imwrite("MicroChipe.png",img)
rsize = 0.92
inlet = 12

#Convert to gray scale
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#img = np.hstack((matplus, img))
img = cv2.resize(img,(0,0),fx=rsize,fy=rsize)

matplus = np.ones((len(img), inlet))
img = np.concatenate((matplus, img), axis = 1)


img = np.where(img != 0,1, img) 


coordinate = []
for i in tqdm(range(len(img))):
    for j in range(len(img[0])):
        if img[i,j] ==0:
            coordinate.append([(len(img[1])-j) + 10, (len(img)-i)])
coordinate = np.array(coordinate)

file = open("/home/wsantos/documentos/doutorado/doutorado/preprocess/topology/MicroChipe.dat", "w")



soma_zeros = np.sum(img==0)
soma_vac = np.sum(img!=0)
forma = np.shape(img)

porosity = soma_vac/(soma_vac + soma_zeros)

np.savetxt(file, coordinate, fmt='%i')

plt.imshow(img, cmap='gray')
plt.title(rf'l_y = {len(img)}, l_x = {len(img[1])}')
print(f'A porosidade é {porosity:.2f}')


