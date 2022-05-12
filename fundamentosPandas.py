import pandas as pd
import numpy as np
from math import log
#Clase de Objeto ""SEREIE"" son oobjetos similares a los arreglos en Numpy, son homogeneas 
# es decir que todos sus elementos deben ser de tipos iguales y de tamaño inmutable 
##pd.Series(data= lista, index=indices, dtype= tipo de datos )
series = pd.Series(data=['Matemáticas', 'Historia', 'Economía', 'Programación'],index=[6.0, 4.5, 8.5, 9.5])
print(series)
#Creacion de series por medio de Diccionarios 
series = pd.Series({'Matemáticas': 6.0,  'Economía': 4.5, 'Programación': 8.5})
print(series)
series1 = pd.Series(np.arange(6))
###Atributos de una serie 
#Size devuelve la cantida de elementos que contiene la serie
print(series1.size)
#Index Devuelve una lista con los nombres de las filas del DataFrame
print(series.index)
#dtype devuelve el tipo de datos de la serie 
print(series1.dtype)
##########################
##ACCESO A LOS ELEMENTOS DE UNA SERIE 
##########################
#El acceso se puede realizar por Posicion al igual que un array 
print(series1[0:2])
#Como tampien el acceso puede ser por medio de un Indice o nombre 
print(series['Economía'])
####################################
##RESUMEN DESCRIPTIVO DE UNA SERIE
####################################
##//Count()\\devuelve el numero de elementos diferentes a nulo y NaN en la serie 
print(series1.count())
##//sum()\\ devuelve la suma de todos los elementos si son de tipo int o float, si es str lo concatena 
print(series1.sum())
##//cumsum()\\ devuelve una serie con la suma acumulada de los datos de la serie si los elementos son numericos 
print(series1.cumsum())
##//value_counts()\\ Devuelve una serie con la frecuencia (número de repeticiones) de cada valor de la serie
print(series1.value_counts())
##//min()\\ : Devuelve el menor de los datos de la serie.
print(series1.min())
##//max()\\ : Devuelve el mayor de los datos de la serie.
print(series1.max())
##//mean()\\ : Devuelve la media de los datos de la serie s cuando los datos son de un tipo numérico.
print(series1.mean())
##//std()\\ Devuelve la desviación típica de los datos de la serie
print(series1.std())
##////describe()\\\\ Devuelve una serie con un resumen descriptivo que incluye el número de datos, su 
##suma, el mínimo, el máximo, la media, la desviación típica y los cuartiles
print(series1.describe())
####################################
##APLICAR FUNCIONES A UNA SERIE
####################################
##la sentencia apply(funcion) es utilizada para la aplicacion de las funciones a cada elemento de una serie
s = pd.Series(['a', 'b', 'c'])
print(s.apply(str.upper))
################################
##FILTRADO DE UNA SERIE 
################################
##Condiciones sereis[condicion] devuelve la lista de todos los valores que sean true en la condicion 
print(series[series > 5])
################################
##Ordenar Las Series
################################
##//sort_values(ascending=booleano)\\ devuelve la orden de los valores de la serie, si el booleano es 
# true el orden sera ascendente o de lo contrario descendiente  
print(series.sort_values())
##//sort_index(ascending=booleano)\\ devuelve la serie que resulta al ordenar los indices de la serie, si 
# el booleano es true el orden sera ascendente o de lo contrario descendiente   
print(series.sort_index(ascending = False))
##################################
##Eliminar datos desconocidos de una serie
##################################
##Para eliminar los datos desconocidos como NaN o None de una serie se usa //////serie.dropna()\\\\\\
s = pd.Series(['a', 'b', None, 'c', np.NaN,  'd'])
print(s.dropna())
################################################################################################
#######///////////////////////////////////DATA FRAME\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\####
################################################################################################
#LOS DATA FRAME SON TABLAS DONDE LAS COLUMNAS SON UN OBJETO DE TIPO SERIE TODOS LOS DATOS DE UNA MISMA 
# COLUMNA SON IGUALES Y LOS DATOS DE LAS FILAS PUEDEN SER DIFERENTES DE ACUERDO AL REGISTRO 
##UN DATA FRAME CONTIENE 2 INDICES UNO QUE ES PARA LA COLUMNA Y EL OTRO PARA LAS FILAS
####Creacion de Data Frame a partir de diccionarios 
dfDicc = pd.DataFrame([{'Nombre':'María', 'Edad':18}, {'Nombre':'Luis', 'Edad':22}, {'Nombre':'Carmen'}])
print(dfDicc)
####Creacion de Data frame a partir de un array 
dfArr = pd.DataFrame(np.random.randn(4, 3), columns=['a', 'b', 'c'])
print(dfArr)
#################################################################################################
#######################CREAR FATA FRAME A PARTIR DE ARCHIVOS CSV O EXCEL#########################
#################################################################################################
#####PARA CREAR DATA FRAME DE ARCHIVOS CSV SE UTILIZA LA SIGUIENTE FUNCION read_csv y para excel se usa read_excel()
dfDeCSV = pd.read_csv(
'https://raw.githubusercontent.com/asalber/manual-python/master/datos/colesteroles.csv', sep=';', decimal=',')
print(dfDeCSV.head()) ##Head() devuelve las primeras filas, por defecto las 5 primeroas pero se puede cambiar agregando un numero como parametro
############################################################################
##############EXPORTACION DE DATAFRAME A FICHEROS CSV O EXCEL###############
############################################################################
##PARA ESTO SE UTILIZA LAS FUNCIONES DE dataframe.to_csv() o en su defecto dataframe.to_excel()
###################################################################
#############ATRIBUTOS DE UN DATA FRAME ###########################
###################################################################
#dataframe.info() Devuelve información (número de filas, número de columnas, índices, tipo de las columnas y memoria usado) sobre el DataFrame
print(dfDeCSV.info())
##dataframe.shape : Devuelve una tupla con el número de filas y columnas del DataFrame
print(dfDeCSV.shape)
##dataframe.size : Devuelve el número de elementos del DataFrame.
print(dfDeCSV.size)
##dataframe.columns : Devuelve una lista con los nombres de las columnas del DataFrame
print(dfDeCSV.columns)
##dataframe.index : Devuelve una lista con los nombres de las filas del DataFrame 
print(dfDeCSV.index)
##dataframe.dtypes : Devuelve una serie con los tipos de datos de las columnas del DataFrame
print(dfDeCSV.dtypes)
##dataframe.head(n) : Devuelve las n primeras filas del DataFrame 
print(dfDeCSV.head())
##dataframe.tail(n) : Devuelve las n últimas filas del DataFrame
print(dfDeCSV.tail())
########################################################################
######################RENOMBRAR LAS FILAS Y LAS COLUMNAS ###############
########################################################################
print(dfDeCSV.rename(columns={'nombre':'nombre y apellidos', 'altura':'estatura'}, index={0:1000, 1:1001, 2:1002}).head())
######CAMBIAR EL INDICE DE UN DATA FRAME 
print(dfDeCSV.set_index("nombre").head()) ##CAMBIA EL INDICE DEL FRAME ANTERIORMENTE ERA EL NUMERO DE FILA Y AHORA ES EL NOMBRE 
######Reindexar un Data frame
print(dfDeCSV.reindex(index=[4, 3, 1], columns=['nombre', 'tensión', 'colesterol'])) ##Si alguno de los nombres indicados en filas o columnas no existía en el DataFrame df, se crean filan o columnas nuevas rellenas con el valor relleno.
#########################################################################################################
######################################ACCESO A DATOS DEL DATA FRAME #####################################
#########################################################################################################
#SE PUEDE UTILIZAR dataframe.iloc[i,j] en este caso i es la fila y i la columna, tambien se puede poner rango en estos parametros 
# tambien se puede utilizar dataframe.iloc[i] para obtener una fila en espesifica
print(dfDeCSV.iloc[1,4])
print(dfDeCSV.iloc[5])
#Para acceder a los datos mediante el nombre de las filas y las columnas se utiliza dataframe.
print(dfDeCSV.loc[:3,('colesterol','peso')])
#tambien se puede acceder a los datos de una columna completa con la sentencias df.columna si el nombre 
# no tiene espacios en blanco o de lo contrario df[columna ]
print(dfDeCSV['colesterol'].head())
#######################################################################################################
###################################OPERACIONES CON LAS COLUMNAS DE UN DATA FRAME#######################
#######################################################################################################
#APARA AÑADIR UNA NUEVA COLUMNA LO UNICO QUE SE DEBE HACER ES datafreme[nombre de la columna] = serie o lista
#las lista o serie tiene que se igual al numero de registro de lo contrario seran autocompletadas con NaN
dfDeCSV['diabetes'] = pd.Series([False, False, True, False, True])
print(dfDeCSV.head())
##Como todos los datos de una columna son del mismo tipo es facil realizar una operacion en todos los registros de la siguiente manera dataframe[columna] (+-*/ ><==) operacion 
print(dfDeCSV['altura']*100)
## tambien se puede poner una condicion 
print(dfDeCSV['sexo'] == 'M')
##APLICAR FUNCIONES A LAS COLUMNAS, PARA HACER ESTO SOLO SE TIENE QUE UTILIZAR LA SENTENCUIA apply(funcion)
print(dfDeCSV['altura'].apply(log).head(3))
#####################
##Para combertir una cadena de fechas a un tipo de datos datetime se utiliza la sentencia 
df = pd.DataFrame({'Nombre': ['María', 'Carlos', 'Carmen'], 'Nacimiento':['05-03-2000', '20-05-2001', '10-12-1999']})
print(pd.to_datetime(df.Nacimiento, format = '%d-%m-%Y'))##se pone primero la columna y despues el formato de fecha que se desea
#######################################################################################################
###########################ATRIBUTOS DESCRIPTIVOS DE UN DATAFRAME######################################
#######################################################################################################
#////df.count()\\\\ Devuelve una serie número de elementos que no son nulos ni NaN en cada columna del DataFrame df.
#////df.sum()\\\\ Devuelve una serie con la suma de los datos de las columnas del DataFrame df cuando los datos son de un tipo numérico, o la concatenación de ellos cuando son del tipo cadena str.
#////df.cumsum()\\\\ Devuelve un DataFrame con la suma acumulada de los datos de las columnas del DataFrame df cuando los datos son de un tipo numérico.
#////df.min()\\\\ Devuelve una serie con los menores de los datos de las columnas del DataFrame df.
#////df.max()\\\\ Devuelve una serie con los mayores de los datos de las columnas del DataFrame df.
#////df.mean()\\\\ Devuelve una serie con las media de los datos de las columnas del DataFrame df cuando los datos son de un tipo numérico.
#////df.std()\\\\ Devuelve una serie con las desviaciones típicas de los datos de las columnas del DataFrame df cuando los datos son de un tipo numérico.
#////df.describe(include = tipo)\\\\ Devuelve un DataFrame con un resumen estadístico de las columnas del 
# DataFrame df del tipo tipo. Para los datos numéricos (number) se calcula la media, la desviación 
# típica, el mínimo, el máximo y los cuartiles de las columnas numéricas. Para los datos no numéricos 
# (object) se calcula el número de valores, el número de valores distintos, la moda y su frecuencia. Si 
# no se indica el tipo solo se consideran las columnas numéricas.
#########################################################################################
###############ELIMINAR UNA COLUMNA DEL DATAFRAME########################################
#########################################################################################
#PARA ELIMINAR LOS REGISTROS DE UNA COLUMAN SE PUEDEN UTILIZAR DOS SENTENCIAS 
# df.del(nombre) elimina directamente la columna con el nombre que se encontro
# df.pop(nombre) elimina la columna y la devuelve como una serie 
nombre = df.pop('Nombre')
print(nombre)
#########################################################################################################
################################OPERACIONES CON LAS FILAS DE UN DATAFRAME################################
#########################################################################################################
##AÑADIR UNA NUEVA FILA A UN DATAFRAME
##Para añadir una nueva fila al dataframe se utiliza la sentencia dataframe.append()
dfDeCSV = dfDeCSV.append(pd.Series(['Carlos Rivas', 28, 'H', 89.0, 1.78, 245.0], index=['nombre','edad','sexo','peso','altura','colesterol']), ignore_index=True)
print(dfDeCSV.tail(3))
##ELIMINAR UNA FILA DEL DATAFRAME
##Para eliminar una fila del dataframe se utiliza la sentencia dataframe.drop(indice de la fila)
print(df.drop(1))
##FILTRADO DE DATOS DE UNA FILA
## datafreme[Condision] en este caso la funcion devolvera un dataframe que se corresponda con true
print(dfDeCSV[(dfDeCSV['sexo']=='H') & (dfDeCSV['colesterol'] > 260)])
#########################################################################################################
##UN DATA FRAME SE ORDENA AL IGUAL QUE UNA SERIE CON LAS SENTENCIAS 
##sort_values() este ordena las filas de acuerdo a los valores de las columnas 
##sort_index() este otro ordena de acuerdo al indice de las filas 
#########################################################################################################
##########################################ELIMINAR FILAS CONDATOS DESCONOCIDOS ##########################
#########################################################################################################
##Para eliminar las filas que tiene algun dato desconocido se utiliza la sentencia dataframe.dropna()
diabetes = dfDeCSV.pop('diabetes')
print(dfDeCSV.dropna().head())
##DIVIDIR UN DATAFRAME EN GRUPOS 
##Para hacer esto se utiliza la siguiente sentencia dataframe.groupby[columna].groups
print(dfDeCSV.groupby('sexo').groups) #esto ocaciono la division de dos grupos que son H (con todos sus indices) y M (con todos sus indices)
#####Para obtener un grupo mas concreto se utiliza ////dataframe.groupby(columnas).get_group(valores)\\\\
## esto devuelve un data frame con las filas que cumplan con el valor requerido en la mencionada columna
print(dfDeCSV.groupby('sexo').get_group('M'))
#############################
##Agregar funciones de Agregacion a los grupos ya divididos (las funciones de agregacion pueden ser min, max, promedio, suma o lo que sea)
## para esto nada mas se utiliza la sentencia /////dataframe.groupby(columnas).agg(funciones)\\\\
print(dfDeCSV.groupby('sexo').agg(np.mean)) ## esto devolvio un promedio de todo en los grupos H y M
##########################################################################################################
###########################REESTRUCTURAR UN DATA FRAME####################################################
##########################################################################################################
##En ocaciones la dispocicion de los datos en un dataframe no es la mas favorable y se debe rrestructurar (puede ser de formato largo o ancho)
##############################
##COMVERTIR DATA FRAME A FORMATO LARGO con la funcion dataframe.melt(id_vars=id-columnas, value_vars=columnas, var_name=nombre-columnas, var_value=nombre-valores)
datos = {'nombre':['María', 'Luis', 'Carmen'],
'edad':[18, 22, 20],
'Matemáticas':[8.5, 7, 3.5],
'Economía':[8, 6.5, 5],
'Programación':[6.5, 4, 9]}
df = pd.DataFrame(datos)
df1 = df.melt(id_vars=['nombre', 'edad'], var_name='asignatura', value_name='nota')
print(df1)
#############################
##Comvertir data Frame a formato ancho con la siguiente funcion dataframe.pivot(index=filas, columns=columna, values=valores)
print(df1.pivot(index='nombre', columns='asignatura', values='nota'))
##############################################################
###########Coonbinar varios Data frame#########################
##############################################################
##A la hora de combinar estas hay dos manera de hacer una es la Concatenacion y la otra es la Mezcla
##Concatenacion es la union de varios dataframe concatenando sus filas o columnas 
##Mezcla combinacion de varios data frame utilizando columans o indices comunes 
##Para concatenar se utiliza la funcion dataframe.concat([df1,df2], axis = eje) si axis es 0(por defecto) se concatena las filas y si es 1 las columnas 
df1 = pd.DataFrame({"Nombre":["Carmen", "Luis"], 
"Sexo":["Mujer", "Hombre"], "Edad":[22, 18]}).set_index("Nombre")
df2 = pd.DataFrame({"Nombre":["María", "Pedro"], 
"Sexo":["Mujer", "Hombre"], "Edad":[25, 30]}).set_index("Nombre")
df = pd.concat([df1, df2]) ##concatenacion por filas 
print(df)

