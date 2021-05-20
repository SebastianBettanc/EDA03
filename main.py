import os
import time
import leercsv
import numpy as np
import LSH
import normalizer

def get_app(apps,alias,key): #'281656475'

    try:
        print (apps[alias[key]])
        return apps[alias[key]]
    except KeyError:
        print("no existe app con este id o nombre x.x")
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

##############################################
##################### def variables########### 

k,dim,hash_lenght=3,12,300

os.system('cls')

V=main(k,dim,hash_lenght)
apps,alias,hashTables,T_list,matrix=V[0],V[1],V[2],V[3],V[4]

vector_t=matrix[0][1]

start = time.time()
neighbours=LSH.LSH(k,vector_t,hashTables,T_list)
end = time.time()
print("tiempo de ejecuion para buscar vecinos en LSH: ",round(end - start,5)," segundos")


#print(len(neighbours))


get_app(apps,alias,'281656475')

