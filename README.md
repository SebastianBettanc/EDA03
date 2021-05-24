# EDA03
Nombre:Sebastian Bettancourt Villaseca Rut:19341715-9

Estructura de datos y algoritmos avanzados , Problema 3 estructuras espaciales

Instrucciones para instalar

Tener instalado python 3.6; 3.7 o 3.8

Correr el archivo main.py

-----------------------------------------------------

El problema de los vecinos mas cercanos (KNN) en este problema se define como: Dado un dataset P con N vectores en el, se construira una estructura de datos que dado cualquier vector Q, retorne el conjunto de vectores L, que sean cercanos a Q, esta estructura tiene que ser capaz de obtener los KNN sin comparar todas las distancias entre el vector Q y los N vectores de P.

  
  
  
  Nuestro dataset P, en cada fila tendra 1 valor , este valor corresponde a:
  
  •(ID,VECTOR_NORMALIZADO) 
  
  Para obtener los vectores normalizado primero tenemos que aplicar una funcion de normalizacion a un vector no normalizado, 
  
Vector Q cualquiera no normalizado:


Pos Vector Q |Informacion                      								              | Tipo de valores	| Rango Valores
-------------|--------------------------------------------------------------|---------|---------------------
Q[0]		     |App ID 														                            |str  		|
Q[1]		     |Nombre de la App 												                      |str  		|
Q[2]		     |Tamaño (en Bytes)												                      |int		  |0-4025969664
Q[3]		     |Moneda														                            |str  		|"USD"
Q[4]		     |Precio en la Moneda											                      |float 		|0-299.99
Q[5]		     |Cantidad de reseñas (Para todas las versiones)				        |int		  |0-2974676
Q[6]		     |Cantidad de reseñas (Para la versión actual)					        |int   		|0-177050
Q[7]		     |Promedio de puntaje de las reseñas (Para todas las versiones)	|float    |0-5.0
Q[8]         |Promedio de puntaje de las reseñas (Para la versión actual)	  |float 		|0-5.0
Q[9]		     |Ultima version 												                        |str		  |
Q[10]		     |Rating de contenido 											                    |str		  |
Q[11]		     |Género principal												                      |str		  |
Q[12] 		   |Cantidad de dispositivos soportados							              |int 		  |0-47
Q[13] 		   |Cantidad de capturas de pantallas por dispositivos			      |int 		  |0-5
Q[14] 		   |Cantidad de lenguajes soportados								              |int 		  |0-75
Q[15] 		   |Licencia Vpp activada 										                    |int 		  |0 o 1




 El vector Q normalizado :
 
Pos Vector Q |Valor
-------------|----------------------------------------------------------------------------------------------
Q[0]| Bytes/4025969664.0
Q[1]| Precio/299.99
Q[2]| Cantidad de reseñas (Para todas las versiones)/2974676
Q[3]| Cantidad de reseñas (Para la versión actual)/177050
Q[4]| Promedio de puntaje de las reseñas (Para todas las versiones)/5.0
Q[5]| Promedio de puntaje de las reseñas (Para la versione actual)/5.0
Q[6]| Rating de contenido *(ver figura 1)
Q[7]| Genero principal *(ver figura 2)
Q[8]| Cantidad de dispositivos soportados/47.0
Q[9]| Cantidad de capturas de pantallas por dispositivos/5.0
Q[10]| Cantidad de lenguajes soportados/75.0
Q[11]| Valor licencia Vpp


>***figura 1***:
![fig1_1](https://user-images.githubusercontent.com/82010968/119278045-f0b6f780-bbf0-11eb-8ab3-a40dc870f910.png)

>***figura 2*** :
![fig2_2](https://user-images.githubusercontent.com/82010968/119278068-03313100-bbf1-11eb-9b0f-fd473d4eaf69.png)



Para reducir el tiempo total y la memoria para encontrar los knn, para este problema en particular utilizaremos LSH.



---------------------------------------------------

 ![#f03c15](https://via.placeholder.com/15/f03c15/000000?text=+)
Local sensitive hashing(LSH)

LSH consiste en utilizar tablas hash que contienen buckets, dentro de cada bucket se encuentran vectores similares entre si; Entonces para encontrar los knn de un vector E cualquiera , simplemente vamos al bucket donde se encuentra este vector y todos los vectores que se encuentren en el mismo bucket que el son vecinos de este. Para poder determinar los vectores que van en un mismo bucket L .

![fig1](https://user-images.githubusercontent.com/82010968/119214820-aa01ba00-ba97-11eb-9bcd-ef54dfb15a18.png)

En la figura anterior,asumamos que A,B Y D son vecinos cercanos , vemos que el vector A y B van en el mismo bucket "111" ,pero no a si el vector D, este problema se presenta ya
que la funcion hash es diferente dependiendo de la tabla T , vemos que pasa si realizamos lo mismo con una tabla M:

![fig2](https://user-images.githubusercontent.com/82010968/119272557-77a9a700-bbd4-11eb-9fb5-4a2f84809161.png)


  En este caso vemos que el vector A y D corresponden al mismo bucket "011", pero en este caso B no tiene el mismo valor del bucket a pesar de ser vecino con A, una solucion para esto , es tener varias tablas hash donde los knn de un vector V cualquiera sera el conjunto de los buckets :
  
  knn(V)= Conjunto( Tabla1( hash (V) ) + Tabla2(hash(V)) + .... + TablaN (hash(V)) )
  
  En nuestro caso particular para ejemplificar mejor seria:
 
  knn(A)= Conjunto(T[hash (A)] + M[hash(A)] ) => Conjunto( T["111"] +M["011"] ) => Conjunto( [A,B]  +[A,D] ) = knn(A) = [A,B,D] (fig7)

Para generalizar si existe una colision de un dato distinto al vector A en una tabla cualquiera (T y M en este caso) , entonces este es muy probable que este sea vecino de
el vector A

  dibujo*

  Los parametros que recibe esta estructura LSH, es una factor k que determina que tan largo sera el hash (hash consiste de 0 y 1) y lenght ,que nos indica que tantas tablaHash se utilizaran para calcular las colisiones; Para nuestro dataset en particular tendremos un factor k=300 y lenght=7.
  
  Un problema que no se ha mencionado, es que nosotros al querer obtener los 10 knn mas cercannos a un vector V es probable que 1 bucket o el set completo tenga mas de 10 datos(vecinos),en este caso en particular simplemente juntamos el set completo y ordenamos por menos distancia euclidiana , elegimos los 10 mejores y descartamos los demas.
  
  
  
  se puede corrobar que de hecho los vecinos con LSH , corresponde exactamente a los vecinos encontrados por fuerza bruta , es decir, mientras mas alto sea el factor k y lenght la prediccion de LSH tiene menos % de falsos positivos, 
Si aumentamos mucho el lenght este ocasiona que nuestro algoritmo sea mas lento , pero si su valor es muy peque;o existe una posibilidad de que puede entregar menos vecinos de los pedidos 











-------------------------


VIDEO EXPLICATIVO LINK = https://youtu.be/V_obqvM2QkY


Coevaluacion 
Sebastian :+0
