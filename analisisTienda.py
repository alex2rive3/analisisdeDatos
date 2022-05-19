from matplotlib import legend
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pymysql import DatabaseError

dfTienda = pd.read_csv('dataset\salesMarkets.csv', sep=',', decimal='.')
#print(dfTienda)
#Realizamos la cuenta de cuantas sucursales hay de cada nivel (A,B,C)
sucursales = dfTienda['Branch'].value_counts().sort_index()
fig, ax = plt.subplots()
#mostramos la Informacionen en un grafico de Pastel
ax.pie(sucursales, labels=["A", "B", "C"], autopct="%1.2f%%", explode = [0.02,0.02,0.02])
ax.legend(loc = 'upper right')
plt.title("Niveles de Sucursales en total")
#plt.show()
#Recuperamos los datos de cauntas tiendas hay en cada ciudad 
ubicacionDeLasTiendas = pd.DataFrame(dfTienda['City'].value_counts())
#Graficamos en un grafico tipo psatel los resultados 
#para realizar el grafico de pastel de esta manera importante no olvidar la sentencia <<<<subplots=True>>>>
ubicacionDeLasTiendas.plot(kind='pie',subplots=True,autopct="%1.2f%%", explode = [0.02,0.02,0.02], ylabel="")
plt.title("Ciudades en las que estan ubicadas las sucursales")
#plt.show()
##creamos una nueva hoja para dibujar
fig, ax =plt.subplots()
#seleccionamos y contamos los tipos de Clientes y mostramos en un grafico tipo pastel
tiposDeClientes = dfTienda['Customer type'].value_counts().plot(kind='pie',subplots=True,autopct="%1.2f%%", explode = [0.02,0.02], ylabel="")
plt.title("Tipos de Clientes")
#plt.legend(loc = 'upper right')
##plt.show() 
##creamos una nueva hoja para dibujar
fig, ax =plt.subplots()
#Obtenemos el Genero de nuestros compradores y lo reflejamos en un grafico pastel para que sea mas facil su comprencion
generoDeLosClientes = dfTienda['Gender'].value_counts().plot(kind='pie',subplots=True,autopct="%1.2f%%", explode = [0.02,0.02], ylabel="")
plt.title("Generos de los Compradores")
#plt.show()
##creamos una nueva hoja para dibujar
fig, ax =plt.subplots()
##Obtemdremos toda la linea de productos 
linesDeProductos = dfTienda['Product line'].value_counts().plot(kind='pie',subplots=True,autopct="%1.2f%%", ylabel="")
plt.title("Lineas de Productos")
#plt.show()
##creamos una nueva hoja para dibujar
fig, ax =plt.subplots()
#Con esto sabremos la cantidad la cantidad de productos que compran los clientes
ax.hist(dfTienda['Quantity'],
    bins = 10)
plt.title("Cantidad de Productos que LLevan los Clientes")
plt.xlabel("Cantidad De Productos")
plt.ylabel("Cantidad De Clientes")
#plt.show()
##creamos una nueva hoja para dibujar
fig, ax =plt.subplots()
#Creamos un Histograma de todos los precios unitarios de todos los productos de la tienda
ax.hist(dfTienda['Unit price'],
    bins = 80)
plt.title("Precio unitario de los productos")
plt.xlabel("Precios Unitarios")
plt.ylabel("Cantidad de Productos ")
#plt.show()
##creamos una nueva hoja para dibujar
fig, ax =plt.subplots()
##Cuanto pagan los clientes en impuestos por sus compras que son 5% del valor total 
ax.hist(dfTienda['Total'],
    bins = 40)
plt.title("Cuanto de impuestos Pagan los Compradores")
plt.xlabel("Monto del Impuesto")
plt.ylabel("Cantidad de Clientes ")
#plt.show()
##creamos una nueva hoja para dibujar
fig, ax =plt.subplots()
##Histogrma de cuantas personas compran diariamente en nuestras tiendas
ax.hist(dfTienda['Date'],
    bins = 90)
plt.title("Cuantos Compradores pasan por nuestras tiendas")
plt.xlabel("Fechas")
plt.ylabel("Cantidad de Clientes")
plt.xticks(rotation = 90)
plt.show()
##creamos una nueva hoja para dibujar
fig, ax =plt.subplots()
ax.hist(dfTienda['Time'],
    bins=50)
plt.title("Tiempo de Compra")
plt.xlabel("Tiempo de demora")
plt.ylabel("Cantidad de Compradores")
plt.xticks(rotation = 90)
#plt.show()