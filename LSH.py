import math as mt
from numpy.core.records import array
import leercsv
import numpy as np
import matplotlib.pyplot as plt
import os
import time

class ProbTable:
    def __init__(self):
        self.prob_tables=list()
    def insert (self,r,dim):
        new_table=np.random.randn(r, dim)
        self.prob_tables.append(new_table)

def normal_data(data): #dejar los valores entre 0 y 1 para mejorar el calculo de que tan similares son

    genre={"Book":(1.0/23.0), #Normalizar la data 
                "Business":2/23.0,
                "Catalogs":3/23.0,
                "Education":4/23.0,
                "Entertainment":5/23.0,
                "Finance":6/23.0,
                "Food & Drink":7/23.0,
                "Games":8/23.0,
                "Health & Fitness":9/23.0,
                "Lifestyle":10/23.0,
                "Medical":11/23.0,
                "Music":12/23.0,
                "Navigation":13/23.0,
                "News":14/23.0,
                "Photo & Video":15/23.0,
                "Productivity":16/23.0,
                "Reference":17/23.0,
                "Shopping":18/23.0,
                "Social Networking":19/23.0,
                "Sports":20/23.0,
                "Travel":21/23.0,
                "Utilities":22/23.0,
                "Weather":23/23.0,

                }

    cont_rating={"12+":0.75,"17+":1,"4+":0.25,"9+":0.5}


    #size_bytes maximo 99992576 , para datos muy dispersos se ocupara dato/datomayor (retorna valores entre 0 y 1)
                            #para datos no tan dispersos o que se repiten poco se usaran diccionarios
    L=list()
    L.append(float(data[0])/4025969664.0) #size_bytes
    L.append(float(data[1])/299.99)#"price" L.append(((float(data[1])/299.99),3))
    L.append(float(data[2])/2974676.0) #"ratingcounttot" 
    L.append(float(data[3])/177050.0)#"ratingcountver" data[3])/177050.0)
    L.append(float(data[4])/5.0)#float(data[4])/5.0
    L.append(float(data[5])/5.0)#float(data[5])/5.0
    L.append(cont_rating[data[6]])                        #177050.0
    L.append(genre[data[7]])
    L.append(float(data[8])/47.0)#(data[8])/47.0)
    L.append(float(data[9])/5.0)#(data[9])/5.0)
    L.append(float(data[10])/75.0)#(data[10])/75.0)
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

def normalize_matrix(matrix):

    data_normalized=list()
    apps=dict()
    alias=dict()

    for app in matrix:
        apps[app[0]]=app
        alias[app[0]]=app[0]
        alias[app[1]]=app[1]

        indices=[2,4,5,6,7,8,10,11,12,13,14,15]
        line=list(app[indices])
        vector=normal_data(line)
        value=(app[0],vector)

        data_normalized.append(value)    


    return data_normalized,apps,alias    

def LSH(numTables,vector_normalized,hashTables,transposed):  #dataset_normalized[0][1]

    
    
    knn_data=list()
    knn_id=list()

    for x in range(numTables):

        knn_data.append((hashTables[x][hashing(vector_normalized,transposed[x])]))    #dataset_normalized[0][1] es el vector normalizado de la app que queremos ver sus vecinos
        knn=list()
        for id in knn_data[x]:
            knn.append(id[0])
        knn_id.append(knn)

    conjunt_A=set(knn_id[0])
    conjunt_B=set(knn_id[1])
    conjunt_C=set(knn_id[2])

    neighbours=list(conjunt_A.union(conjunt_B,conjunt_C))

    
    print(len(knn_id[0]),len(knn_id[1]),len(knn_id[2]))
    
    return neighbours

def get_app(apps,alias,key): #'281656475'

    try:
        print (apps[alias[key]])
        return apps[alias[key]]
    except KeyError:
        print("no existe app con este id o nombre x.x")
        return None

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

archive="Desafio3.csv"
dataset=np.array(leercsv.read_dataset(archive))
dataset_n=normalize_matrix(dataset)                       #contiene (id,vector_normalizado) de cada aplicacion
dataset_normalized=dataset_n[0]
apps=dataset_n[1]
alias=dataset_n[2]

os.system('cls')

length=300 #largo del valor hash
dim=12 #dimensiones del vector
k=3 #cantidad de tablas hash que va a crear el algoritmo
tables=create_hashTables(k,length,dim,dataset_normalized)
hashTables=tables[0]
transposed=tables[1]

vector_t=dataset_normalized[0][1]
start = time.time()
neighbours=LSH(k,vector_t,hashTables,transposed)
end = time.time()
print("tiempo de ejecuion para buscar vecinos en LSH: ",round(end - start,5)," segundos")

#print(neighbours)


vectores=list()

if len(neighbours)>2:

    for id in neighbours:
        indices=[2,4,5,6,7,8,10,11,12,13,14,15]
        app=np.array(apps[alias[id]])
        line=list(app[indices])
        vector_id=normal_data(line)
        vectores.append(vector_id)    

    print("distancia coseno")
    print(cossim(vectores[0],vectores[1]))
#end = time.time()

get_app(apps,alias,'281656475')

#print("tiempo de ejecion para buscar vecinos en LSH: ",round(end - start,5)," segundos")
