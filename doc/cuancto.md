#CuanCTo
"**Cuan**tificación de **C**onjuntos **T**onales"

[TOC]

##Introducción

###Motivación

El espíritu y la filosofía que impulsan el desarrollo de CoDigAR son inspirados por los principios del *software libre*. Un software es libre si garantiza al usuario las siguientes libertades esenciales *(«gnu.org» 2016)*:

- La libertad de ejecutar el programa como se desea, con cualquier propósito (libertad 0).
- La libertad de estudiar cómo funciona el programa, y cambiarlo para que haga lo que usted quiera (libertad 1). El acceso al código fuente es una condición necesaria para ello.
- La libertad de redistribuir copias para ayudar a su prójimo (libertad 2). 
- La libertad de distribuir copias de sus versiones modificadas a terceros (libertad 3). Esto le permite ofrecer a toda la comunidad la oportunidad de beneficiarse de las modificaciones. El acceso al código fuente es una condición necesaria para ello.

Actualmente, el desarrollo de software en el ámbito de la arqueología se está abriendo paso en la academia tanto para la sistematización y la optimización en los métodos de registro, así como también para el análisis de datos.

Cuando la década de los ’60 la Teoría General de Sistemas sirvió de inspiración para el desarrollo de teorías culturales y la incorporación de nuevas técnicas de análisis, la confianza creciente en torno a la potencialidad de la implementación de sistemas informáticos permitió que se incorporaran grandes cantidades de datos y se pudieran desarrollar cálculos que excedían la capacidad humana.

Más allá de los postulados teóricos de la Arqueología Procesual -y nuestro no tan próximo posicionamiento teórico- hemos de destacar que su esperanza en la tecnología y en la "cuantificación de los datos" es, quizá, un punto significativo de las trayectorias en las que han derivado nuestro campos de estudio.

El proyecto que hemos denominado **"Colorimetría Digital Argentina"** o **"CoDigAR"** pretende sintonizarse con las libertades del software libre,

- La libertad de identificar y solucionar desarrollos teóricos, adicionar nuevas funcionalidades y aplicaciones con fines específicos.
- La libertad de fomentar el trabajo colaborativo, dinámico, el intercambio de datos y procesamiento a diferentes niveles, en pos de un fin común.
- Libertad de contribuir en el estudio de la cultura local.
- Libertad de mostrar los resultados a la comunidad.

CoDigAR es un proyecto académico argentino que permite obtener más información sobre el **arte rupestre**, mediante el análisis de un tipo particular de rasgo: las **imagenes**, en particular aquellas manifestaciones gráficas de antiguas culturas, a través del uso de la **tecnología y herramientas libres** y mediante el trabajo en conjunto de dos campos científicos: -Arqueología e Ingeniería en Telecomunicaciones- de dos universidades nacionales, dotando así a los resultados de cuantificación y exactitud.

Se trata de **técnicas inéditas** de análisis y determinación cuantitativa de características de arte rupestre empleando como información cruda fotografías de las rocas en cuestión y haciendo uso emph{herramientas libres de tratamiento digital de imágenes} para la automatización del proceso.

##Objetivo

En el presente trabajo se busca compartir los principios generales que fundamentan el desarrollo de una técnica inédita hasta el momento relacionada con el estudio del arte rupestre, que se lleva adelante en forma conjunta e interdisciplinaria.


* * *

##Un poco de contexto

Como hemos mencionado en el acápite anterior, el proyecto se encuentra destinado al estudio de manifestaciones rupestres arqueológicas. Actualmente se conoce una amplia variedad de técnicas que se han utilizado en la antigüedad para lograr plasmar distinta clase de motivos en las rocas. Algunas de estas técnicas incluyen la utilización de pinturas y otras la remoción de material rocoso para lograr superficies en bajo y alto relieve, como ocurre en el caso de los grabados y picados, etc.

En algunos casos, los motivos plasmados en un mismo panel no corresponden a la misma época de ejecución, pudiendo distanciarse por cientos o hasta miles de años. Para su estudio se utiliza una gama bastante amplia de metodologías y técnicas que permiten, entre otros aspectos, asignarles una antigüedad o, al menos, un orden de ejecución.

