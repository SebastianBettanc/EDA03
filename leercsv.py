import os
import csv

def read_dataset(archive): 

    path=os.path.abspath(archive)
    file=open(path,"r", encoding="utf8")              
    reader=csv.reader(file)
    next(reader)
    data=list()
    x=0
    
    for line in reader:


        data.append(line[1:])

    file.close()
    
    return data

