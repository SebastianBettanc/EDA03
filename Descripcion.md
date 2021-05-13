
Explicación funciones kd-tree

El árbol kd-tree es una estructura de datos que particiona el espacio, para organizar los puntos en este.
Este árbol tiene nodos los cuales contienen la data del punto en el espacio, una referencia a su hijo izquierdo, derecho y en que dimensión del árbol se encuentran

![Node](https://user-images.githubusercontent.com/82010968/118082226-c8c2cb00-b38a-11eb-98d6-1faaee21f372.png)

Para Crear el árbol primero le enviamos una lista con todos los puntos que queremos plotear:

![make_kdtree](https://user-images.githubusercontent.com/82010968/118082553-628a7800-b38b-11eb-9323-a1103d5e0d07.png)

El código de make_kdtree es una función recursiva que funciona de la siguiente manera:

• Ordena la lista que le enviamos según su coordenada (parte en x, luego en y , luego x y así sucesivamente), En este caso quedaría así:

![points](https://user-images.githubusercontent.com/82010968/118082962-1855c680-b38c-11eb-9c55-f32129d00ccf.png)

• Luego seleccionamos el punto del medio, y cortamos la lista en 2, Aquí seleccionamos el punto (7,2) y la lista de la izquierda son todos los valores donde su x<7 y la lista de la derecha x>7:

![list_sorted_points](https://user-images.githubusercontent.com/82010968/118082989-21df2e80-b38c-11eb-8ff8-529d26aaa30d.png)

•	Creamos un nuevo nodo, al cual le insertamos el punto de al medio, y para crear su hijo izquierdo le pasamos la lista 1 y le aplicamos la misma función para el hijo izquierdo, para crear el hijo derecho es exactamente lo mismo pasándole la lista 3

![Node_kd](https://user-images.githubusercontent.com/82010968/118083320-a8940b80-b38c-11eb-80bb-2e8c41ddb0bb.png)

• Una vez que la lista es vacia simplemente retornamos null y asi se va llenando el arbol
	
![null_kdtree_return](https://user-images.githubusercontent.com/82010968/118083423-e42ed580-b38c-11eb-84f3-b4bb3b1ae958.png)

Este arbol quedaria de la siguiente manera 


![Tree_0001 svg](https://user-images.githubusercontent.com/82010968/118083746-6d460c80-b38d-11eb-96df-51149f6de08b.png)

Y en forma cartesiana:

![Kdtree_2d svg](https://user-images.githubusercontent.com/82010968/118083751-71722a00-b38d-11eb-91ef-7dcf2d518f05.png)



Funcion nearest neighbourt (vecino mas cercano al punto):

Para encontrar el vecino mas cercano es similar a la busqueda de 1 nodo.

Primero calculamos la distancia del nodo actual el siguiente

--IMAGEN

Si la distancia calculada anteriormente es menor a la mejor_distancia , entonces mejor_distancia pasa a ser la nueva distancia calculada y ademas se guarda el nodo correspodiente a esta

--IMAGEN

Si la coordenada x o y (depende de la dimension en la que estamos, se parte con x luego y y asi sucesivamente), del punto es menor que la coordenada x o y del nodo entonces
guardamos la hoja mas prometedora (hijo izquierdo) y la hoja posible (hijo derecho), la hoja mas prometedora y la posible se invierten si el punto es mayor al nodo x,y.


--IMAGEN

Recorremos hacia la hoja prometedora y repetimos el proceso en el paso 1

--IMAGEN

Recorremos hacia la hoja posible solo si se cumple que la diferencia entre las coordenadas x o y entre el punto y el nodo es menor a la mejor distancia guardada, en caso 
contrario no recorremos la hoja posible , ya que no existiran nodos con menor distancia a la mejor guardada

--IMAGEN

Una vez que llegamos a un nodo vacio , simplemente retornamos el mejor nodo y distancia guardados

--IMAGEN


Funcion  K-neares neighbour






