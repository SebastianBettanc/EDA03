import math as mt

from numpy.core.records import array
import leercsv
import numpy as np
import matplotlib.pyplot as plt
import os
import time

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

#Locality-Sensitive Hashing (LSH), Implementado

archive="Desafio3.csv"
dataset=leercsv.read_dataset(archive)
dataset_array=np.array(leercsv.read_dataset(archive))
map_data=dict()
alias=dict()
vectors=list()

for row in dataset:

    aux=transformar(row)    #modificar row
    vectors.append(aux)
    map_data[row[0]]=row
    alias[row[0]]=row[0]
    alias[row[1]]=row[1]

vectors_standar=list()
for k in map_data.keys():
    data=transformar(map_data[k])
    vector=(k,map_data[k])
#    print (vector)
#time.sleep(10)
os.system('cls')

#try:
#    print (movies[alias['281796108asdasdasdf']])
#except KeyError:
#    print("no existe pelicula con este id o nombre x.x")

vec1=np.array([-0.99137472, 0.61572851, -0.37733555,  0.0363575 , -0.71647706])#matriz de vectores de a comparar con peliculas #se usara para knn (k-nearest-neighbour)
vec2=np.array([-0.16737788, 0.83147812, -2.06947369, -0.48174425, -1.60276846])#
vec3=np.array([-0.9074722 , 0.75953396,  1.10696926, -0.8773451 , -1.11589595])


projections=np.array([[ 0.58834302,  0.24020825,  2.21323827, -0.21147486,  1.18477223],
                      [-0.31146359, -1.88214137, -0.37489443, -0.58475914, -1.57121651]]) #matriz con probabilidades para calcular el hash de la tabla hash

T=projections.T #matriz transpuerta de projections

#np.random.seed(47)
r=13 #largo del hash , equivale a la cantidad de buckets=2^r
b=2**r
print(b) #cantidad de buckets en la tabla hash
dim=5# dimension de la data
prob=np.random.randn(r, dim) # dimension de vector con dimension 
#T=prob.T
#print (prob)
M=prob.T
codigo_hash1=hashing(vec1,T)
codigo_hash2=hashing(vec2,T)
codigo_hash3=hashing(vec3,T)
print(codigo_hash1,codigo_hash2,codigo_hash3)

table_hash=dict() #sonn varias tablas hash , si coincide en su valor de hash en 1 de las tablas , entonces son vecinos 
L=list()
id1="12345"
id2="asdfgh"

vectores_qls=[(id1,[3,4,9,0,0]),(id2,[3,4,10,7,4])]
print (cossim(vectores_qls[0][1],vectores_qls[1][1]))

for vector_ql in vectores_qls:
    codigo_hash=hashing(vector_ql[1],M)  #mientras mas cercanos sean mas probabilidad tienen de tener el mismo hashing
    if codigo_hash in table_hash:
        table_hash[codigo_hash].append(vector_ql)
    else:
        L=list()
        table_hash[codigo_hash]=L
        table_hash[codigo_hash].append(vector_ql) 
    print(codigo_hash)

#print (table_hash["10"]) 
os.system('cls')

print(dataset_array)