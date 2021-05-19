import os
import csv

def read_dataset(archive): 

    path=os.path.abspath(archive)
    file=open(path,"r", encoding="utf8")              
    reader=csv.reader(file)
    next(reader)

    x=0

    data=list()
    
    for line in reader:
        #if x<3:
            data.append(line[1:])
        #else:
        #    break
        #x+=1
    
    file.close()
    
    return data

