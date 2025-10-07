# Problema: Angry Professor

t = int(input("Número de casos: "))

for i in range(t):
    n, k = map(int, input("Número de alumnos y umbral: ").split())
    llegadas = list(map(int, input("Tiempos de llegada: ").split()))
    
    # Contar cuántos llegaron a tiempo
    puntuales = 0
    for tiempo in llegadas:
        if tiempo <= 0:
            puntuales += 1
    
    # Decidir si se cancela o no
    if puntuales < k:
        print("YES")  # Se cancela
    else:
        print("NO")   # No se cancela