Una de las vías más implementadas para lograr obtener una cronología relativa es el **estudio de las “pátinas”**, elemento en el que nos centraremos de aquí en adelante.

*Nota: Los estudios realizados hasta el momento se restringen al análisis de pátinas en surcos con técnicas de "picado plano" y "picado en surco".*

###¿Qué son las pátinas?, ¿cómo estudiarlas?
Las pátinas son el producto del paso del tiempo sobre los surcos de los grabados -o de las pinturas- que se confeccionan sobre la roca. En el momento de su confección, la superficie de los surcos de un picado, por ejemplo, presenta una coloración viva que proviene de la reciente exposición de la superficie rocosa.

Con el paso del tiempo, la coloración de los surcos se va oscureciendo de tal modo que la pátina se vuelve más “fuerte” mientras mayor sea la antigüedad del surco.  En el caso de las pinturas, el efecto es el mismo, a diferencia de que lo que se va “envejeciendo” es la superficie donde se distribuyen los pigmentos, otorgándoles una coloración más apagada y, en algunos casos, “perdiendo color”.

Con un análisis pormenorizado de las pátinas, en conjunción con otras técnicas, se puede llegar a conocer el orden en el cual los motivos han sido plasmados en el soporte, otorgándoles una cronología relativa, aplicable en la mayor parte de los casos, a la comparación de los motivos dentro del panel.

Entre las *dificultades del estudio* de pátinas se encuentra la necesidad de contar con un ojo entrenado, y con la dificultad de no poder cuantificarlo, ya que se trata de un análisis de percepción visual.
Ya que ela asignación cronológica de los motivos -absoluta o relativa- constituye una necesidad de primer orden para su entendimiento, planteamos la posiblidad de:

obtener una cuantificación para el análisis de las pátinas, en donde la apreciación de los colores pueda tener su contraparte en valores numéricos y gráficos, en un proceso que pretendemos sistematizar a traves de un software de código abierto. Con este objeto, se procede a compartir el principio de funcionamiento básico de la técnica colorimétrica que se encuentra en vías de desarrollo.

##Solución propuesta
Se propone, entonces, el desarrollo de una técnica basada en la **colorimetría digital** (para principios colorimétricos, véase: Ohta y Robertson 2006) a fin de lograr la **cuantificación** de los datos obtenidos a partir del análisis visual de los paneles.

La diferencia de coloración en las pátinas puede ser mensurable si a cada tipo de pátina se le asigna como identidad **los colores más representativos de las mismas**. Para ello se opta por confeccionar paletas cromáticas, implementando técnicas digitales.

Las paletas incluyen un conjunto de colores que se corresponden con los más representativos de cada una. La manera de confeccionarlos deberá ser analógica y digital (ya que el humano debe seleccionar el área en donde el ordenador debe tomar la muestra de colores). Es el ordenador el que debe confeccionar la paleta y determinar los colores más representativos de la muestra.

Estas paletas deben convertirse en valores numéricos basados en un sistema de ejes cartesianos donde quedan representados los valores de rojo, verde y azul que comprenda cada color (implementación de sistema de representaición RGB).

Así, para cada pátina, se tienen valores asignables a los límites cartesianos en los que se encuentra enmarcado cada conjunto de colores. Al tratarse de un sistema tridimensional (RGB), la valoración de los conjuntos tonales se realizará siguiendo estándares gráficos y, a futuro, volumétricos, posibilitando la comparación de muestras y su posible adscripción. 

Se procede a continuación a Demostrar el principio básico de funcionamiento de una técnica de colorimetría digital que permitiría obtener parámetros numéricos para la caracterización de las pátinas en arte rupestre. 

###Fases del procedimiento

- Determinar diferencias entre surcos de grabados, que permitan distinguir distintas pátinas.
- Obtener muestras de color representativas de cada pátina.
- Generar para cada muestra una paleta de colores representativa. 
- Con la información de dicha paleta, obtener los códigos RGB de cada uno de sus colores.
- Trasladar cada uno de los códigos a un eje de tres coordenadas, donde se representen los valores de cada canal, es decir: $$$[r;g;b] \rightarrow [x;y;z]$$$
	- Los puntos del mismo conjunto determinarán la existencia de un cuerpo irregular de 1, 2 o 3 dimensiones, que establecerá los límites del intervalo colorímetro que caracterizará a cierta pátina.
	- Se podrán representar cuantas pátinas sean necesarias.
	- Se podrá obtener muestras de surcos de pátina indiferenciada para establecer comparaciones con los conjuntos ya establecidos.

