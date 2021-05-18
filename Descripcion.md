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

-----------------------------------------------------------------------------------

Funcion search (busca si el punto dado existe o no el kd-tree):

La funcion search es una funcion recursiva , llegara a falso en caso de llegar a un nodo nulo (esto pasara si ningun nodo cumple la condicion), o sera true si el nodo current 
es igual al punto buscado

![search_returns](https://user-images.githubusercontent.com/82010968/118112089-86ad7f80-b3b2-11eb-9ed7-168cff49d2e1.png)

Para ir recorriendo los nodos del arbol primero chequeamos si la coordenada x (x o y, en este caso es X) del punto es menor que la coordenada x del nodo, en caso de ser menor nos movemos al hijo izquierdo
y ejecutamos la funcion denuevo donde ahora root sera root.left_child, para el caso contrario (es mayor) sera root.right_child

![search_next](https://user-images.githubusercontent.com/82010968/118112130-962cc880-b3b2-11eb-9794-6a2a778b4062.png)

En la siguiente iteracion sera lo mismo de los pasos anteriores pero ahora coompara con la coordenada y en caso de no cumplirse las condiciones para terminar la funcion

*La funcion insert es exactamente igual a la funcion search con la diferencia que la condicion de salida de la funcion solo retorna cuando se llega a un nodo vacio y este retorna
el ultimo nodo

![return_insert](https://user-images.githubusercontent.com/82010968/118112169-a3e24e00-b3b2-11eb-8349-ecce769f72b2.png)


---------------------------------------------------------------------------------------------------

Funcion nearest neighbourt (vecino mas cercano al punto):

Para encontrar el vecino mas cercano es similar a la busqueda de 1 nodo.

Primero calculamos la distancia del nodo actual el siguiente

![funcion_distancia](https://user-images.githubusercontent.com/82010968/118108744-5cf25980-b3ae-11eb-93b2-b8be9c13124c.png)


Si la distancia calculada anteriormente es menor a la mejor_distancia , entonces mejor_distancia pasa a ser la nueva distancia calculada y ademas se guarda el nodo correspodiente a esta

![best_distance](https://user-images.githubusercontent.com/82010968/118109098-beb2c380-b3ae-11eb-82d6-8fe89997bdcf.png)

Si la coordenada x o y (depende de la dimension en la que estamos, se parte con x luego y y asi sucesivamente), del punto es menor que la coordenada x o y del nodo entonces
guardamos la hoja mas prometedora (hijo izquierdo) y la hoja posible (hijo derecho), la hoja mas prometedora y la posible se invierten si el punto es mayor al nodo x,y.

![branches](https://user-images.githubusercontent.com/82010968/118109373-181af280-b3af-11eb-93a5-f539b83ee68f.png)

Recorremos hacia la hoja prometedora y repetimos el proceso en el paso 1

![best_branch](https://user-images.githubusercontent.com/82010968/118109746-94153a80-b3af-11eb-90f8-4896171f89bb.png)

Recorremos hacia la hoja posible solo si se cumple que la diferencia entre las coordenadas x o y entre el punto y el nodo es menor a la mejor distancia guardada, en caso 
contrario no recorremos la hoja posible , ya que no existiran nodos con menor distancia a la mejor guardada

![other_branch](https://user-images.githubusercontent.com/82010968/118109769-9b3c4880-b3af-11eb-8245-e9cbb8d2719e.png)

Una vez que llegamos a un nodo vacio , simplemente retornamos el mejor nodo y distancia guardados

![return_nn](https://user-images.githubusercontent.com/82010968/118109787-a000fc80-b3af-11eb-95ae-ce7a5786cdea.png)

------------------------------------------------------------------------------------
Funcion  K-nearest neighbour

Es similar a la funcion Nearest Neighbour(nn) en cuanto a funcionalidad

Primero creamos una Stack S y una lista ordenada Q; El stack contendra nodos "posibles" que podrian ser vecinos  , mientras que la lista Q guarda los n mejores nodos (los 
mas cercanos al punto p por distancia)

Insertamos el nodo root en el stack.

Mientras el stack no este vacio vamos chequeando que:

• Sacamos el ultimo nodo del stack y lo almacenamos en una variable.

• Calculamos la distance euclidiana entre el punto y el nodo

![distance_knn](https://user-images.githubusercontent.com/82010968/118110323-451bd500-b3b0-11eb-8c96-1122a16cf440.png)

• Al igual que en nn vamos guardando las hoja mas prometedora y la posible dependiendo de si la coordenada x o y del punto es menor o mayor que la coordenada x,y del nodo

![branches_knn](https://user-images.githubusercontent.com/82010968/118110343-4baa4c80-b3b0-11eb-9a8c-8d725cdc912b.png)

• Si la cantidad de datos de la lista Q es menor o igual a n(cantidad de vecinos), entonces agregamos el nodo a la lista Q, reordenamos la lista y agregamos al stack las 2
hojas

![Q_not_full](https://user-images.githubusercontent.com/82010968/118110378-5664e180-b3b0-11eb-818a-d6de9151052e.png)


• Si la lista Q se encuentra llena y la distancia del nodo con el punto , es mejor que la distancia mayor guardada en la lista Q , (ulitmo dato de la lista contiene el vecino
con la distancia mas larga), se borra el ultimo dato de la lista Q , se agrega el nuevo nodo a Q y se reordena

![Q_full_distance_true](https://user-images.githubusercontent.com/82010968/118110649-ac398980-b3b0-11eb-8bf6-cf574a913de9.png)


• En caso de que la lista Q este llena pero el nodo no cumple con la condicion de la distancia previa, entonces agregamos la hoja prometedora al stack ; Agregamos la hoja posible al stack solo si la diferencia de las coordenadas x o y entre el punto y el nodo , es menor a la distancia peor de la lista Q , entonces agregamos la hoja posible en
el stack

![Q_full](https://user-images.githubusercontent.com/82010968/118110669-b3f92e00-b3b0-11eb-95b3-a1c846d17773.png)

• Repetimos el proceso hasta que el stack este vacio

------------------------------------------------------------------------------------

Ejecucion del programa:


![ejecucion](https://user-images.githubusercontent.com/82010968/118112454-03d8f480-b3b3-11eb-8dd4-7ac09ac33991.png)






