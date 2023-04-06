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

#Import image

img = cv2.imread("MicroChipe.png")

#Resize Resolution
cv2.imwrite("MicroChipe.png",img)

#Convert to gray scale
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.resize(img,(0,0),fx=0.397,fy=0.397)



img = np.where(img != 0, 1, img)        
pts = np.argwhere(img==0)

coordinate = []

for i in tqdm(range(len(img))):
    for j in range(len(img[0])):
        if img[i,j] ==0:
            coordinate.append([len(img[1])-j, len(img)-i])
coordinate = np.array(coordinate)

inlet = 40
file = open("Poro_Complexo.dat", "w")
np.savetxt(file, coordinate+inlet, fmt='%i')

soma_zeros = np.sum(img==0)
soma_vac = np.sum(img!=0)
forma = np.shape(img)


sea.heatmap(img==0)

soma_zeros

porosity = soma_vac/(soma_vac + soma_zeros)
print(f'A porosidade é {porosity:.2f}')


