from collections import deque
import heapq
import math as mt
import operator


k=2

class Node:
    def __init__(self,point,left_child,right_child,dim):
        self.point=point
        self.left_child=left_child
        self.right_child=right_child
        self.dim=dim

def make_kdtree(points,depth : int=0):

   if not points:
       return None
   dim= depth % k   #en que dimension se encuentra 

   points.sort(key=operator.itemgetter(dim))#ordena la lista de puntos de menor a mayor segun su dimension
   median=len(points)//2 # division entera
    
   return Node(
       points[median],
       make_kdtree(points[0:median],depth+1), #left_child
       make_kdtree(points[median+ 1:],depth+1), #right_child
       dim
       )

def insert(point,root,depth: int=0):

    dim = depth % k
    if not root:
        return Node(point,None,None,dim)  
    if point[dim] < root.point[dim]:
        root.left_child= insert(point, root.left_child,depth+1)
    else:
        root.right_child= insert(point, root.right_child,depth+1) 
    
    return root

def search(point,root,depth : int=0):

    if not root:
        return False
    if root.point==point:
        return True
    dim = depth % k
    if point[dim] < root.point[dim]:
        return search(point, root.left_child,depth+1)
    else:
        return search(point, root.right_child,depth+1)
 
def distance(point,node):
    suma=0
    for i in range(len(point)):
        suma+=(point[i]-node.point[i])**2
    total=mt.sqrt(suma)

    return total

def nn(point,root,best_distance,best_node): #nearest_neighbour

    if not root:
        return best_node,best_distance
    d = distance(point,root)
    dim=root.dim
    if d<best_distance:
        best_node=root
        best_distance=d

    if point[dim]<root.point[dim]:
        nextBranch=root.left_child
        otherBranch=root.right_child
    else:
        nextBranch=root.right_child
        otherBranch=root.left_child
    best_node,best_distance=nn(point,nextBranch,best_distance,best_node)

    if abs(root.point[dim] -point[dim]) < best_distance:
        best_node,best_distance=nn(point,otherBranch,best_distance,best_node)    

    return best_node,best_distance


       
def knn(point,root,n):
    if root==None:
        return None
    S=[]
    Q=[]
    aux=[]
    S.append(root)
    while S:
        node=S.pop()
        d=distance(point,node)
        dim=node.dim


        if len(Q)<n :  ##guardar las cagas de distances distance(point,Q[-1])<d
            aux.append(node)
            aux.append(d)
            Q.append(aux)
            Q.sort(key=operator.itemgetter(1))
            aux.clear()
        elif len(Q)==n and Q[-1][1]>d:
            Q.pop()
            aux.append(node)
            aux.append(d)
            Q.append(aux)
            Q.sort(key=operator.itemgetter(1))
            aux.clear()
        if point[dim] < node.point[dim]:
            S.append(root.left_child) #verificar distancia
            if abs(node.point[dim]-point[dim]) < distance(Q[0].point,node):
                S.append(root.right_child)#sale primero
        else:
            S.append(root.right_child) #verificar distancia
            if abs(node.point[dim]-point[dim]) < distance(Q[0].point,node):
                S.append(root.left_child) #sale primero

    return Q  

points=[[3,6],[17,15],[13,15],[6,12],[9,1],[2,7],[10,19]]
points2=[[2,3],[5,4],[9,6],[4,7],[8,1],[7,2]]
root2=make_kdtree(points2)
root=None

for p in points:
    root= insert(p,root)
point=[4,3]
point2=[6,7]

Q=[]
aux=["123",3]
aux2=["123123",4]
aux3=["asdf",5]
Q.append(aux)
Q.append(aux3)
Q.append(aux2)
Q.sort(key=operator.itemgetter(1))

print (Q)
