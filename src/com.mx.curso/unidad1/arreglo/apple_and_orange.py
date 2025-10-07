
# Entrada de datos
s,t =map(int, input("Inicio y fin de la casa: ").split())  # límites de la casa
a,b =map(int, input("Posición de los árboles (manzana y naranja): ").split())
m,n =map(int, input("Cantidad de manzanas y naranjas: ").split())

# Distancias que caen las frutas
apples=list(map(int, input("Distancias de las manzanas: ").split()))
oranges=list(map(int, input("Distancias de las naranjas: ").split()))

# Contadores
apples_on_house = 0
oranges_on_house = 0

# Calcular posición final de cada manzana y verificar si cae sobre la casa
for d in apples:
    posicion = a + d
    if s <= posicion <= t:
        apples_on_house += 1

# Calcular posición final de cada naranja
for d in oranges:
    posicion = b + d
    if s <= posicion <= t:
        oranges_on_house += 1

print(apples_on_house)
print(oranges_on_house)
