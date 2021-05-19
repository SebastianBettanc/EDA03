import math as mt

from numpy.core.records import array
import leercsv
import numpy as np
import matplotlib.pyplot as plt
import os
import time

def normal_data(data): #dejar los valores entre 0 y 1 para mejorar el calculo de que tan similares son

    genre={"Book":round(1.0/23.0,3), #Normalizar la data 
                "Business":round(2/23.0),
                "Catalogs":round(3/23.0),
                "Education":round(4/23.0),
                "Entertainment":round(5/23.0),
                "Finance":round(6/23.0),
                "Food & Drink":round(7/23.0),
                "Games":round(8/23.0),
                "Health & Fitness":round(9/23.0),
                "Lifestyle":round(10/23.0),
                "Medical":round(11/23.0),
                "Music":round(12/23.0),
                "Navigation":round(13/23.0),
                "News":round(14/23.0),
                "Photo & Video":round(15/23.0),
                "Productivity":round(16/23.0),
                "Reference":round(17/23.0),
                "Shopping":round(18/23.0),
                "Social Networking":round(19/23.0),
                "Sports":round(20/23.0),
                "Travel":round(21/23.0),
                "Utilities":round(22/23.0),
                "Weather":round(23/23.0),

                }
    cont_rating={"12+":0.75,"17+":1,"4+":0.25,"9+":0.5}


    #size_bytes maximo 99992576 , para datos muy dispersos se ocupara dato/datomayor (retorna valores entre 0 y 1)
                            #para datos no tan dispersos o que se repiten poco se usaran diccionarios
    L=list()
    L.append(round((float(data[0])/4025969664.0),3))
    L.append(round((float(data[1])/299.99),3))
    L.append(round((float(data[2])/2974676.0),3))  
    L.append(round((float(data[3])/177050.0),3))
    L.append(round((float(data[4])/5.0),3))
    L.append(round((float(data[5])/5.0),3))
    L.append(cont_rating[data[6]])                        #177050.0
    L.append(genre[data[7]])
    L.append(round((float(data[8])/47.0),3))
    L.append(round((float(data[9])/5.0),3))
    L.append(round((float(data[10])/75.0),3))
    L.append(float(data[11]))

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
dataset=np.array(leercsv.read_dataset(archive))
apps=dict()
alias=dict()

dataset_normalized=list() #contiene (id,vector_normalizado) de cada aplicacion

for app in dataset:
    
    apps[app[0]]=app
    alias[app[0]]=app[0]
    alias[app[1]]=app[1]

    indices=[2,4,5,6,7,8,10,11,12,13,14,15]
    line=list(app[indices])
    
    vector=normal_data(line)
    value=(app[0],vector)
    dataset_normalized.append(value)

#print(dataset_normalized)

#time.sleep(10)


try:
    print (apps[alias['281656475']])
except KeyError:
    print("no existe app con este id o nombre x.x")

r=13 #largo del hash , equivale a la cantidad de buckets=2^r  #b=2**r

dim=12# dimension de la data
prob=np.random.randn(r, dim) # dimension de vector con dimension 
##T=prob.T
##print (prob)
#M=prob.T
#codigo_hash1=hashing(vec1,T)
#codigo_hash2=hashing(vec2,T)
#codigo_hash3=hashing(vec3,T)
#print(codigo_hash1,codigo_hash2,codigo_hash3)
#
#table_hash=dict() #sonn varias tablas hash , si coincide en su valor de hash en 1 de las tablas , entonces son vecinos 
#id1="12345"
#id2="asdfgh"

#vectores_qls=[(id1,[0.01,1,0.001,0.4,0.6,0.7,0,0,0]),(id2,[3,4,1,3,4,3,3,2,2])]
#
#vector_test=[[]]
#print (cossim(vectores_qls[0][1],vectores_qls[1][1]))
#
#for vector_ql in vectores_qls:
#
#    codigo_hash=hashing(vector_ql[1],M)  #mientras mas cercanos sean mas probabilidad tienen de tener el mismo hashing
#    if codigo_hash in table_hash:
#        table_hash[codigo_hash].append(vector_ql)
#    else:
#        L=list()
#        table_hash[codigo_hash]=L
#        table_hash[codigo_hash].append(vector_ql) 
#    print(codigo_hash)

#for vector in dataset:


#print (table_hash["10"]) 
#os.system('cls')



