matriz = [
    [0,1,2,1,2,0,1,1],
    [0,1,2,1,2,0,1,1],
    [0,1,2,1,2,0,1,1],
    [0,1,2,1,2,0,1,1],
    [0,1,2,1,2,0,1,1],
    [0,1,2,1,2,0,1,1],
    [0,1,2,1,2,0,1,1],
    [0,1,2,1,2,0,1,1]
]

#Imprimir mapa original
print("Mapa de riesgo original:")
for fila in matriz:
    print(fila)

#Contar áreas de precaución (1) y alto riesgo (2)
precaucion=0
alto_riesgo=0

for fila in matriz:
    for valor in fila:
        if valor==1:
            precaucion+=1
        elif valor==2:
            alto_riesgo+=1

print(f"\nÁreas de precaución (1): {precaucion}")
print(f"Áreas de alto riesgo (2): {alto_riesgo}")

#Actualizar el mapa: todos los 2 → 1
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j]==2:
            matriz[i][j]=1

#Imprimir mapa actualizado
print("\nMapa actualizado (sin alto riesgo):")
for fila in matriz:
    print(fila)
