import os
import csv

def read_dataset(archive): 

    path=os.path.abspath(archive)
    file=open(path,"r", encoding="utf8")              
    reader=csv.reader(file)
    next(reader)
    data=list()
    
    for line in reader:

        data.append(line[1:])

    file.close()
    
    return data

#0  "id" : App ID # no es importante para el vector
#1  "track_name": Nombre de la App # no
#2  "size_bytes": Tamaño (en Bytes) #si              #0 #normalizado
#3  "currency": Moneda  #no
#4  "price": Precio en la moneda #si                  # 1            #normalizado
#5  "ratingcounttot": Cantidad de reseñas (Para todas las versiones) #si             #2 #normalizado
#6  "ratingcountver": Cantidad de reseñas (Para la versión actual) #si                #3 # normalizado
#7  "user_rating" : Promedio de puntaje de las reseñas (Para todas las versiones) #si  #4 #normalizado
#8  "userratingver": Promedio de puntaje de las reseñas (Para la versión actual) #si   #5 # normalizado
#9  "ver" : Ultima version #no
#10 "cont_rating": Rating de contenido #si                             #6 #normalizado
#11 "prime_genre": Género principal #si                             #7 normalizado
#12 "sup_devices.num": Cantidad de dispositivos soportados #si #8 #normalizado
#13 "ipadSc_urls.num": Cantidad de capturas de pantallas por dispositivos #si #9 #normalizado
#14 "lang.num": Cantidad de lenguajes soportados #si #10 #
#15 "vpp_lic": Licencia Vpp activada #si #11
