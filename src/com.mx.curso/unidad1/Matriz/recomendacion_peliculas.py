matriz = [
    [5,	5,	4,	5,	5,	1,	5,	5,	3,	5,	3,	4,	4],
    [2,	5,	4,	5,	5,	3,	5,	4,	5,	5,	3,	5,	3],
    [2,	5,	5,	5,	4,	3,	5,	4,	4,	5,	2,	4,	3],
    [4,	5,	4,	5,	5,	4,	4,	5,	5,	5,	3,	4,	2],
    [5,	4,	4,	5,	5,	4,	5,	5,	3,	5,	1,	5,	1],
    [3,	5,	3,	5,	3,	5,	2,	1,	3,	5,	3,	1,	1],
    [2,	4,	5,	3,	5,	2,	5,	3,	3,	4,	1,	3,	2],
    [4,	5,	5,	2,	5,	1,	3,	5,	5,	4,	3,	1,	3],
    [3,	2,	5,	2,	5,	2,	3,	2,	5,	4,	5,	4,	2],
    [3,	5,	2,	5,	3,	1,	1,	5,	1,	5,	3,	1,	5],
    [5,	1,	5,	5,	5,	4,	4,	1,	4,	5,	4,	1,	5],
    [5,	5,	5,	5,	5,	5,	5,	5,	5,	5,	5,	5,	5],
    [5,	4,	3,	5,	5,	1,	4,	2,	3,	5,	2,	1,	5]
]
#imprimir la matriz de calificaciones 
for i in range (len(matriz)):
    for j in range(len(matriz)):
        print(matriz[i][j], end="")
    print()

#promedio de una pelicula 
suma=0
pelicula=1
for i in range (len(matriz)):
    suma += int (matriz[i][pelicula])

print("la suma de calificaciones de pelicula 1 es", suma )
promedio= suma/len(matriz)
print("el promedio de la calificaciones es una ", promedio)

calificacione_usuario0= matriz[0]
print ("calificaciones usuario", calificacione_usuario0)


#ver todas las calificaciones 
calificaiones=[]
promedios=[]
pelicula=0
suma=0

for pelicula in range(len(matriz)):
    
    for l in range (len(matriz)):
        suma= suma+int (matriz [l][pelicula])
        calificaiones.append(suma)

print(calificaiones)
print ("\n","este es el while perrillo ")
while pelicula< len(matriz):
    for l in range (len(matriz)):
        suma= suma+int (matriz [l][pelicula])
        calificaiones.append(suma)
    pelicula+=1

print(calificaiones)

