# -*- coding: utf-8 -*-
import sys
import cv2  
import numpy as np 
import Tkinter
from mpl_toolkits.mplot3d import Axes3D 
import matplotlib.pyplot as plt 
from PyZenity import *
import FileDialog
InfoMessage('¡El equipo CoDigAR le da la bienvenida!')
class Muestra:
    path=''
    nombre=''
    color=''
    img=[[], [], []]
    rgb=[[],[],[]]
    fft=[]
    hvs=[]
    def LeerImg(self):
        self.img[0]=cv2.imread(self.path,0)
        self.img[1]=cv2.imread(self.path)
        self.img[2]=cv2.cvtColor(self.img[1],cv2.COLOR_BGR2HSV)
    def RGB(self):
        self.rgb[2],self.rgb[1],self.rgb[0]=cv2.split(self.img[1])
    def Plt3D(self):
        ax.scatter(self.rgb[2],self.rgb[1],-self.rgb[0], c=self.color) #grafico
        ax.set_xlabel('R')
        ax.set_ylabel('G')
        ax.set_zlabel('B')
    def FFT(self):
        f = np.fft.fft2(self.img[0])
        fshift = np.fft.fftshift(f)
        fshift = np.fft.ifftshift(fshift)
        self.fft = 20*np.log(np.abs(fshift))
    def HVS(self):
        self.hvs = cv2.calcHist( [self.img[2]], [0, 1], None, [180, 256], [0, 180, 0, 256] )

cant=int(GetText(text='¿Cuántas muestras querés analizar?', entry_text='3', password=False))

fig = plt.figure(-1) #creo obj fig 3D
ax = fig.add_subplot(111, projection='3d') #indico param grafico
muestra=[] #Lista de objetos de clase Muestra()
for i in range(cant):
    InfoMessage('A continuación ingresá el archivo .png, un nombre y el color para graficar de la muestra:')
    muestra.append(Muestra()) #se crea un obj por cada muestra
##Seteo de parámetros##
    muestra[i].path=GetFilename(multiple=False, sep='|')[0]
    muestra[i].nombre=GetText(text='Nombre de la muestra:', entry_text='', password=False)
    muestra[i].color=GetText(text='Color de nube de puntos:', entry_text='', password=False)
##Métodos del obj###
    muestra[i].LeerImg()
    muestra[i].RGB()
    muestra[i].Plt3D()
###FFT###
    muestra[i].FFT()
    plt.figure(i)
    plt.subplot(121),plt.imshow(muestra[i].img[0],cmap = 'gray')
    plt.title(muestra[i].nombre), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(muestra[i].fft, cmap = 'gray')
    plt.title('Espectro de '+muestra[i].nombre), plt.xticks([]), plt.yticks([])
###HVS###
    muestra[i].HVS()
    plt.figure(i+cant)
    plt.subplot(121),plt.imshow(muestra[i].img[2],cmap = 'gray')
    plt.title(muestra[i].nombre), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(muestra[i].hvs,interpolation = 'nearest')
    plt.title('HVS de '+muestra[i].nombre), plt.xticks([]), plt.yticks([])
##Muestro gráficas##
plt.show(-1)
for i in range(cant*2+1):
    plt.show(i)
