#operaciones con matrices utilizando numpy 
import numpy as np 

matriz_A =[[1,2,3],
            [4,6,7],
            [9,9,9]]

matriz_B=[
    [1,4,3],
    [1,6,7],
    [9,4,99]
]

#suma de matrices 
suma=np.add(matriz_A,matriz_B)
print("suma de matrices:\n",suma)

#multiplicacion de matrices 
multiplicacion=np.dot(matriz_A,matriz_B)
print("multiplicacion de matrices:\n", multiplicacion)
