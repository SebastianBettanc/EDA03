def normalize_vector(vector): #dejar los valores entre 0 y 1 para mejorar el calculo de que tan similares son

    genre={"Book":(1.0/23.0), #Normalizar la vector 
                "Business":2/23.0,
                "Catalogs":3/23.0,
                "Education":4/23.0,
                "Entertainment":5/23.0,
                "Finance":6/23.0,
                "Food & Drink":7/23.0,
                "Games":8/23.0,
                "Health & Fitness":9/23.0,
                "Lifestyle":10/23.0,
                "Medical":11/23.0,
                "Music":12/23.0,
                "Navigation":13/23.0,
                "News":14/23.0,
                "Photo & Video":15/23.0,
                "Productivity":16/23.0,
                "Reference":17/23.0,
                "Shopping":18/23.0,
                "Social Networking":19/23.0,
                "Sports":20/23.0,
                "Travel":21/23.0,
                "Utilities":22/23.0,
                "Weather":23/23.0,

                }

    cont_rating={"12+":0.75,"17+":1,"4+":0.25,"9+":0.5}


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

    for app in matrix:
        apps[app[0]]=app
        alias[app[0]]=app[0]
        alias[app[1]]=app[1]

        indices=[2,4,5,6,7,8,10,11,12,13,14,15]
        line=list(app[indices])
        vector=normalize_vector(line)
        value=(app[0],vector)

        data_normalized.append(value)    


    return data_normalized,apps,alias