df1 = pd.DataFrame({"Nombre":["Carmen", "Luis", "María"], 
"Sexo":["Mujer", "Hombre", "Mujer"]}).set_index("Nombre")
df2 = pd.DataFrame({"Nombre":["Carmen", "Luis", "María"], 
"Edad":[22, 18, 25]}).set_index("Nombre")
df = pd.concat([df1, df2], axis = 1)##concatenacion por columnas 
print(df)
#######################
##Mezcla de dataframes esto permite integrar filas de dos DataFrames que contienen información en común 
# en una o varias columnas o índices que se conocen como clave
#para realizar la mezcla se utilza la funcion df.merge(df1, df2, on = clave, how = tipo): Devuelve el
#  DataFrame que resulta de mezclar el DataFrame df2 con el DataFrame df1, usando como claves las 
# columnas de la lista clave y siguiendo el método de mezcla indicado por tipo
#El tipo de mezcla pueden ser las siguientes 

##"inner" (por defecto): El DataFrame resultante solo contiene las filas cuyos valores en la clave están 
# en los dos DataFrames. Es equivalente a la intersección de conjuntos.
df1 = pd.DataFrame({"Nombre":["Carmen", "Luis", "María"],  "Sexo":["Mujer", "Hombre", "Mujer"]})
df2 = pd.DataFrame({"Nombre":["María", "Pedro", "Luis"], "Edad":[25, 30, 18]})
df = pd.merge(df1, df2, on="Nombre")
print(df)

