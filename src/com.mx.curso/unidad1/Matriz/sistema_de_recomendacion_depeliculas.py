
# Crear la matriz de calificaciones
usuarios = int(input("Número de usuarios: "))
peliculas = int(input("Número de películas: "))

matriz = []  # matriz vacía

print("\nIngresa las calificaciones (del 1 al 5):")
for i in range(usuarios):
    fila = []
    for j in range(peliculas):
        calificacion = int(input(f"Usuario {i+1}, Película {j+1}: "))
        # Validar que esté entre 1 y 5
        while calificacion < 1 or calificacion > 5:
            print(" Solo se permiten valores entre 1 y 5.")
            calificacion = int(input(f"Usuario {i+1}, Película {j+1}: "))
        fila.append(calificacion)
    matriz.append(fila)

# matriz
print("\n--- MATRIZ DE CALIFICACIONES ---")
for fila in matriz:
    print(fila)

# promedio 
pelicula = int(input("\nIngresa el número de película para calcular su promedio: ")) - 1
while pelicula < 0 or pelicula >= peliculas:
    pelicula = int(input("Número inválido. Ingresa un número válido: ")) - 1

suma = 0
for i in range(usuarios):
    suma += matriz[i][pelicula]
promedio = suma / usuarios

print(f"Promedio de calificación de la película {pelicula + 1}: {promedio:.2f}")


usuario = int(input("\nIngresa el número de usuario para ver sus calificaciones: ")) - 1
while usuario < 0 or usuario >= usuarios:
    usuario = int(input("Número inválido. Ingresa un número válido: ")) - 1

vector_usuario = matriz[usuario]

print(f"\nCalificaciones del usuario {usuario + 1}: {vector_usuario}")
