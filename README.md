# EDA03
🟦Nombre:Sebastian B.


Estructura de datos y algoritmos avanzados , Problema 3 estructuras espaciales

Instrucciones para instalar

Tener instalado python 3.6; 3.7 o 3.8

Correr el archivo main.py

-----------------------------------------------------


🟥El problema de los vecinos mas cercanos (KNN) en este problema se define como: Dado un dataset P con N vectores en el, se construira una estructura de datos que dado cualquier vector Q, retorne el conjunto de vectores L, que sean cercanos a Q, esta estructura tiene que ser capaz de obtener los KNN sin comparar todas las distancias entre el vector Q y los N vectores de P.

  
  
  
  Tendremos un dataset A ,cada fila estara compuesta de la siguiente forma:
  

  ID  | VECTOR NO NORMALIZADO
  ----|---------------------
  "123468421"  |  Q
  .|.
  .|.
  .|.
  .|.
  

  
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

---------------------------------------------------------------

Para generar el dataset P:

  ID  | VECTOR NORMALIZADO
  ----|---------------------
  "123468421"  |  Q'
  .|.
  .|.
  .|.
  .|.
          
          
 
Pos Vector Q' |Valor
-------------|----------------------------------------------------------------------------------------------
Q[0]| Bytes/4025969664.0
Q[1]| Precio/299.99
Q[2]| Cantidad de reseñas (Para todas las versiones)/2974676
Q[3]| Cantidad de reseñas (Para la versión actual)/177050
Q[4]| Promedio de puntaje de las reseñas (Para todas las versiones)/5.0
Q[5]| Promedio de puntaje de las reseñas (Para la versione actual)/5.0
Q[6]| Rating de contenido ***(ver figura 1)***
Q[7]| Genero principal ***(ver figura 2)***
Q[8]| Cantidad de dispositivos soportados/47.0
Q[9]| Cantidad de capturas de pantallas por dispositivos/5.0
Q[10]| Cantidad de lenguajes soportados/75.0
Q[11]| Valor licencia Vpp


>***figura 1***:<img src="https://user-images.githubusercontent.com/82010968/119278045-f0b6f780-bbf0-11eb-8ab3-a40dc870f910.png" width="300" />

>***figura 2*** :<img src="https://user-images.githubusercontent.com/82010968/119278068-03313100-bbf1-11eb-9b0f-fd473d4eaf69.png" width="300" />


Para reducir el tiempo total y la memoria para encontrar los knn, para este problema en particular utilizaremos LSH.



---------------------------------------------------

 
🟩Local sensitive hashing(LSH)



LSH consiste en utilizar tablas hash que contienen buckets, dentro de cada bucket se encuentran vectores similares entre si:

<img src="https://user-images.githubusercontent.com/82010968/119298657-70fa4e80-bc2b-11eb-93fe-d9d3fd77da02.png" width="600" />

Entonces para encontrar los knn de un vector E cualquiera , simplemente vamos al bucket donde se encuentra este vector y todos los vectores que se encuentren en el mismo bucket que el son vecinos de este. Para poder determinar los vectores que van en un mismo bucket L utilizaremos una funcion hash, esta funcion hash dada esta por:


<img src="https://user-images.githubusercontent.com/82010968/119299737-81132d80-bc2d-11eb-8dc7-3269109608de.png" width="400" />

------------------------------------------

<img src="https://user-images.githubusercontent.com/82010968/119214820-aa01ba00-ba97-11eb-9bcd-ef54dfb15a18.png" width="400" />

 


En la figura anterior,asumamos que A,B Y D son vecinos cercanos , vemos que el vector A y B van en el mismo bucket "111" ,pero no a si el vector D, este problema se presenta ya
que la funcion hash es diferente dependiendo de la tabla T , vemos que pasa si realizamos lo mismo con una tabla M:

<img src="https://user-images.githubusercontent.com/82010968/119272557-77a9a700-bbd4-11eb-9fb5-4a2f84809161.png" width="400" />


  En este caso vemos que el vector A y D corresponden al mismo bucket "011", pero en este caso B no tiene el mismo valor del bucket a pesar de ser vecino con A, una solucion para esto , es tener varias tablas hash donde los knn de un vector V cualquiera sera el conjunto de los buckets :
  
 ***knn(V)= Conjunto( Tabla1( hash (V) ) + Tabla2(hash(V)) + .... + TablaN (hash(V)) )***
  
  En nuestro caso particular para ejemplificar mejor seria:
 
  ***knn(A)= Conjunto( T[hash (A)] + M[hash(A)] ) => Conjunto( T["111"] +M["011"] )***
  
  ***=> Conjunto( [A,B]  +[A,D] ) = knn(A) = [A,B,D]*** 
  

------------------------------

Para generalizar se tiene la siguiente figura de ejemplo: 

<img src="https://user-images.githubusercontent.com/82010968/119300440-c1bf7680-bc2e-11eb-9a72-f884856d21cb.png" width="700" />



  Los parametros que recibe esta estructura LSH, es el factor k del hash (largo del hash) y lenght ,que nos indica que tantas tablaHash se utilizaran para calcular las colisiones; Para nuestro dataset **k=300** , **lenght=7**.
  
  Un problema que no se ha mencionado, es que nosotros al querer obtener los 10 knn mas cercannos a un vector V es probable que 1 bucket o el set completo tenga mas de 10 datos(vecinos),en este caso en particular simplemente juntamos el set completo y ordenamos por menos distancia euclidiana , elegimos los 10 mejores y descartamos los demas.
  
  
  <img src="https://user-images.githubusercontent.com/82010968/119300899-8d988580-bc2f-11eb-910d-8ccb1ad36906.png" width="550" />




-------------------------

🟪Resultados



-Mostrar informacion app:

***get_app (apps,alias,'281656475')***

***get_app (apps,alias,'PAC-MAN Premium')***

![resultado1](https://user-images.githubusercontent.com/82010968/119301688-e0bf0800-bc30-11eb-8cb2-4e05e969c87a.png)

-Mostrar informacion app mas usadas parecidas a id o vector , En este caso de ejemplo contiene la id y la distancia hacia el vector que  corresponde a la app ('281656475' ,pacman premium) :

***Vector A= get_app (apps,alias,id ) o Vector A= [0.03,0.01,.....,n}***

***set_lsh = list(LSH.LSH(k,vectorA,hashTables,T_list))***

***neighbours_lsh= lsh_knn(vectorA,set_lsh,apps,alias,10)***

***print(neighbours_lsh)***

![resultado2](https://user-images.githubusercontent.com/82010968/119302054-76f32e00-bc31-11eb-8fe2-9fbb25de3c7c.png)

-Comparar resultados:

***neighbours_brute=brute_knn(vector_id,matrix,10) vs neighbours_lsh***

![resultado3](https://user-images.githubusercontent.com/82010968/119302486-31833080-bc32-11eb-92d9-2827d47bd15f.png)

🔴Corroborar que lsh y fuerza bruta son los mismos


![resultado_final](https://user-images.githubusercontent.com/82010968/119303307-84111c80-bc33-11eb-8bc5-dfecd5df184a.png)

Podemos ver que son exactamentes iguales.


------


⬛VIDEO EXPLICATIVO LINK = https://youtu.be/V_obqvM2QkY


Coevaluacion 
Sebastian :+0
