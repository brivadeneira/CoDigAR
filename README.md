# CoDigAR

"**Co**lorimetría **Dig**ital de **A**rte **R**upestre / **AR**gentina": Técnicas y algoritmos de determnación cuantitativa de características de arte rupestre vinculadas con la antigüedad de las mismas, mediante el tratamiento de fotografías de las rocas en cuestión.

El usuario debe, a partir de una fotografía de la roca a analizar, determinar, rotular y extraer las muestras de interés mediante una herramienta de selección libre de un software de edición de imágenes, CoDigAR se encarga de:

- Determinar y almacenar el código de colores presente en cada pixel de la muestra.
- Convertir dicho código a RGB.
- Exponer los resultados en un gráfico 3D.
- Permitir análisis cuantitativo, cualitativo y comparativo.

## Capturas

Los resultados de la implementación de [CuanCTo](https://github.com/brivadeneira/CoDigAR/wiki/4.1-CuanCTo) para las siguientes tres muestras,

![](https://github.com/brivadeneira/CoDigAR/blob/master/img/demo/ar.png?raw=true)
Arte rupestre - [Peñas Coloradas](https://es.wikiloc.com/wikiloc/view.do?id=1319853), dpto de Antofagasta de la Sierra, provincia de Catamarca, Argentina.

![](https://github.com/brivadeneira/CoDigAR/blob/master/img/demo/m0.png?raw=true) muestra 0, matriz (roca sin tallar), puntos rojos.

![](https://github.com/brivadeneira/CoDigAR/blob/master/img/demo/m1.png?raw=true) muestra 1, sector del lomo del camélido, puntos azules.

![](https://github.com/brivadeneira/CoDigAR/blob/master/img/demo/m2.png?raw=true) muestra 2, sector del motivo serpentiforme, puntos verdes.

son:

![](https://github.com/brivadeneira/CoDigAR/blob/master/img/demo/ploteo1.png?raw=true) 


![](https://github.com/brivadeneira/CoDigAR/blob/master/img/demo/ploteo2.png?raw=true) 

## Guía de uso rápido

### Requerimientos

- [Python](https://www.python.org/downloads/) 2.7.12
- [OpenCV](http://opencv.org/downloads.html)
- [numpy](http://www.numpy.org/)
- [matplotlib](http://matplotlib.org/1.4.3/mpl_toolkits/index.html)

### Sintaxis

```
python codigar.py ruta_muestra0 color0 ... ruta_muestraN colorN
```
#### Ejemplo
El siguiente código reporta los resultados expuestos en las capturas:
```
python codigar.py img/demo/m0.png red img/demo/m1.png blue img/demo/m2.png green
```


## Más información

CoDigAR es un proyecto académico argentino que permite obtener más información sobre el arte rupestre, mediante el análisis de un tipo particular de rasgo: las imagenes, más específicamente aquellas manifestaciones gráficas de antiguas culturas, a través del uso de la tecnología y herramientas libres y mediante el trabajo en conjunto de dos campos científicos: -Arqueología e Ingeniería en
Telecomunicaciones- de dos universidades nacionales, dotando así a los resultados de cuantificación y exactitud.

Se trata de **técnicas inéditas de análisis y determinación cuantitativa de características de arte rupestre** empleando como información cruda fotografías de las rocas en cuestión y haciendo uso emphherramientas libres de tratamiento digital de imágenes para la automatización del proceso.

### Objetivos a corto o mediano plazo

- [x] **Desarrollo teórico y experimental de una técnica inédita** de análisis de manifestaciones rupestres, a partir de la cuantificación de un procedimiento que hasta la actualidad se realiza cualitativamente.
- [x] **Desarrollo de algoritmos de automatización**  de dicha técnica empleando herramientas libres.

### Objetivos a largo plazo
- [ ] **Experimentación y evolución** de la técnica en base al control de variables, a fin de determinar las fortalezas, debilidades y alcances del proyecto para su mejora.
- [ ] **Presentación de los resultados obtenidos** referentes a la técnica desarrollada y la fase experimental a través de informes técnicos estandarizados.
- [ ] **Mejora y evolución de los algoritmos** incluyendo: interfáz de usuario, correcciones y preparación de la imagen, banco de datos.

## Documentación

| Acerca de CoDigAR | Acerca del equipo  | Guía de instalación y uso | Documentación técnica |
|:--------:|:--------:|:--------:|:--------:|
|    [![](https://github.com/brivadeneira/CoDigAR/blob/master/img/iconos/question-mark-6x.png?raw=true)](https://github.com/brivadeneira/CoDigAR/wiki/1.-Acerca-de-CoDigAR)     |    [![](https://github.com/brivadeneira/CoDigAR/blob/master/img/iconos/people-6x.png?raw=true)](https://github.com/brivadeneira/CoDigAR/wiki/2.-Acerca-del-equipo)    |    [![](https://github.com/brivadeneira/CoDigAR/blob/master/img/iconos/wrench-6x.png?raw=true)](https://github.com/brivadeneira/CoDigAR/wiki/3.-Guía-de-instalación-y-uso)    |    [![](https://github.com/brivadeneira/CoDigAR/blob/master/img/iconos/document-6x.png?raw=true)](https://github.com/brivadeneira/CoDigAR/wiki/4.-Documentación-técnica)    |

## Licencia

        				Copyright (C)  2016  CoDigAR.
                        
    	This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    	This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

