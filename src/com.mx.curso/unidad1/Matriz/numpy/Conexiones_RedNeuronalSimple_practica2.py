import numpy as np

array= [57, 12 ,89]
np.random.seed(42)
conexiones=[]
neurona=np.random.rand(3,2)*100

for i in array:
    conexiones.append(np.dot(i,neurona))

print (conexiones)
