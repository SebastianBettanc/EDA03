import os
import csv
from collections import deque 

def read_dataset(archive): #app 35k datos , por archivo dejaremos 24,5k entrenamiento ,app 10k pruebas
    path=os.path.abspath(archive)# funcion get para instalar #70% de las lineas es para entrenar (le paso pixeles y paso el valor esperado (0 a 9), el otro 30% de los casos le paso pixeles)
    file=open(path,"r")                # y me retorna el numero de que cree que es
    reader=csv.reader(file)
    next(reader)
    x=0
    k=0
    training=list()
    tests_p=list()

    for line in reader:
        
        #print (line)
        #
        # training=list()
        #
        #line=[400,1,2,3,4,5,6,7,8,9]
        #
          

        if x<2000:
            
            line_num=[int(i) for i in line]

            aux=deque((line_num))
            estimate_value=aux.popleft()
            pixels=list(aux)
            test=(estimate_value,pixels)

            training.append(test)

            x+=1

        elif x>=2000 and x<2010:
            x+=1
        else:
            break  
   


    file.close()

    return training