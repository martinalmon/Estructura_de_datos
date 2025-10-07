# Ejercicio 7

# Crear una matriz vacía de 5x5
tablero = []

print("Ingresa los valores del tablero (0 = vacío, 1 = obstáculo):")

for i in range(5):
    fila = []
    for j in range(5):
        valor = int(input(f"Fila {i+1}, Columna {j+1}: "))
        # Validar que el valor sea 0 o 1
        while valor not in [0, 1]:
            print("Solo se permiten 0 o 1.")
            valor = int(input(f"Fila {i+1}, Columna {j+1}: "))
        fila.append(valor)
    tablero.append(fila)


print("\n--- Tablero ---")
for fila in tablero:
    print(fila)


obstaculos_totales = 0
for fila in tablero:
    for celda in fila:
        if celda == 1:
            obstaculos_totales += 1


fila_elegida = int(input("\nElige el número de fila (1 a 5) para contar sus obstáculos: ")) - 1

while fila_elegida < 0 or fila_elegida >= 5:
    fila_elegida = int(input("Fila inválida. Ingresa un número entre 1 y 5: ")) - 1

obstaculos_fila = tablero[fila_elegida].count(1)

print("\n--- Resultados ---")
print("Obstáculos totales en el tablero:", obstaculos_totales)
print(f"Obstáculos en la fila {fila_elegida + 1}:", obstaculos_fila)
