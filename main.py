import os
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

def distance(v1,v2):

    sum=0
    for i in range(len(v1)):
        sum+=(v1[i]-v2[i])**2

    return mt.sqrt(sum)

def brute_knn(vector_normal,matrix,n):
    knn=list()

    for vector in matrix:                                 
        d=distance(vector_normal,vector[1])

        if len(knn)<n and d!=0:
            value=(vector[0],d)
            knn.append(value)
            knn.sort(key=operator.itemgetter(1))  
                
        elif  len(knn)==n:
            knn.sort(key=operator.itemgetter(1))
            if d<knn[-1][1] and d!=0:
                value=(vector[0],d)
                knn.pop()
                knn.append(value)

    knn.sort(key=operator.itemgetter(1))

    return knn

def lsh_knn(vector,ids,apps,alias,n): #1-distance_cos
    knn=list()

    for id in ids:
        app=get_app(apps,alias,id)
        vector_app=normalizer.normalize_vector(app)
        d=distance(vector,vector_app)

        if len(knn)<n and d!=0:
            value=(id,d)
            knn.append(value)
            knn.sort(key=operator.itemgetter(1))  
                
        elif  len(knn)==n:
            knn.sort(key=operator.itemgetter(1))
            if d<knn[-1][1] and d!=0:
                value=(id,d)
                knn.pop()
                knn.append(value)


    knn.sort(key=operator.itemgetter(1))

    return knn

############################################## ('1097482356'
##################### def variables########### 
os.system('cls')

k,dim,hash_lenght=7,12,300

V=main(k,dim,hash_lenght)
apps,alias,hashTables,T_list,matrix=V[0],V[1],V[2],V[3],V[4]

app=get_app(apps,alias,'281656475') 
vector_id=normalizer.normalize_vector(app)#vector normal dada la id de la app
vector=[0.03, 0.026, 0.007, 0.0001, 0.8, 0.9, 0.0, 0.31, 0.8, 1.0, 0.13, 1.0] #vector random # se puede reemplazar por vector_id para los vecinos
#de un vector dado cualquiera

t1=timeit.default_timer()
set_lsh=list(LSH.LSH(k,vector_id,hashTables,T_list)) #contiene una lista con "posibles vecinos"
neighbours_lsh=lsh_knn(vector_id,set_lsh,apps,alias,10) #ordena la lista de "posibles vecinos" , por distancia y retorna los n mejores (para 10 vecinos, el % de falsos positivos es casi 0)
t2=timeit.default_timer()
print("tiempo de ejecucion para buscar vecinos en LSH: ",t2-t1," segundos")

t3 = timeit.default_timer()
neighbours_brute=brute_knn(vector_id,matrix,10)
t4 = timeit.default_timer()
print("tiempo de ejecucion para buscar vecinos por fuerza bruta : ",t4 - t3," segundos")


print(neighbours_lsh)#impride id y distancia de vecinos por LSH
print("")
print(get_app (apps,alias,'1061610336'))

###
