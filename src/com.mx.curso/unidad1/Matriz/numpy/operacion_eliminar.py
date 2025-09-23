import numpy as np
datos= np.array([
    [10,10,10],
    [20,20,20],
    [30,30,30]]
    

)

print("datos originales:\n",datos)

datos_limpios=np.delete(datos,1,axis=0) #elimina la segunda fila 
print("datos despues de eliminar la segunda fila : \n", datos_limpios)

#introducir datos de errores 
datos[0]= [-1,-2,-2]
print("datos con errores introducidos :\n",datos)

valor_negativos= []
for i in range(datos.shape[0]):
    for j in range(datos.shape[1]):
        if datos [i,j] <0:
            valor_negativos.append([i,j])

datos_limpios=np.delete(datos,valor_negativos,axis=0)#eliminar datos negativos 
print("datos limpios despues de eliminar valores negativos", datos_limpios)
