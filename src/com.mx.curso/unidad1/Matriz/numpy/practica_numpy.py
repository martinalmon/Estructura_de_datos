import numpy as np 

datos=np.array([
    [10.9,9.1,20.1,30.1],
    [5.9,9.1,20.9,3.1],
    [10.9,9.1,20.1,30.1],
    [10.9,9.1,20.1,30.1],
    [10.9,9.1,20.1,30.1],
    [10.9,9.1,20.1,30.1],
    [10.9,9.1,20.1,30.1],
    [7.9,9.1,20.1,30.1],
    [10.9,9.1,20.1,30.1],
    [10.9,9.1,10.1,30.1]
])

print("datos originales")
print(datos)

datos[5]= [99.99,99.99,99.99,99.99]
datos[0,1]=np.nan
datos=[5,2]=np.nan
datos=[9,3]=np.nan
print("----DATOS CON ERRORES------------", datos)
datos_sin_errores=np.delete(datos,6,axis=0)
print("---------------datos sin errores------",datos_sin_errores)
media_columna=np.nanmean(datos_sin_errores,axis=0)
#llenar valores donde se encuntran nan por medio de cada columna 
for i in range(datos.shape[0]):
    for j in range(datos.shape[1]):
        if np.isnan(datos[i,j]):
            datos[i,j]=media_columna[j]

print("---------datos sin errores y con nan reemplazados---------",datos)


