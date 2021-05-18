import math as mt
import operator
import leercsv

k=3

class Node:
    def __init__(self,point,left_child,right_child,dim,info): #,data
        #self.data=data
        self.point=point    
        self.left_child=left_child
        self.right_child=right_child
        self.dim=dim
        self.info=info
    def get_id(self):
        #
        point()
        return None
def transforma_data(line):
    L=list()
    


    return L






def make_kdtree(points,depth : int=0):

    if not points:
       return None

    dim= depth % k   #en que dimension se encuentra 

    points.sort(key=operator.itemgetter(dim))#ordena la lista de puntos de menor a mayor segun su dimension
    median=len(points)//2 # division entera
    info=None

    return Node(points[median],make_kdtree(points[0:median],depth+1),make_kdtree(points[median+ 1:],depth+1), dim,info)

def insert(point,root,depth: int=0):

    dim = depth % k #dimension en que se encuentra
    if not root: #Si se encuentra vacio el nodo , retorna un nuevo nodo sin hijos
        info=None
        return Node(point,None,None,dim,info)  
    if point[dim] < root.point[dim]:#Si la coordenada x o y del punto es menor que el punto del nodo en x o y, se mueve hacia el hijo izquierdo , caso contrario hacia el hijo derecho y ejecuta la funcion denuevo
        root.left_child= insert(point, root.left_child,depth+1)
    else:
        root.right_child= insert(point, root.right_child,depth+1) 
    
    return root

def search_id(id,root,depth :int=0):


    if not root: #Si llega a un nodo vacio retorna falso
        return False
    if root.point==point: #Si los puntos del nodo , equivalen al punto que buscamos retorna true
        return True
    dim = depth % k #dimension en que se encuentra
    if point[dim] < root.point[dim]:#Si la coordenada x o y del punto es menor que el punto del nodo en x o y, se mueve hacia el hijo izquierdo , caso contrario hacia el hijo derecho y ejecuta la funcion denuevo
        return search(point, root.left_child,depth+1)
    else:
        return search(point, root.right_child,depth+1)


def search(point,root,depth : int=0):

    if not root: #Si llega a un nodo vacio retorna falso
        return False
    if root.point==point: #Si los puntos del nodo , equivalen al punto que buscamos retorna true
        return True
    dim = depth % k #dimension en que se encuentra
    if point[dim] < root.point[dim]:#Si la coordenada x o y del punto es menor que el punto del nodo en x o y, se mueve hacia el hijo izquierdo , caso contrario hacia el hijo derecho y ejecuta la funcion denuevo
        return search(point, root.left_child,depth+1)
    else:
        return search(point, root.right_child,depth+1)
 
def distance(point,node): #distancia euclidiana entre el punto y el punto del nodo
    suma=0
    for i in range(len(point)):
        suma+=(point[i]-node.point[i])**2
    total=mt.sqrt(suma)

    return total

def nn(point,root,best_distance,best_node): #nearest_neighbour

    if not root: #Si llega a un nodo vacio, retorna el mejor nodo y mejor distancia guardadas
        return best_node,best_distance
    d = distance(point,root) #distancia entre el punto y el nodo actual
    dim=root.dim #dimension actual del kd-tree
    if d<best_distance:
        best_node=root
        best_distance=d

    if point[dim]<root.point[dim]: #Si la coordenada x o y del punto es menor que el punto del nodo en x o y
        nextBranch=root.left_child  #guarda la hoja mas prometedora (hijo izquierdo), y la posible (hijo derecho)
        otherBranch=root.right_child 
    else:
        nextBranch=root.right_child
        otherBranch=root.left_child
    best_node,best_distance=nn(point,nextBranch,best_distance,best_node) #Ejecuta la funcion de nuevo y se mueve hacia la hoja mas prometedora

    if abs(root.point[dim] -point[dim]) < best_distance: #Ejecuta la funcion de nuevo y se mueve hacia la posible hoja solo si la diferencia entre las coordenadas x o y
        best_node,best_distance=nn(point,otherBranch,best_distance,best_node) #entre el punto y el punto del nodo es menor a la mejor distancia   

    return best_node,best_distance

def knn(point,kdtree,n): #k-nearest neighbour
    if kdtree==None or n<1: #Si el arbol se encuentra vacio , o existe una cantidad de vecinos invalida (0 o negativo) retorna null
        return None
    S=[] #StaCK que contiene nodos prometedores a visitar
    Q=[] #Lista ordenada que contiene a los ultimos n nodos mas cercanos al punto ordenados por distancia   
    S.append(kdtree)
    while S:
        node=S.pop()
        d=distance(point,node)
        dim=node.dim
        if point[dim] < node.point[dim]: #Lo mismo que en el algoritmo nn , se va guardando la hoja prometedora y la posible
            nextBranch=node.left_child
            otherBranch=node.right_child    
        else:
            nextBranch=node.right_child
            otherBranch=node.left_child 
        if len(Q)<n :  #Si el tama;o de la lista es menor a n se guardara cualquier nodo que se le inserte
            Q.append(tuple((node,d)))
            Q.sort(key=operator.itemgetter(1))
            if otherBranch is not None:
                S.append(otherBranch)#Como el tama;o de lista es menor a n se agregan todas las hojas al stack
            if nextBranch is not None:    
                S.append(nextBranch)
        #elif len(Q)==n and Q[-1][1]>d: #Si la lista ordenada ya se encuentra llena pero se encuentra un nodo , cuya distancia hacia el punto es menor que

        else:
            if Q[-1][1]>d:     
                Q.pop()                    #la distancia mayor guardada en Q, entonces se elimina la distancia mas grande de Q y se inserta el nuevo nodo en la lista  
                Q.append(tuple((node,d)))
                Q.sort(key=operator.itemgetter(1)) #Si la lista ordenada ya se encuentra llena pero la distancia del nodo no se satisface, entonces se guarda la hoja prometedora en el stack para analizarla en el siguiente ciclo
            if nextBranch is not None: 
                S.append(nextBranch)
            if abs(node.point[dim]-point[dim]) < Q[-1][1]: #Lo mismo que en nn ,guarda en el stack la posible hoja solo si la diferencia entre las coordenadas x o y
                if otherBranch is not None:                #entre el punto y el punto del nodo (distancia mayor de la lista Q), es menor a la mejor distancia      
                    S.append(otherBranch)

    return Q  


###MAIN################################

points=[(3,6),(17,15),(13,15),(6,12),(9,1),(2,7),(10,19)]

points2=[(2,3,4),(5,4,6),(9,6,7),(4,7,8),(8,1,9),(7,2,10)]



archive="Desafio3.csv"
dataset=leercsv.read_dataset(archive)

movies=dataset[0]
alias=dataset[1]
#raise KeyError("asd")
try:
    print (movies[alias['281796108asdasdasdf']])
except KeyError:
    print("no existe pelicula con este id o nombre x.x")



#print (movies[alias['281796108asdasdasdf']])



#root=make_kdtree(points2)
#root2=None
#
#for p in points2:
#    root2=insert(p,root2)
#
#
#point=(4,3,1)
#point2=(9,6,7)
#point3=(2,3,4)
#
#neighbours=3
#print ("Search Results")
#print (search(point,root))
#print (search(point3,root))
#print("")
#
#Neighboorhood=knn(point,root,neighbours)
#Neighboor=nn(point,root,mt.inf,None)
#
#print(Neighboor[0].point)
#print("Neighboorss")
#p=0
#while p<neighbours:
#    print (Neighboorhood[p][0].point)
#    p+=1

