from turtle import title, width
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
#plt.show()
#pocentaje de canciones que tienen contenido explicitos
#para estos solo dividimos la columna explicit endos grupos uno es True y False
explicitos = dfCanciones['explicit'].value_counts().sort_index()
fig, ax = plt.subplots()
##la sentencias autopct='%1.2f%%' es para mostrar el porcentaje de las divisiones en el grafico
ax.pie(explicitos,labels=["No Contiene", "Contiene"], colors=["red","green"],autopct='%1.2f%%', explode = [0.02,0.02])
plt.title("Porcentaje de Contenidos Explicitos")
#plt.show()
##Modalidad de la pista (mayor o menor)
modo = dfCanciones['mode'].value_counts().sort_index()
fig, ax = plt.subplots()
##la sentencias autopct='%1.2f%%' es para mostrar el porcentaje de las divisiones en el grafico
ax.pie(modo,labels=["Menor", "Mayor"], colors=["yellow","blue"],autopct='%1.2f%%', explode = [0.02,0.02])
plt.title("Modalidad de las canciones")
#plt.show()

#Canciones por Año 
#optenemos la cantidad de canciones que hay en un mismo año 
cancionesPorAno = pd.DataFrame(dfCanciones['year'].value_counts().sort_index())
#realizamos el grafico con los datos que teniamos
cancionesPorAno.plot(kind = 'bar', 
    width=0.9,
    xlabel = "Años",
    ylabel = "Cantidad de Canciones")
#plt.show()

ArtistasConMasCanaciones =pd.DataFrame(dfCanciones['artist'].value_counts().head(10))
ArtistasConMasCanaciones.plot(kind="bar",
    title= "Top 10 Artistas con mas Canciones",
    xlabel="Artistas",
    ylabel="Canciones")
#plt.show()
#print(ArtistasConMasCanaciones)

##Dansabilidad
#dfCanciones.iloc[dfCanciones.groupby('year').agg(max_ = ('popularity', lambda data: data.idxmax())).max_]
dansabilidad = dfCanciones.iloc[dfCanciones.groupby('song').agg(max_ = ('danceability', lambda data: data.idxmax())).max_].head(10)
fig, ax = plt.subplots()
ax.bar(dansabilidad['song'],dansabilidad['danceability'])
plt.title("Top 10 Canciones mas Dansables")
plt.xticks(rotation = 90)
#plt.show()
##Histograma de que tan energica es una cancion 
fig, ax = plt.subplots()
ax.hist(dfCanciones['energy'], 
    bins=20,
    width = 0.06)
plt.show()
#print(energia)