import os
import csv
from collections import deque 

def read_dataset(archive): #app 35k datos , por archivo dejaremos 24,5k entrenamiento ,app 10k pruebas
    path=os.path.abspath(archive)# funcion get para instalar #70% de las lineas es para entrenar (le paso pixeles y paso el valor esperado (0 a 9), el otro 30% de los casos le paso pixeles)
    file=open(path,"r", encoding="utf8")                # y me retorna el numero de que cree que es
    reader=csv.reader(file)
    next(reader)
    x=0
    points=list()

    for line in reader:
        
        x+=1
          

        if x<2:
            
            #toda la linea line_num=[float(i) for i in line] #transformar valores string a float
           #print(line)
           y=2
           #aux=deque((line_num))
           #estimate_value=aux.popleft()
           #pixels=list(aux)
           #test=(estimate_value,pixels)

           #training.append(test)
        else:
            break  
   


    file.close()

    return points