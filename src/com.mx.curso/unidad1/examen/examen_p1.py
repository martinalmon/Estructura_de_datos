#se tiene  una matriz cuadrad por ejemplo 3x3 
# y se requierd calcular la diagonal para saber la diferencia absoluta 

dimension= int(input("Tamaño de la matriz: "))

# hacemos la  matriz leyendo línea por línea
matriz=[]
for i in range(dimension):
    fila = input(f"Fila {i+1}: ").split()
    fila = [int(x)for x in fila[:dimension]]
    while len(fila) < dimension:
        faltan = dimension-len(fila)
        print(f"Faltan {faltan} números en esta fila. Ingresa los faltantes:")
        extras = input().split()
        fila += [int(x) for x in extras[:faltan]]
    matriz.append(fila)

#diagonales 
diagonal_principal=0
diagonal_secundaria=0

for i in range(dimension):
    diagonal_principal+=matriz[i][i]
    diagonal_secundaria+=matriz[i][dimension-1-i]

# calculamos  la diferencia absoluta 
diferencia = abs(diagonal_principal-diagonal_secundaria)
print("La diferencia absoluta es:",diferencia)


