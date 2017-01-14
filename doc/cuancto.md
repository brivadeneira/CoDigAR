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

CoDigAR es un proyecto académico argentino que permite obtener más información sobre el **arte rupestre**, mediante el análisis de un tipo particular de rasgo: las **imagenes**, especial de aquellas manifestaciones gráficas de antiguas culturas, a través del uso de la **tecnología y herramientas libres** y mediante el trabajo en conjunto de dos campos científicos: -Arqueología e Ingeniería en Telecomunicaciones- de dos universidades nacionales, dotando así a los resultados de cuantificación y exactitud.

Se trata de **técnicas inéditas** de análisis y determinación cuantitativa de características de arte rupestre empleando como información cruda fotografías de las rocas en cuestión y haciendo uso emph{herramientas libres de tratamiento digital de imágenes} para la automatización del proceso.

##Objetivo

En el presente trabajo se busca compartir la versión 2.0 de la técnica, que incluye la incorporación de herramientas estadísticas, de teoría de conjuntos y fundamentos colorimétricos.


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

En la **versión 1.0** de CuanCTo, se planteó que la diferencia de coloración en las pátinas puede ser mensurable si a cada tipo de pátina se le asigna como identidad los colores más representativos de las mismas, para lo que se optó por confeccionar paletas cromáticas, implementando técnicas digitales, que luego podrían ser representadas en espacios de color que pudieran pudieran representar gráfica y numéricamente de los valores de color de cada muestra. 

La **versión 2.0** plantea un refinamiento del principio, que incluye las nociones anteriores y simultáneamente permite ampliar los alcances de la técnica.

Se detalla en el siguiente cuadro las diferencias y similitudes entre las dos versiones:

| Versión 1.0 | Versión 2.0 |
|--------|--------|
|1-Sobre una imagen se determinan áreas de muestreo. | Idem|
|2-Estas áreas son sometidas a herramientas que generan paletas cromáticas de los colores más representativos de la muestra. | Idem|
|3-Con los valores de color obtenidos se confecciona un cuadro de doble entrada, detallando los valores de RGB de cada muestra.|Idem|
| 4-Se grafican dichos valores de RGB en ejes coordenados x,y,z correspondientemente.  | Entre los puntos 3, 4 y 5 de la columna contigua se realizaron modificaciones y se incluyeron variables, que serán descriptas en el siguiente cuadro. 
| 5- Se determinam áreas ocupadas por los valores de cada muestra que permiten comparar gráficamente los colores representativos de cada muestra. |

Innovaciones de la version 2.0

| Denominación | Aplicación |
|--------|--------|
|Asignación de acrónimos| A fin de lograr documentar con mayor efectividad la técnica y lograr estandarizar los elementos y fases del proceso.
|Analisis estadístico| Descripción de conjuntos muestrales. Analisis predictivo para comparación de muestras. Niveles de certeza.
|Teoría de conjuntos| Correspondencia de conjuntos tonales. Niveles de certeza.
|Teoría colorimétrica| Implementación de espacios de color. Interpolación. Niveles de certeza. 


###Fases del procedimiento

**1. SELECCION DEL ÁREA DE MUESTREO (procedimiento manual)**
- Determinar diferencias entre surcos de grabados, que permitan distinguir distintas pátinas.
- Obtener muestras de color representativas de los conjuntos tonales deseados  (pátina, roca sin tallar, etc).
    
**2. GENERACION DE MUESTRAS DE ORIGEN (mo)**
- Los conjuntos muestreados constituirán "muestras de origen" con un ID único. Ejemplo. Muestra 1 ==> mo1
- Cada "mo" contrendrá valores de tipo "identitario". Esta variable comprende la totalidad de los colores de la muestra (en código RGB), junto a sus frecuencias relativas.

**3. METODO COMPARATIVO DE CONJUNTOS TONALES**

* DETERMINACION DE MUESTRAS DEL TIPO "PATRÓN" Y "COMPARATIVA": 
 - *Generación de "muestras patrón" (mp)*: se seleccionará una muestra de origen para que constituya un modelo sobre el cual comparar otro conjunto.  Se procederá a interpolar los valores identitarios de la mo. Por ende, los  una muestra patrón comprenderá los valores identitarios de la "mo" seleccionada y los valores que resulten de la interpolación de los mismos.
 - *Generación de "muestras comparativas (mc)*: se seleccionará una muestra de origen para comparar con una muestra patrón. Durante el procedimiento de comparación, la primera será denominada "muestra comparativa".

* NIVELES DE CERTEZA
Los niveles de certeza permiten determinar si existe una correspondencia tonal entre conjuntos y cuantificar aquella relación. Existen dos parámetros a determinar:

 - *Certeza de aproximación de  color*: determina qué tanto se aproximan los valores tonales de la muestra comparativa a los valores identitarios de la muestra patrón. Responde a la pregunta ¿Cuánta similitud tonal hay entre las muestras comparadas?
 - *Certeza de correspondencia*:  determina el porcentaje de individuos de la muestra comparativa que se corresponde colorimetricamente con la muestra patrón. Responde a la pregunta ¿Cuántos elementos coinciden?

**4. PRESENTACIÓN GRÁFICO-NUMERICA DE RESULTADOS**
- Se postula la necesidad de generar un documento exportable a partir del cual el usuario pueda analizar y cuantificar los valores obtenidos para su investigación. Las características de este documento se encuentran en vías de investigacion debido a que se plantea la necesidad de adaptar los valores cuantitativos a las necesidades y a los recursos del usuario, para lograr expresar con claridad los resultados obtenidos sin por ello generar una pérdida de información potencial.
- Se pretende, además lo siguiente:
	- Los puntos del mismo conjunto determinarán la existencia de un cuerpo irregular de 1, 2 o 3 dimensiones, que establecerá los límites del intervalo colorímetro que caracterizará a cierta pátina.
	- Se podrán representar cuantas muestras sean necesarias.
	- Se podrá obtener muestras de surcos de pátina indiferenciada para establecer comparaciones con los conjuntos ya establecidos.

###CuanCTo v2.0: Desarrollo teórico de la técnica
A continuación se desarrolla en profundidad 


###Procedimiento de muestreo



###Obtención de gama de colores


###Transformación de código hexadecimal a RGB


###Análisis de los resultados



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