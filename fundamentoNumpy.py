import numpy as np
##Arange es una sentencia que se utliza para generar numeros en un rango determinado 
rangoNumeros = np.arange(1,10)
print(rangoNumeros)
## a arange tambien se le puede decir de cuanto en cuanto debe sumar /////(desde, hasta, pasos)\\\\\\
rangoNumeros2 = np.arange(1,10,2)
print(rangoNumeros2)
##Podemos Crear Arreglos de Ceros facilmente con la funcion /////zeros\\\\\ el argumento que se le pasa es la 
##cantidad de datos que se decea que tenga el arreglo
arreglosCeros = np.zeros(5)
print(arreglosCeros)
##esto tambien se puede usar para matrices en este caso el agumento serian 2, estas son las dimenciones de la matriz
matrizCeros = np.zeros((4,3))
print(matrizCeros)
## esto mismo se puede hacer pero llenar la matriz de 1 con la funcion ////np.ones(5) y np.ones((4,3))\\\\
##//////////////////////////////////////
## Para dividir un rango de numero en Intervalos iguales se utiliza /////////linspace(inicio, fin, numeor de subintervalos)\\\\\\\\\\\
intervalos = np.linspace(0,1,5)
print(intervalos)
##Para hacer un arreglo Identidad (la diagonal de una matriz cuadrada son todos 1) en Numpy se utiliza la funcion 
#///////np.eye(extencion de la matriz)\\\\\\\\\
arregloIdentidad = np.eye(3)
print(arregloIdentidad)
##Crear matrices (4,3) o arreglos(6)  con numero a leatorios en numpy se hace con la siguiente funcion 
#/////////np.random.randint(inicio, fin, dimencion)\\\\\\
matrizAleatorio1 = np.random.randint(1,10,(4,3))
print(matrizAleatorio1)
##Transformar un arreglo en una matriz ///arreglo.reshape(dimeciones)\\\\
arreglo = np.array(np.random.randint(1,10,6))
print(arreglo)
arregloTransformadoMatriz = arreglo.reshape(2,3)
print(arregloTransformadoMatriz)
#////////////////// 
#Metodos para encontrar el numero mayor/menor o la poisicion del numero mayor/menor en un arreglo 
##///arreglo.max\\\ numero mayor del arreglo
print(arreglo.max())
##///arreglo.argmax\\\ posicion(indice) del numero mayor 
print(arreglo.argmax())
##///arreglo.min\\\ numero menor del arreglo 
print(arreglo.min())
##///arreglo.argmin\\\ posicion(indice) del numeor menor 
print(arreglo.argmin())

#####////////OPERACIONES MAS COMPLEJAS////////////
#La raiz cuadrada se calcula con la funcion //////np.sqrt(arreglo o numero o matriz )\\\\\\\
print(np.sqrt(arreglo))
#para calcular el exponencial se utiliza ///////np.exp(arreglo)\\\\\\\\\
print(np.exp(arreglo))
####################################################
##Para calculos trigonometricos se utilizan las funciones np.sin (seno), np.cos(coseno) y np.log(logaritmo)
##seno
print(np.sin(arreglo))
##coseno 
print(np.cos(arreglo))
##tangente
print(np.tan(arreglo))
##logaritmo 
print(np.log(arreglo))
#####################################################################
## INDEXACION Y ASIGNACION 
#####################################################################
arr = np.round(np.random.rand(5),2)
##la utilizacion de slice es la misma que en python con los corchetes
print(arr[:])
## accedemos a los elementos por medio de la indexacio y le asignamos un nuevo valor 
arr[2:4] = 2
print(arr)

