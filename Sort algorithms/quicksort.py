#Metodo ordenamiento
#A partir de un array no ordenado
#Elijo un elemento al azar (pivot)
#Ordeno los elementos mayores al pivot y los pongo arriba
#Ordeno los elementos menores al pivot y los pongo abajo

import random as rn

arr=[1,1,2,5,4,5,4,2,1,1,7,8,5,7,4,31,-1,2,13,0,5] #Array a ordenar

def quicksort(array):

    mayor=[]
    menor=[]
    igual=[]

    if len(array) > 1: 
      

        ran = rn.choice(array) #Elijo un elemento al azar
	pivot = ran
        #pivot = array[0]
        #print pivot
        #print len(array)

        

        for i in array:
            if i > pivot:
                mayor=mayor+[i]
            elif i < pivot:
                menor=menor+[i]
            elif i == pivot:
                igual=igual+[i]

        return quicksort(mayor)+igual+quicksort(menor)

    else:
        return array
        
    
print quicksort(arr)
