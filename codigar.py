import sys
import cv2  
import numpy as np 
from mpl_toolkits.mplot3d import Axes3D 
import matplotlib.pyplot as plt 

fig = plt.figure() #creo obj fig
ax = fig.add_subplot(111, projection='3d') #indico param grafico

for i in range(1, len(sys.argv)-1, 2): #recorro lista exceptuando nombre del script
    img=cv2.imread(sys.argv[i]) #almaceno img de c/ muestra en un array
    b, g, r = cv2.split(img) #almaceno canales rgb por separado en un array
    ax.scatter(r, g, -b, c=sys.argv[i+1]) #grafico
    ax.set_xlabel('R')
    ax.set_ylabel('G')
    ax.set_zlabel('B')

plt.show() #muestro grafica
