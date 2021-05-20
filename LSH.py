import math as mt
from numpy.core.records import array
import leercsv
import numpy as np
import matplotlib.pyplot as plt
import os
import time
import normalizer

class ProbTable:
    def __init__(self):
        self.prob_tables=list()
    def insert (self,r,dim):
        new_table=np.random.randn(r, dim)
        self.prob_tables.append(new_table)

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

def LSH(numTables,vector_normalized,hashTables,transposed):  #dataset_normalized[0][1]

    knn_data=list()
    knn_id=list()
    S=list()

    for x in range(numTables):

        knn_data.append((hashTables[x][hashing(vector_normalized,transposed[x])]))    #dataset_normalized[0][1] es el vector normalizado de la app que queremos ver sus vecinos
        knn=list()
        for id in knn_data[x]:
            knn.append(id[0])
        knn_id.append(knn)
        S.append(set(knn_id[x]))
    
    neighbours=frozenset().union(*S)

    return neighbours

def create_hashTables(numTables,length,dim,matrix_normalized):

    tables_prob=ProbTable()
    transposed=list()
    hash_tables=list()

    for x in range(numTables):

        hash=dict()
        hash_tables.append(hash)
        tables_prob.insert(length,dim)
        transposed.append(tables_prob.prob_tables[x].T)

        for vector in matrix_normalized:
            hash_code=hashing(vector[1],transposed[x])

            if hash_code in hash_tables[x]:
                hash_tables[x][hash_code].append(vector)
            else:
                L=list()
                hash_tables[x][hash_code]=L
                hash_tables[x][hash_code].append(vector)

    return hash_tables,transposed

######################MAIN################################

#Locality-Sensitive Hashing (LSH), Implementado
