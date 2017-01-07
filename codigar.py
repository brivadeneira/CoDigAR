import sys
import cv2  
import numpy as np 
from mpl_toolkits.mplot3d import Axes3D 
import matplotlib.pyplot as plt 

fig = plt.figure() #creo obj fig
ax = fig.add_subplot(111, projection='3d') #indico param grafico

for i in range(1, len(sys.argv)-1, 2): #recorro lista exceptuando nombre del script
    img=cv2.imread(sys.argv[i]) #almaceno img de c/ muestra en un array
#### RGB ####
    b, g, r = cv2.split(img) #almaceno canales rgb por separado en un array
    ax.scatter(r, g, -b, c=sys.argv[i+1]) #grafico
    ax.set_xlabel('R')
    ax.set_ylabel('G')
    ax.set_zlabel('B')
plt.show() #muestro grafica

for i in range(1, len(sys.argv)-1, 2): #recorro lista exceptuando nombre del script
    img=cv2.imread(sys.argv[i],0) #almaceno img de c/ muestra en un array
#### FFT ####
    f = np.fft.fft2(img)
    fshift = np.fft.fftshift(f)
    fshift = np.fft.ifftshift(fshift)
    magnitude_spectrum = 20*np.log(np.abs(fshift))
    plt.subplot(121),plt.imshow(img,cmap = 'gray')
    plt.title(sys.argv[i]), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
    plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
    plt.show()
for i in range(1, len(sys.argv)-1, 2): #recorro lista exceptuando nombre del script
    img=cv2.imread(sys.argv[i]) #almaceno img de c/ muestra en un array
#### HVS ####
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    hist = cv2.calcHist( [hsv], [0, 1], None, [180, 256], [0, 180, 0, 256] )
    plt.subplot(121),plt.imshow(img,cmap = 'gray')
    plt.title(sys.argv[i]), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(hist,interpolation = 'nearest')
    plt.title('HSV'), plt.xticks([]), plt.yticks([])
    plt.show()
