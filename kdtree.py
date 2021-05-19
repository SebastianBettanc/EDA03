import math as mt

from numpy.core.records import array
import leercsv
import numpy as np
import matplotlib.pyplot as plt
import os
import time

class Node:
    def __init__(self,point,info): #,data
        self.point=point    
        self.info=info


def transformar(data):

    dictionary={"Social Networking":1,
                "Health & Fitness":2,
                "Games":3,
                "Sports":4,
                "Food & Drink":5,
                "Productivity":6,
                "Weather":7,
                


    }


    L=list()
    L.append(data[11]) # genero principal transformaremos data

    return L


def cossim(v1,v2):#"compute cosine similarity of v1 to v2: (v1 dot v2)/{||v1||*||v2||)" distancia coseno entre dos listas
    
    sumxx, sumxy, sumyy = 0, 0, 0
    for i in range(len(v1)):
        x = v1[i]; y = v2[i]
        sumxx += x*x
        sumyy += y*y
        sumxy += x*y
    return sumxy/mt.sqrt(sumxx*sumyy)

def hashing(vector,matriz_transpuesta):

    hash=''.join((np.dot(vector,matriz_transpuesta)>0).astype(int).astype('str')) #fucnion hash #vector 1 pelicula

    return hash

###MAIN################################

#Locality-Sensitive Hashing (LSH), implementar , se 

archive="Desafio3.csv"
#dataset=np.array(leercsv.read_dataset(archive))
dataset2=leercsv.read_dataset(archive)
map_data=dict()
alias=dict()
vectors=list()

for row in dataset2:
    #modificar row
    aux=transformar(row)
    vectors.append(aux)
    map_data[row[0]]=row
    alias[row[0]]=row[0]
    alias[row[1]]=row[1]






#a[11].append(3)
#a[11].append(5)
#print(a[11])


os.system('cls')


#movies=dataset[0]
#alias=dataset[1]
#raise KeyError("asd")
#try:
#    print (movies[alias['281796108asdasdasdf']])
#except KeyError:
#    print("no existe pelicula con este id o nombre x.x")








#n = 7190 #total de datos n=b*r
#
#b=719 #cantidad de buckets
#r =10 #cantidad de datos x bucket
#d= 20  #largo vectores del data set
#
#
#i=42
#K = 3
vec1=np.array([-0.99137472, 0.61572851, -0.37733555,  0.0363575 , -0.71647706])#matriz de vectores de a comparar con peliculas #se usara para knn (k-nearest-neighbour)
vec2=np.array([-0.16737788, 0.83147812, -2.06947369, -0.48174425, -1.60276846])#
vec3=np.array([-0.9074722 , 0.75953396,  1.10696926, -0.8773451 , -1.11589595])


projections=np.array([[ 0.58834302,  0.24020825,  2.21323827, -0.21147486,  1.18477223],
                      [-0.31146359, -1.88214137, -0.37489443, -0.58475914, -1.57121651]]) #matriz con datos de las peliculas

T=projections.T #matriz transpuerta de projections

#np.random.seed(47)
prob=np.random.randn(5, 5) # dimension de vector con dimension 
#T=prob.T
print (prob)

codigo_hash1=hashing(vec1,T)
codigo_hash2=hashing(vec2,T)
codigo_hash3=hashing(vec3,T)

table_hash=dict() #sonn varias tablas hash , si coincide en su valor de hash en 1 de las tablas , entonces son vecinos 
L=list()

vectores_qls=[[3,4,9,7,8],[1,2,3,9,10]]
print (cossim(vectores_qls[0],vectores_qls[1]))

for vector_ql in vectores_qls:
    codigo_hash=hashing(vector_ql,T)
    print(codigo_hash)



lsh[11]=L
print(lsh[11])
#
#print("\n\n\n\n")
#print (" vector1: ",vec1,"su hash es: ",codigo_hash1,"\n",
#    '#############################################################################\n',
#    "vector2: ",vec2,"su hash es: ",codigo_hash2,"\n",
#    '#############################################################################\n',                   
#    "vector3: ",vec3,"su hash es: ",codigo_hash3,"\n ################################")
#print(" ###############################")
#print("Distancia coseno para vecinos: \n ",vec1,"\n ",vec2 ,"\n  ",cossim(vec1,vec2))
#print(" ###############################")
#print("Distancia coseno para vecinos: \n ",vec1,"\n ",vec3 ,"\n  ",cossim(vec1,vec3))
#print(" ###############################")
#print("Distancia coseno para vecinos: \n ",vec2,"\n ",vec3 ,"\n  ",cossim(vec2,vec3))
#
#
#local_hashing= LSH(3,7,len(vec1))  #cantidad de tablas hash por la que pasara la colicion , 7 largo del valor hash ,
#local_hashing.set(vec1,"bucket1")
#local_hashing.set(vec2,"bucket1")
#local_hashing.set(vec3,"bucket3")
#
#print(local_hashing.__getitem__(vec2))
#
##time.sleep(5)
#os.system("cls")
#vector_aux=list(movies.values())
#print(vector_aux)
#print("\n")
#
#for i in range(len(vector_aux)):
#    vector_aux[i]=transformar(vector_aux[i])
#print(vector_aux)
