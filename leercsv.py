import os
import csv
from collections import deque 

#def convertir=

def read_dataset(archive): 
    path=os.path.abspath(archive)
    file=open(path,"r", encoding="utf8")              
    reader=csv.reader(file)
    next(reader)
    x=0
    data=list()
    movies=dict()
    alias=dict()

    for line in reader:
        
        x+=1
          
        
        if x<4:
            
            
            print(line)
            data*=0         #metodo para borrar lista mas rapido (mas que data.clear())
            for result in line[1:]:
               data.append(result)
            movies[data[0]]=data
            alias[data[1]]=data[0]
            alias[data[0]]=data[0]
        else:

            break  


    file.close()

    return movies,alias
