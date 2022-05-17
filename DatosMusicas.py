from turtle import title
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dfCanciones = pd.read_csv(
'songs_normalize.csv', sep=',', decimal='.')
#print(dfCanciones.head())
##Obtenemos las canciones mas populares de cada año
##seleccionamos solo las filas que contienen la cancion mas popular
cancionesMasPopularesPorAno = dfCanciones.iloc[dfCanciones.groupby('year').agg(max_ = ('popularity', lambda data: data.idxmax())).max_]
fig, ax = plt.subplots()
#Puntos que seran graficados en el diagrama 
ax.plot(cancionesMasPopularesPorAno['year'],cancionesMasPopularesPorAno['popularity'], marker = 'o')
##Se le da un titulo al Grafico 
ax.set_title('Canciones Mas Populares Anualmente', loc = "left", fontdict = {'fontsize':14, 'fontweight':'bold', 'color':'tab:blue'})
##Etiqueta para el eje x
ax.set_xlabel('Año', loc = "center", fontdict = {'fontsize':14, 'fontweight':'bold', 'color':'tab:blue'})
##Etiqueta para el eje y
ax.set_ylabel('Popularidad', loc = "center", fontdict = {'fontsize':14, 'fontweight':'bold', 'color':'tab:blue'})
#splt.show()
fig, ax = plt.subplots()
explicitos = dfCanciones['explicit'].value_counts().sort_index()
ax.pie(explicitos,labels=["False", "True"], colors=["red","green"],autopct='%1.2f%%')
plt.title("Porcentaje de Contenidos Explicitos")
plt.show()