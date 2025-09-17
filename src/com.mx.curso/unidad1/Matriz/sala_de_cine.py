# Inicializamos la matriz del cine con 4 filas y 5 asientos por fila (todo libre = 0)
cine=[[0 for _ in range(5)] for _ in range(4)]

# Función para imprimir el mapa de asientos
def imprimir_cine(cine):
    print("\n=== Mapa de asientos ===")
    for i, fila in enumerate(cine, start=1):
        print(f"Fila {i}: ", end="")
        for asiento in fila:
            print(asiento, end=" ")
        print()  # salto de línea

# Imprimimos el mapa inicial
imprimir_cine(cine)

# Pedimos al usuario que elija fila y asiento
fila=int(input("\nIngresa la fila (1-4): ")) - 1
asiento=int(input("Ingresa el asiento (1-5): ")) - 1

# Validamos que esté dentro del rango y que el asiento esté libre
if 0<=fila<4 and 0<=asiento<5:
    if cine[fila][asiento]==0:
        cine[fila][asiento]=1
        print("\nAsiento reservado correctamente.")
    else:
        print("\n Ese asiento ya estaba ocupado.")
else:
    print("\nFila o asiento fuera de rango.")

# Imprimimos el mapa actualizado
imprimir_cine(cine)

# Contamos los asientos libres (0)
libres=0
for fila in cine:
    for asiento in fila:
        if asiento==0:
            libres+=1

print(f"\nNúmero total de asientos libres: {libres}")
