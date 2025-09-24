#creamos un array simple que sera nuestro vector 

array= [3.5,4,5.5,7,7.9]
suma=sum(array)
normalizados=[]
print(suma)

for i in array:
    normalizados.append(i/suma)

print(f"arreglo original:\n{array} \n datos normalizados{normalizados}")