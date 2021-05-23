# EDA03
Nombre:Sebastian Bettancourt Villaseca Rut:19341715-9

Estructura de datos y algoritmos avanzados , Problema 3 estructuras espaciales

Instrucciones para instalar

Tener instalado python 3.6; 3.7 o 3.8

Correr el archivo main.py

-----------------------------------------------------


  








---------------------------------------------------

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
