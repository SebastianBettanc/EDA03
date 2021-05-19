import os
import csv

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
          
        
        if x<4: #7190
            
            
            print(line)
            data*=0         #data.clear() mas rapido en tiempo
            for result in line[1:]:
               data.append(result)
            movies[data[0]]=data
            alias[data[1]]=data[0]
            alias[data[0]]=data[0]
        else:

            break  


    file.close()
    

    return movies,alias

#
#A="7+"
#B=A.replace('+','')
#
#print (int(B))

#matrices de datos 

#n = b*r
#n =total set de datos , b= cantidad de buckets , r= cantidad de movies por bucket

#probabilidad de que sean aprecidos = 1-(1-p^r)^b

