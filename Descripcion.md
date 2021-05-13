
Explicación funciones kd-tree

El árbol kd-tree es una estructura de datos que particiona el espacio, para organizar los puntos en este.
Este árbol tiene nodos los cuales contienen la data del punto en el espacio, una referencia a su hijo izquierdo, derecho y en que dimensión del árbol se encuentran

![Node](https://user-images.githubusercontent.com/82010968/118082226-c8c2cb00-b38a-11eb-98d6-1faaee21f372.png)

Para Crear el árbol primero le enviamos una lista con todos los puntos que queremos plotear:

![make_kdtree](https://user-images.githubusercontent.com/82010968/118082553-628a7800-b38b-11eb-9323-a1103d5e0d07.png)

El código de make_kdtree es una función recursiva que funciona de la siguiente manera:

• Ordena la lista que le enviamos según su coordenada (parte en x, luego en y , luego x y así sucesivamente), En este caso quedaría así:

![points](https://user-images.githubusercontent.com/82010968/118082962-1855c680-b38c-11eb-9c55-f32129d00ccf.png)

•	Luego seleccionamos el punto del medio, y cortamos la lista en 2, Aquí seleccionamos el punto (7,2) y la lista de la izquierda son todos los valores donde su x<7 y la lista de la derecha x>7:

![list_sorted_points](https://user-images.githubusercontent.com/82010968/118082989-21df2e80-b38c-11eb-8ff8-529d26aaa30d.png)

•	Creamos un nuevo nodo, al cual le insertamos el punto de al medio, y para crear su hijo izquierdo le pasamos la lista 1 y le aplicamos la misma función para el hijo izquierdo, para crear el hijo derecho es exactamente lo mismo pasándole la lista 3

![Node_kd](https://user-images.githubusercontent.com/82010968/118083320-a8940b80-b38c-11eb-80bb-2e8c41ddb0bb.png)

• Una vez que la lista es vacia simplemente retornamos null y asi se va llenando el arbol
	
![null_kdtree_return](https://user-images.githubusercontent.com/82010968/118083423-e42ed580-b38c-11eb-84f3-b4bb3b1ae958.png)

Este arbol quedaria de la siguiente manera 


![Tree_0001 svg](https://user-images.githubusercontent.com/82010968/118083746-6d460c80-b38d-11eb-96df-51149f6de08b.png)

Y en forma cartesiana:

![Kdtree_2d svg](https://user-images.githubusercontent.com/82010968/118083751-71722a00-b38d-11eb-91ef-7dcf2d518f05.png)