###Demostración de la viabilidad de la técnica

Para la demostración de este principio se procede a su aplicación en un caso de estudio. Se toma como objeto de estudio un panel de arte rupestre que se ubica en la localidad de Peñas Coloradas, en el departamento de Antofagasta de la Sierra, provincia de Catamarca.

Debido a cuestiones de extensión la demostración se enfoca de modo exclusivo a la aplicación de la técnica aquí descripta, demostrando la viabilidad de su aplicación.

El punto de partida se corresponde con una situación típica en la que se encuentra el investigador al momento de abordar el estudio de arte rupestre en el gabinete: el mismo dispone de la información que haya podido recolectar durante sus tareas de campo y uno de los pilares más sólidos en la documentación estará conformado por el registro fotográfico. Por lo que hemos de partir en nuestro análisis con la siguiente fotografía: 

![](https://github.com/brivadeneira/CoDigAR/blob/master/img/demo/ar.png?raw=true)
Arte rupestre - [Peñas Coloradas](https://es.wikiloc.com/wikiloc/view.do?id=1319853), dpto de Antofagasta de la Sierra, provincia de Catamarca, Argentina.

Es importante destacar que, a fines prácticos, hemos seleccionado una imagen que favorezca la simple detección de los motivos y en la que la que el procedimiento de muestreo resulte afable al proceso de demostración. Más adelante se analizarán algunos aspectos relacionados con los retos de muestreo en casos donde se presenten obstáculos de muestreo y riesgo de introducción de error.

###Procedimiento de muestreo

Sobre la imagen a trabajar, se seleccionaran áreas en las que se desee tomar muestras de color.  Para obtener una muestra representativa que nos permita obtener luego parámetros sólidos de comparación, procederemos a tomar muestra de la “matriz” del panel, es decir, un sector en donde la roca no ha sido tallada.

Luego tomaremos muestra de los surcos que deseemos comparar, en este caso, se han seleccionado dos representaciones: un camélido y un motivo serpentiforme. De aquellos, se ha dado predilección a sectores en los que el surco permitía una mejor ilustración de las cualidades de la pátina. 

Los sectores de muestreo se detallan gráficamente a continuación:

![](https://github.com/brivadeneira/CoDigAR/blob/master/img/demo/m0.png?raw=true) muestra 0, matriz (roca sin tallar).

![](https://github.com/brivadeneira/CoDigAR/blob/master/img/demo/m1.png?raw=true) muestra 1, sector del lomo del camélido.

![](https://github.com/brivadeneira/CoDigAR/blob/master/img/demo/m2.png?raw=true) muestra 2, sector del motivo serpentiforme.

El procedimiento de muestreo se realizó siguiendo varios parámetros de experimentación por ensayo/error. En primer lugar se consideró apropiado realizar un recorte de la imagen, siguiendo los contornos del surco, tal como se indica en las figuras amarillas para el caso de las muestras, luego fueron exportadas individualmente en formato *PNG* para prescindir del fondo de la imagen. Sin embargo, las herramientas web que fueron utilizadas en momentos posteriores, no admitían el formato *PNG*, por lo que se convirtió las imágenes a formato *JPG*.

Este formato incorpora el error del color blanco en el fondo, que en etapas posteriores podría alterar los valores del patrón de cada pátina. Por ello, se optó por realizar un “muestreo en caja”, que consiste en seleccionar, dentro de los sectores resaltados en amarillo, áreas en formato rectangular.

En uno de los casos se debió unir varias muestras para poder lograr un muestreo representativo de la gama que abarcaba cada surco. Esto se debe a otro impedimento técnico que presentan las herramientas aquí implementadas, relacionado con el tamaño en ppp (píxel por pulgada) que podían tolerarse para su tratamiento. El hecho de recortar varios sectores cuadrangulares del mismo surco no afecta en la consecución de los siguientes pasos, debido a que aquello que se buscará más adelante será obtener una medida de la riqueza de colores presentes en cada surco.

 Es importante destacar también, que la toma de muestras a simple vista no presenta grandes variaciones de color, hecho al que también contribuirá la presente técnica, debido a que un ordenador es capaz de muestrear a escala de píxeles, precisión que no posee la vista humana en la actualidad.

###Obtención de gama de colores

La fase siguiente al muestreo, será la obtención de una gama representativa de los colores de cada muestra. Para esto, es necesario destacar que resulta imposible utilizar herramientas tales como el cuentagotas de los editores gráficos, debido a que los valores obtenidos responden al orden del pixel, situación que no representa la amplia gama de tonalidades que puede darse dentro de un mismo surco. De hecho, los colorímetros RGB implementados actualmente toman, por lo general, muestras de a un color por vez, aspecto que impide su uso para arte rupestre.

Es importante destacar aquí que, incluso las características mineralógicas del soporte (la roca en donde se han ejecutado los motivos) pueden determinar la existencia de variaciones de color propias de la naturaleza de la roca. Sobre este abanico de posibles colores trabajaremos, intentando obtener una muestra de los valores mejor representados en cada imagen.

Para ello utilizaremos alguna herramienta que permita obtener “paletas” de colores a partir de una imagen con extensión *jpg*.  Hemos seleccionado una herramienta web de acceso libre y gratuito denominada [imgr](http://imgr.co/imgr.php) *(«Imgr - Image Color Tool» 2016)*.

El procedimiento resulta sencillo: se importan las imágenes desde el ordenador a la web y se le solicita un muestreo de los colores más representativos. Como resultado se obtiene una paleta, tal como se observa a continuación:

![](https://github.com/brivadeneira/CoDigAR/blob/master/img/cuancto/imgr.png?raw=true)
Ejemplo de obtención de paleta de colores a partir de una imagen. (muestra 1)

Los recursos brindados por esta herramienta web resultan útiles dado que: permite la exportación de la paleta en formato *ACO*, compatible con el software de Adobe, genera una paleta gráfica que puede duplicarse sólo a partir de una impresión de pantalla y brinda los valores de cada color obtenido en código hexagesimal.

Cable aclarar que imgr no admite formato *PNG* y obtiene muestras representativas de los colores de la imagen, por lo que no resulta conveniente implementar imágenes que contengan fondo blanco o de tamaño muy reducido.

Luego de procesar las muestras que necesitemos de manera individual, buscaremos la conversión de los códigos del color, procedimiento que veremos en el siguiente apartado.

###Transformación de código hexadecimal a RGB

La transformación de un sistema a otro puede realizarse fácilmente a través de un conversor online. En este caso hemos seleccionado otra web de acceso libre y gratuito denominada [rgbtohex](http://www.rgbtohex.net/hextorgb) *(«Hex to RGB» 2016)*.

Para la consecución de este paso hemos optado por confeccionar una tabla en donde conste por cada muestra:

- Los valores de color obtenidos a partir del generador de paletas (hexagesimal).
- Los valores obtenidos a partir de la conversión a RGB.

Se obtuvieron los siguientes datos:

|  MUESTRA  | HEXAGESIMAL |     RGB     |
|:---------:|:-----------:|:-----------:|
| MUESTRA 0 | 9E8B85      | 158.139.113 |
|           | E8E4E1      | 232.228.225 |
|           | 8E7D78      | 142.125.120 |
|           | B8A9A3      | 184.169.163 |
|           | AB9B94      | 171.155.148 |
|           | C4BAB5      | 196.186.181 |
| MUESTRA 1 | AA877E      | 170.135.126 |
|           | B99B90      | 185.155.144 |
|           | 937A76      | 147.122.118 |
|           | 7E6A68      | 126.106.104 |
|           | DEC9C3      | 222.201.195 |
|           | CFB8B2      | 207.184.178 |
|           | BEABA0      | 190.171.160 |
|           | EDE2DF      | 237.226.223 |
| MUESTRA 2 | 9A7D6B      | 154.125.107 |
|           | 906F5E      | 114.111.94  |
|           | A18C79      | 161.140.121 |

###La expresión gráfica de los parámetros colorimétricos
Hemos optado por la conversión de los valores de color al sistema *RGB*, debido a que las características del mismo permitirán la realización de este procedimiento.

Un código de color expresado en *RGB* expresa los contenidos de rojo, verde y azul que cada color posee para lograr su propia tonalidad. En este caso, por ejemplo, un código que enuncie 161.140.121 expresa que un único color comprende las siguientes proporciones de: rojo 161, verde 140 y 121 de azul.
Los valores de color en RGB adoptan parámetros que pueden abarcar el intervalo de [0;255], donde 0.0.0 implica el color negro y 255.255.255 implica el blanco absoluto.
Por esta razón, se deberá discriminar dentro de cada color, valores correspondientes a cada canal. El objetivo de ello será lograr posicionar en un sistema tridimensional cada uno de estos valores, según indiquen sus porcentajes de rojo, verde y azul.
Se le asignará a cada canal los siguientes ejes de modo arbitrario: rojo eje x, verde eje y, azul eje z.

Obtenemos la siguiente tabla:

|  MUESTRA  |  CODIGO RGB | EJE TRI | DIMEN | SIONAL |
|:---------:|:-----------:|:-------:|:-----:|:------:|
|           |             |   X(R)  |  Y(G) |  Z(B)  |
| MUESTRA 0 | 158.139.113 |   158   |  139  |   113  |
|           | 232.228.225 |   232   |  228  |   225  |
|           | 142.125.120 |   142   |  125  |   120  |
|           | 184.169.163 |   184   |  169  |   163  |
|           | 171.155.148 |   171   |  155  |   148  |
|           | 196.186.181 |   196   |  186  |   181  |
| MUESTRA 1 | 170.135.126 |   170   |  135  |   126  |
|           | 185.155.144 |   185   |  155  |   144  |
|           | 147.122.118 |   147   |  122  |   118  |
|           | 126.106.104 |   126   |  106  |   104  |
|           | 222.201.195 |   222   |  201  |   195  |
|           | 207.184.178 |   207   |  184  |   178  |
|           | 190.171.160 |   190   |  171  |   160  |
|           | 237.226.223 |   237   |  226  |   223  |
| MUESTRA 2 | 154.125.107 |   154   |  125  |   107  |
|           |  114.111.94 |   114   |  111  |   94   |
|           | 161.140.121 |   161   |  140  |   121  |

Luego, con la ayuda de un software que permita graficar en tres dimensiones, ingresaremos cada valor de color, determinando sus coordenadas centrales en base a los parámetros descriptos en nuestro cuadro. Será necesario diferenciar entre los conjuntos muestreados, para obtener una ilustración gráfica de la distribución de cada muestra.

El software que permite lo anterior es [Blender](https://www.blender.org) (software libre), el que se dedica al modelado y animación en 3D *(Blender Foundation 2016)*. Sin embargo, dejamos abierta la posibilidad de utilizar cualquier software alternativo que permita )la representación tridimensional de valores numéricos.

A continuación ilustramos la disposición de cada conjunto, donde los puntos en rojo ilustran los valores de la muestra 0, en verde la muestra 1 y en azul la muestra 2.
*(Nota: no debe confundirse en esta imagen los colores de los puntos con el codigo RGB. Cada color representa una muestra colorimétrica distinta.)*

###Análisis de los resultados

A continuación se puede observar los gráficos obtenidos a partir de los valores numéricos de cada conjunto muestral. Así, en diferentes colores tenemos la representación gráfica de las tres muestras obtenidas, lo que nos permite otro tipo de representación de los resultados, tal como se puede apreciar a continuación:

![](https://github.com/brivadeneira/CoDigAR/blob/master/img/cuancto/rgb3D.png?raw=true)
Gráfico en tres dimensiones sobre la información en RGB de las muestras. Rojo: muestra 0; Verde: muestra 1; Azul: muestra 2. *Blender*

![](https://github.com/brivadeneira/CoDigAR/blob/master/img/cuancto/rgb3D2.png?raw=true)
Gráfico en tres dimensiones sobre la información en RGB de las muestras. *Blender*

Al tomar en cuenta la distribución de cada conjunto, se puede observar que la extensión de los mismos podría expresarse en términos volumétricos, procedimiento que no expresaremos en el presente informe por cuestiones de extensión.

La técnica implementada permite:

- Obtener una muestra representativa no de un color predominante, sino de una gama de colores que es capaz de representar los valores de color de cada pátina: esto permite sortear la inviabilidad de utilizar un cuentagotas para tomar una muestra de color por cada elemento a comparar. Por otro lado, la detección digital de los colores más representativos permite obtener a nivel estadístico valores realmente representativos de la muestra, procedimiento que resulta de gran dificultad para realizar a escala humana.
- La posibilidad de asignar valores numéricos a los conjuntos permite:
  - Su cuantificación: herramienta de la cual no se disponía actualmente.
  - Su valoración: posibilita la detección de una mayor variedad de colores que no pueden distinguirse a partir de la vista humana.
  - Permite la contrastación o la detección de pátinas que no pueden determinarse a simple vista.
- La representación gráfica de los conjuntos:
  - Permite analizar conjuntos de parámetros que conforman una unidad de muestreo, brindando facilidades para quienes deseen prescindir del enfoque numérico.
  - El establecimiento de los valores liminares de cada conjunto, permite además, caracterizar los parámetros en los que se enmarca cada muestra, por lo que podría plantearse que es viable la interpolación entre los elementos de cada conjunto para plantear posibles variaciones de muestras que luego puedan ingresarse al estudio comparativo. Por ejemplo: un valor que se enmarque dentro de los parámetros liminares de la muestra nro 1, por los principios de interpolación podría ser considerado como perteneciente al mismo, y por ende, esto permitiría la adscripción de la muestra en base al conjunto referencial.
  - Es importante destacar que la representación volumétrica de las muestras responde a la organización original de los parámetros de RGB, lo cual permite su compatibilidad para futuras aplicaciones con otros sistemas de procesamiento información.

###Elementos a tener en cuenta: errores y medidas de control.

Algunos aspectos deberán tomarse en cuenta para, a futuro, disponer los pasos necesarios dentro del protocolo de muestreo, que permita eliminar ciertos errores sistemáticos relacionados con la naturaleza del material gráfico implementado, y con las herramientas digitales implementadas.
Entre ellos se puede destacar:

- **Tamaño de la muestra:** debe tomarse las dimensiones y la resolución básica tolerada por los instrumentos de medición.
- **Luz y sombra en la fotografía:** pueden generar diferencias tonales en un surco que presente la misma pátina.
- **Tipo de selección: ** debería pensarse a futuro la posibilidad de abarcar la mayor superficie posible del surco en los muestreos.
- ** Nivel de representatividad de la muestra: **se precisará de la agudeza visual del operador y de su suspicacia a la hora de seleccionar sectores que aporten las muestras “de mayor pureza posible”.
- ** ¿Qué hacer cuando las muestras no tienen la misma riqueza tonal?  ** Esto se puede observar en la muestra 2, para la cual se obtuvo un $40-50$ por ciento menos cantidad de valores de color con respecto a las muestra 0 y 1. Deberá analizarse a posteriori cuál será el procedimiento a seguir en estos casos, preguntándonos si la falta de variabilidad puede ser considerada como una marca identitaria de la muestra o si se precisa seguir otro protocolo de muestreo para obtener mayor cantidad de valores tonales.

###Limitaciones

Dentro de las limitaciones del método, la primera y fundamental remite a la accesibilidad de los recursos, de la información y la formación para realizar este tipo de tratamiento de imágenes. La implementación de varios recursos informáticos, tales como conversores de código de color, o software de tratamiento tridimensional de las imágenes exige del usuario una cantidad considerable de recursos que restringe su aplicación y libre acceso.
Por ende, los principios aquí demostrados serán incorporados en un software de distribución libre y gratuita denominago CoDigAr, que responde a las cuatro libertades planteadas desde la filosofía del software libre, mencionadas al inicio del trabajo.

##Proyección

La visión de CoDigAR contempla el trabajo colaborativo de voluntarios de diferentes campos de estudio para el perfeccionamiento y evolución de la técnica colorimétrica y el desarrollo de un software libre que permita la automatización de dicho proceso y la solución de cuestiones como las mencionadas en la sección Limitaciones.

Además se proyecta en el futuro de CoDigAR la implementación de un portal web libre que le permita el acceso a la información referente a los resultados del análisis de arte rupestre en Argentina, a la comunidad, así como su contribución con imagenes de las mismas.

>*"No hables de cómo será el futuro, lucha por un buen futuro", Richard Stallman.*