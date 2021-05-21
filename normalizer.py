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


def normalize_vector(vector_no_normalized): #dejar los valores entre 0 y 1 para mejorar el calculo de que tan similares son

    indices=[2,4,5,6,7,8,10,11,12,13,14,15]
    vector=list(vector_no_normalized[indices])

    genre={"Book":(0.0), #Normalizar la vector 
                "Business":1/22.0,
                "Catalogs":2/22.0,
                "Education":3/22.0,
                "Entertainment":4/22.0,
                "Finance":5/22.0,
                "Food & Drink":6/22.0,
                "Games":7/22.0,
                "Health & Fitness":8/22.0,
                "Lifestyle":9/22.0,
                "Medical":10/22.0,
                "Music":11/22.0,
                "Navigation":12/22.0,
                "News":13/22.0,
                "Photo & Video":14/22.0,
                "Productivity":15/22.0,
                "Reference":16/22.0,
                "Shopping":17/22.0,
                "Social Networking":18/22.0,
                "Sports":19/22.0,
                "Travel":20/22.0,
                "Utilities":21/22.0,
                "Weather":1.0

                }

    cont_rating={"12+":2.3/3.0,"17+":1.0,"4+":0.0,"9+":1.0/3.0}


    #size_bytes maximo 99992576 , para datos muy dispersos se ocupara dato/datomayor (retorna valores entre 0 y 1)
                            #para datos no tan dispersos o que se repiten poco se usaran diccionarios
    L=list()
    L.append(float(vector[0])/4025969664.0) #size_bytes
    L.append(float(vector[1])/299.99)#"price" L.append(((float(vector[1])/299.99),3))
    L.append(float(vector[2])/2974676.0) #"ratingcounttot" 
    L.append(float(vector[3])/177050.0)#"ratingcountver" vector[3])/177050.0)
    L.append(float(vector[4])/5.0)#float(vector[4])/5.0
    L.append(float(vector[5])/5.0)#float(vector[5])/5.0
    L.append(cont_rating[vector[6]])                        #177050.0
    L.append(genre[vector[7]])
    L.append(float(vector[8])/47.0)#(vector[8])/47.0)
    L.append(float(vector[9])/5.0)#(vector[9])/5.0)
    L.append(float(vector[10])/75.0)#(vector[10])/75.0)
    L.append(float(vector[11]))

    return L

def normalize_matrix(matrix):

    data_normalized=list()
    apps=dict()
    alias=dict()

    for app in matrix: # q vector

        apps[app[0]]=app
        alias[app[0]]=app[0]
        alias[app[1]]=app[1]
        vector=normalize_vector(app)

        value=(app[0],vector)
        data_normalized.append(value)    

    return data_normalized,apps,alias
