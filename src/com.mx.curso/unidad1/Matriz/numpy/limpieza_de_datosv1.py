import numpy as np

#simular una matriz de 12*5 

np.random.seed(42)
datos= np.random.rand(5,5)*100

#simular datos erroneos
datos[0,0]=-999
datos[2,3]=150
print("datos originales:\n,")
print(datos, "\n")

indices_erroneos= [0,2]
datos_limpios= np.delete(datos, indices_erroneos, axis=0)
print("\n","=============", datos_limpios)
