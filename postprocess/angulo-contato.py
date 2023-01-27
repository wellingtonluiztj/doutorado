import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
import glob




datas = glob.glob("gnu_output/*")
datas.sort()
data =  np.loadtxt("gnu_output/RES-100.dat",skiprows=1) 
x,y = data[:,0],data[:,1]

den_1,den_2,is_wall = data[:,3], data[:,4],data[:,7]

den_1 = den_1.reshape((int(np.amax(x)),int(np.amax(y)))) 
is_wall = is_wall.reshape((int(np.amax(x)),int(np.amax(y))))# 
den_1 = np.transpose(den_1)
is_wall = np.transpose(is_wall)


meiox = int(np.shape(den_1)[0]/2)



#plt.axis('off')
#################################  MEDIR AQUI  ###################
cross = 208
plus = 43
##################################################################

plt.figure()
plt.title("Ângulo de Contato")
plt.imshow(den_1)
plt.hlines(y=meiox, xmin=cross, xmax=cross+plus, color='b')
plt.vlines(x=cross, ymin=0.0, ymax=np.shape(den_1)[0], color='b')
plt.vlines(x=cross+plus, ymin=0.0, ymax=np.shape(den_1)[0], color='b')



'''
Cálculo do Âgulo de Contato
'''
 
h = (cross+plus) - cross
w = np.shape(den_1)[0]

R_m = (h**2 + (w/2)**2)/(2*h)

theta = np.arcsin((w/2)/R_m)

pi=3.14
theta = theta*(180/pi)
theta = 90 - theta
print(theta)
