import numpy as np

#cargar el data set

datos= np.genfromtxt('src/com.mx.curso/unidad1/Matriz/numpy/practica_numpy_1/iris.data',delimiter=',',dtype='object')

print(datos)
#solo sacamos los datos numericos de la db
datos_numericos =np.genfromtxt('src/com.mx.curso/unidad1/Matriz/numpy/practica_numpy_1/iris.data',delimiter=',',usecols=(0,1,2,3))

print ("--------------------------------datos numericos----------------------------",datos_numericos)

#limpiar indices
indices_eliminar=[0,1,2,50]
datos_limpios=np.delete(datos_numericos,indices_eliminar,axis=0)

print("---------------datos limpios-----------",datos_limpios)

datos_limpios[0,0]=np.nan
datos_limpios[4,0]=np.nan
datos_limpios[12,1]=np.nan
datos_limpios[10,2]=np.nan
datos_limpios[10,0]=np.nan
datos_limpios[3,1]=np.nan
datos_limpios[4,3]=np.nan
datos_limpios[12,3]=np.nan
datos_limpios[11,2]=np.nan
datos_limpios[13,0]=np.nan

print("------------datos con faltantes----------",print(datos_limpios))
media_columna=np.nanmean(datos_limpios,axis=0)
for i in range(datos_limpios.shape[0]):
    for j in range(datos_limpios.shape[1]):
        if np.isnan(datos_limpios[i,j]):
            datos[i,j]=media_columna[j]

print("---------media de cada columna--------", media_columna)
