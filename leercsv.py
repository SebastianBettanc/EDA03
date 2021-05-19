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

    for line in reader:
        
                  
  #      if x<4: #7190

        data.append(line[1:])

 #       else:
#
        #    break  

        #x+=1
    file.close()
    

    return data

#
#A="7+"
#B=A.replace('+','')
#
#print (int(B))

#matrices de datos 

#n = b*r
#n =total set de datos , b= cantidad de buckets , r= cantidad de movies por bucket

#probabilidad de que sean aprecidos = 1-(1-p^r)^b

a=dict()
L=list()
a[11]=L
print(a[11])
a[11].append(3)
a[11].append(5)
print(a[11])