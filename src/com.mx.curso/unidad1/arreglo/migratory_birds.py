
n=int(input("Número de observaciones: "))
aves=list(map(int, input("IDs de las aves: ").split()))

# Contar cuántas veces aparece cada tipo de ave
conteo={}
for ave in aves:
    if ave in conteo:
        conteo[ave] += 1
    else:
        conteo[ave] = 1

# Encontrar la frecuencia más alta
maximo=max(conteo.values())

# Filtrar los IDs que tienen esa frecuencia
tipos_maximos=[ave for ave, cantidad in conteo.items() if cantidad == maximo]

# Tomar el menor ID en caso de empate
resultado=min(tipos_maximos)

print(resultado)
