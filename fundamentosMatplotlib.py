#Importar numpy
import numpy as np
# Importar el módulo pyplot con el alias plt
import matplotlib.pyplot as plt
# Crear la figura y los ejes
fig, ax = plt.subplots()
# Dibujar puntos
ax.scatter(x = [1, 2, 3], y = [3, 2, 1])
# Guardar el gráfico en formato png
#plt.savefig('diagrama-dispersion.png')
# Mostrar el gráfico
plt.show()
#############################
########Diagrama de dispersion de puntos
#############################
#para el diagrama de dispercion de puntos se uriliza la funcion scatter(x,y) a esta se le deve pasar dos 
# arreglos o coordenas para que pueda agregar un punto en el mapa 
fig, ax = plt.subplots()
ax.scatter([1, 2, 3, 4], [1, 2, 0, 0.5])
plt.show()
#############################################
#######Diagramas de lineas 
#############################################
#Para el diagrama de lines se utiliza la funcion plot(x,y) y a esta tambien se le pasan dos arreglos o 
# coordenas para los picos de la linea 
fig, ax = plt.subplots()
ax.plot([1, 2, 3, 4], [1, 2, 0, 0.5])
plt.show()
#############################################
#######DIAGRAMAS DE AREA
#############################################
#Este tipo de graficos dibuja el area bajo los polígonos con los vertices dados por las coordenadas X e Y utilizando la funcion fill_between(x, y)
fig, ax = plt.subplots()
ax.fill_between([1, 2, 3, 4], [1, 2, 0, 0.5])
plt.show()
#############################################
######Diagrama de Barras verticales 
#############################################
#Para graficar esto se utiliza la funcion bar(x,y)
fig, ax = plt.subplots()
ax.bar([1, 2, 3], [3, 2, 1])
plt.show()
#############################################
######Diagrama de Barras Horizontales 
#############################################
#Para graficar esto se utiliza la funcion barh(x,y)
fig, ax = plt.subplots()
ax.barh([1, 2, 3], [3, 2, 1])
plt.show()
#############################################
######Histogramas
#############################################
#hist(x, bins)  Este dibuja un histograma resultante con las frecuencias resultantes de agrupar los datos de la lista x en las clases definidas en bins
fig, ax = plt.subplots()
###para el histograma siempre se utiliza la funcion np.random.normal(loc, scale,size)
##loc es la ubicacion del punto medio del pico del histograma 
## scale es la desbiacion a los costados 
## size es el tamaño de y la forma de la salida
x = np.random.normal(5, 1.5, size=1000)
ax.hist(x, np.arange(0, 11))
plt.show()
#############################################
######Diagrama de porcioens o Diagrama Circular
#############################################
## Este dibuja un idagrama de los sectores con las frecuencia de la lista x con la funcion pie(x)
fig, ax = plt.subplots()
ax.pie([5, 4, 3, 2, 1])
plt.show()
#############################################
######Diagrama de Belas Japonesas
#############################################
##Este grafico dibuja una caja con bigotes para abajo y para arriba de acuerdo a los datos de la lista x con la funcion boxplot(x)
fig, ax = plt.subplots()
ax.boxplot([1, 2, 1, 2, 3, 4, 3, 3, 5, 7])
plt.show()
#############################################
######Diagrama de Violin
#############################################
#Dibuja un diagrama de Violin con los datos de x, para esto se utiliza la funcion violinplot(x)
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.violinplot([1, 2, 1, 2, 3, 4, 3, 3, 5, 7])
plt.show()
#############################################
######Diagrama de Contorno 
#############################################
#contourf(x, y, z): Dibuja un diagrama de contorno con las curvas de nivel de la superficie dada por los #puntos con las coordenadas de las listas x, y y z en los ejes X, Y y Z respectivamente
fig, ax = plt.subplots()
x = np.linspace(-3.0, 3.0, 100)
y = np.linspace(-3.0, 3.0, 100)
x, y = np.meshgrid(x, y)
z = np.sqrt(x**2 + 2*y**2)
ax.contourf(x, y, z)
plt.show()
#############################################
######Mapa de Colres
#############################################
##imshow(x): Dibuja un mapa de color a partir de una matriz (array bidimensiona)
fig, ax = plt.subplots()
x = np.random.random((16, 16))
ax.imshow(x)
plt.show()
###hist2d(x, y): Dibuja un mapa de color que simula un histograma bidimensional, donde los colores de los 
# cuadrados dependen de las frecuencias de las clases de la muestra dada por las listas x e y
fig, ax = plt.subplots()
x, y = np.random.multivariate_normal(mean=[0.0, 0.0], cov=[[1.0, 0.4], [0.4, 0.5]], size=1000).T
ax.hist2d(x, y)
plt.show()
##########################################################################################################
##########################################################################################################
######################################CAMBIAR ASPECTO DE LOS GRAFICOS#####################################
##########################################################################################################
##########################################################################################################
##COLORES>>>para esto solo debes agregar el sentencia color="nombre_color"
fig, ax = plt.subplots()
dias = ['L', 'M', 'X', 'J', 'V', 'S', 'D']
temperaturas = {'Madrid':[28.5, 30.5, 31, 30, 28, 27.5, 30.5], 'Barcelona':[24.5, 25.5, 26.5, 25, 26.5, 24.5, 25]}
ax.plot(dias, temperaturas['Madrid'], color = 'tab:purple')
ax.plot(dias, temperaturas['Barcelona'], color = 'lime')
plt.show()
#####Marcadores>> estos se utilizan mas en las lineas para saber en donde estaba la marca segun los datos 
# del los arreglos y se aãnde utilizando marker = "simbolo"
fig, ax = plt.subplots()
dias = ['L', 'M', 'X', 'J', 'V', 'S', 'D']
temperaturas = {'Madrid':[28.5, 30.5, 31, 30, 28, 27.5, 30.5], 'Barcelona':[24.5, 25.5, 26.5, 25, 26.5, 24.5, 25]}
ax.plot(dias, temperaturas['Madrid'], marker = '^')
ax.plot(dias, temperaturas['Barcelona'], marker = 'o')
plt.show()
####Líneas>>>>>Las lineas se puede cambiar tambien, como para que sean punteadas por ejemplo con la sentencia linestyle = nombre-estilo
fig, ax = plt.subplots()
dias = ['L', 'M', 'X', 'J', 'V', 'S', 'D']
temperaturas = {'Madrid':[28.5, 30.5, 31, 30, 28, 27.5, 30.5], 'Barcelona':[24.5, 25.5, 26.5, 25, 26.5, 24.5, 25]}
ax.plot(dias, temperaturas['Madrid'], linestyle = 'dashed')
ax.plot(dias, temperaturas['Barcelona'], linestyle = 'dotted')
plt.show()
#######################################
##Añadir Titulos 
#Para el titulo se utiliza la sentencia set_title(titulo, loc=alineacion, fontdict=fuente)
#la aliniacion puede ser left, center o right
##<<<fontdict>>. indica mediante un diccionario las características de la fuente (la el tamaño fontisize, el grosor fontweight o el color color).
fig, ax = plt.subplots()
dias = ['L', 'M', 'X', 'J', 'V', 'S', 'D']
temperaturas = {'Madrid':[28.5, 30.5, 31, 30, 28, 27.5, 30.5], 'Barcelona':[24.5, 25.5, 26.5, 25, 26.5, 24.5, 25]}
ax.plot(dias, temperaturas['Madrid'])
ax.plot(dias, temperaturas['Barcelona'])
ax.set_title('Evolución de la temperatura diaria', loc = "left", fontdict = {'fontsize':14, 'fontweight':'bold', 'color':'tab:blue'})
plt.show()
########################################################################
#Para cambiar el aspecto de los ejes se suelen utilizar los siguientes métodos:
#ax.set_xlabel(titulo) : Añade un título con el contenido de la cadena titulo al eje x de ax. Se puede #personalizar la alineación y la fuente con los mismos parámetros que para el título principal.
#ax.set_ylabel(titulo) : Añade un título con el contenido de la cadena titulo al eje y de ax. Se puede #personalizar la alineación y la fuente con los mismos parámetros que para el título principal.
#ax.set_xlim([limite-inferior, limite-superior]) : Establece los límites que se muestran en el eje x de ax.
#ax.set_ylim([limite-inferior, limite-superior]) : Establece los límites que se muestran en el eje y de ax.
#ax.set_xticks(marcas) : Dibuja marcas en el eje x de ax en las posiciones indicadas en la lista marcas.
#ax.set_yticks(marcas) : Dibuja marcas en el eje y de ax en las posiciones indicadas en la lista marcas.
#ax.set_xscale(escala) : Establece la escala del eje x de ax, donde el parámetro escala puede ser 'linear' #(lineal) o 'log' (logarítmica).
#ax.set_yscale(escala) : Establece la escala del eje y de ax, donde el parámetro escala puede ser 'linear' #(lineal) o 'log' (logarítmica).
fig, ax = plt.subplots()
dias = ['L', 'M', 'X', 'J', 'V', 'S', 'D']
temperaturas = {'Madrid':[28.5, 30.5, 31, 30, 28, 27.5, 30.5], 'Barcelona':[24.5, 25.5, 26.5, 25, 26.5, 24.5, 25]}
ax.plot(dias, temperaturas['Madrid'])
ax.plot(dias, temperaturas['Barcelona'])
ax.set_xlabel("Días", fontdict = {'fontsize':14, 'fontweight':'bold', 'color':'tab:blue'})
ax.set_ylabel("Temperatura ºC")
ax.set_ylim([20,35])
ax.set_yticks(range(20, 35))
plt.show()
###########################################################
##############Leyendas
###########################################################
##Para agregar Leyendas a un grafico se utiliza el siguiente metodo ax.legend(leyendas, loc = posición) 
#las posiciones de LOC puede ser 'upper left' (arriba izquierda), 'upper center' (arriba centro), 'upper 
# right' (arriba derecha), 'center left' (centro izquierda), 'center' (centro), 'center right' (centro 
# derecha), 'lower left' (abajo izquierda), 'lower center' (abajo centro), 'lower right' (abajo derecha)
fig, ax = plt.subplots()
dias = ['L', 'M', 'X', 'J', 'V', 'S', 'D']
temperaturas = {'Madrid':[28.5, 30.5, 31, 30, 28, 27.5, 30.5], 'Barcelona':[24.5, 25.5, 26.5, 25, 26.5, 24.5, 25]}
ax.plot(dias, temperaturas['Madrid'], label = 'Madrid')
ax.plot(dias, temperaturas['Barcelona'], label = 'Barcelona')
ax.legend(loc = 'upper right')
plt.show()
##################################################################################
##########################INTEGRACION CON PANDAS##################################
##################################################################################
##df.plot(kind=tipo, x=columnax, y=columnay, ax=ejes) : Dibuja un diagrama del tipo indicado por el 
# parámetro kind en los ejes indicados en el parámetro ax, representando en el eje x la columna del 
# parámetro x y en el eje y la columna del parámetro y. El parámetro kind puede tomar como argumentos 
# 'line' (lineas), 'scatter' (puntos), 'bar' (barras verticales), 'barh' (barras horizontales), 'hist' 
# (histograma), 'box' (cajas), 'density' (densidad), 'area' (area) o 'pie' (sectores). Es posible pasar 
# otros parámetros para indicar el color, el marcador o el estilo de línea como se vió en los apartados anteriores.
import pandas as pd 
df = pd.DataFrame({'Días':['L', 'M', 'X', 'J', 'V', 'S', 'D'], 
                    'Madrid':[28.5, 30.5, 31, 30, 28, 27.5, 30.5], 
                    'Barcelona':[24.5, 25.5, 26.5, 25, 26.5, 24.5, 25]})
fig, ax = plt.subplots()
df.plot(x = 'Días', y = 'Madrid', ax = ax)
df.plot(x = 'Días', y = 'Barcelona', ax = ax)
plt.show()
##Si no se indican los parámetros x e y se representa el índice de las filas en el eje x y una serie por 
# cada columna del Dataframe. Las columnas no numéricas se ignoran.
df = pd.DataFrame({'Días':['L', 'M', 'X', 'J', 'V', 'S', 'D'], 
                    'Madrid':[28.5, 30.5, 31, 30, 28, 27.5, 30.5], 
                    'Barcelona':[24.5, 25.5, 26.5, 25, 26.5, 24.5, 25]})
df = df.set_index('Días') 
fig, ax = plt.subplots()
df.plot(ax = ax)
plt.show()