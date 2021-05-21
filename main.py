import os
import time
import leercsv
import numpy as np
import LSH
import normalizer
import math as mt
import operator
import timeit

def get_app(apps,alias,key): #'281656475'

    try:
        return apps[alias[key]]
    except KeyError:
        #print("no existe app con este id o nombre x.x")
        return None

def main(k,dim,length):

    archive="Desafio3.csv"
    dataset=np.array(leercsv.read_dataset(archive))
    dataset_n=normalizer.normalize_matrix(dataset)                       #contiene (id,vector_normalizado) de cada aplicacion
    matrix=dataset_n[0]
    apps=dataset_n[1]
    alias=dataset_n[2]

    tables=LSH.create_hashTables(k,length,dim,matrix)
    hashTables=tables[0]
    transposed=tables[1]

    return apps,alias,hashTables,transposed,matrix

def cossim(v1,v2):#"compute cosine similarity of v1 to v2: (v1 dot v2)/{||v1||*||v2||)" distancia coseno entre dos vectores
    
    sumxx, sumxy, sumyy = 0.0, 0.0, 0.0
    for i in range(len(v1)):
        x = v1[i]; y = v2[i]
        sumxx += x*x
        sumyy += y*y
        sumxy += x*y
    return float(sumxy/mt.sqrt(sumxx*sumyy))

def default(vector_normal,matrix): #buscar vecinos mas cercanos por fuerza bruta

    knn=list()

    for vector in matrix:                                 
        cos_distance=cossim(vector_normal,vector[1])

        if len(knn)<10 and cos_distance!=1:
            value=(vector[0],cos_distance)
            knn.append(value)
            knn.sort(key=operator.itemgetter(1),reverse=True)  
                
        elif  len(knn)==10:
            knn.sort(key=operator.itemgetter(1),reverse=True)
            if cos_distance>=knn[-1][1] and cos_distance!=1:
                value=(vector[0],cos_distance)
                #
                knn.pop()
                knn.append(value)

    knn.sort(key=operator.itemgetter(1),reverse=True)

    return knn

def correction(vector,ids,apps,alias): #1-distance_cos
    knn=list()

    for id in ids:
        app=get_app(apps,alias,id)
        vector_app=normalizer.normalize_vector(app)
        cos_distance=cossim(vector,vector_app)

        if len(knn)<10 and cos_distance!=1:
            value=(id,cos_distance)
            knn.append(value)
            knn.sort(key=operator.itemgetter(1),reverse=True)  
                
        elif  len(knn)==10:
            knn.sort(key=operator.itemgetter(1),reverse=True)
            if cos_distance>=knn[-1][1] and cos_distance!=1:
                value=(id,cos_distance)
                knn.pop()
                knn.append(value)


    knn.sort(key=operator.itemgetter(1),reverse=True)

    return knn



############################################## ('1097482356'
##################### def variables########### 
os.system('cls')

k,dim,hash_lenght=7,12,300

V=main(k,dim,hash_lenght)
apps,alias,hashTables,T_list,matrix=V[0],V[1],V[2],V[3],V[4]

app=get_app(apps,alias,'281656475') 
vector_id=normalizer.normalize_vector(app)#vector normal dada la id de la app
vector=[0.025034521472241278, 0.013300443348111604, 0.007157754323496072, 0.00014685117198531489, 0.8, 0.9, 0.0, 0.3181818181818182, 0.8085106382978723, 1.0, 0.13333333333333333, 1.0] #vector normalizo cualquiera



t1=timeit.default_timer()
set_lsh=list(LSH.LSH(k,vector_id,hashTables,T_list))
neighbours_lsh=correction(vector_id,set_lsh,apps,alias)
t2=timeit.default_timer()
print("tiempo de ejecucion para buscar vecinos en LSH: ",t2-t1," segundos")

t3 = timeit.default_timer()
neighbours_brute=default(vector_id,matrix)
t4 = timeit.default_timer()
print("tiempo de ejecucion para buscar vecinos por fuerza bruta : ",t4 - t3," segundos")

print(neighbours_brute)#imprime id y distancia de vecinos por fuerza bruta
print("")
print(neighbours_lsh)#impride id y distancia de vecions por LSH

###