##"outer": El DataFrame resultante contiene todas las filas de los dos DataFrames. Si una fila de un 
# DataFrame no puede emparejarse con otra los mismos valores en la clave en el otro DataFrame, la fila se 
# añade igualmente al DataFrame resultante rellenando las columnas del otro DataFrame con el valor NaN. 
# Es equivalente a la unión de conjuntos.
df1 = pd.DataFrame({"Nombre":["Carmen", "Luis", "María"],  "Sexo":["Mujer", "Hombre", "Mujer"]})
df2 = pd.DataFrame({"Nombre":["María", "Pedro", "Luis"], "Edad":[25, 30, 18]})
df = pd.merge(df1, df2, on="Nombre", how="outer")
print(df)

##"left": El DataFrame resultante contiene todas las filas del primer DataFrame y descarta las filas del 
# segundo DataFrame que no pueden emparejarse con alguna fila del primer DataFrame a través de la clave.
df1 = pd.DataFrame({"Nombre":["Carmen", "Luis", "María"],  "Sexo":["Mujer", "Hombre", "Mujer"]})
df2 = pd.DataFrame({"Nombre":["María", "Pedro", "Luis"], "Edad":[25, 30, 18]})
df = pd.merge(df1, df2, on="Nombre", how="left")
print(df)

##"right": El DataFrame resultante contiene todas las filas del segundo DataFrame y descarta las filas 
# del primer DataFrame que no pueden emparejarse con alguna fila del segundo DataFrame a través de la clave.
df1 = pd.DataFrame({"Nombre":["Carmen", "Luis", "María"],  "Sexo":["Mujer", "Hombre", "Mujer"]})
df2 = pd.DataFrame({"Nombre":["María", "Pedro", "Luis"], "Edad":[25, 30, 18]})
df = pd.merge(df1, df2, on="Nombre", how="right")
print(df)