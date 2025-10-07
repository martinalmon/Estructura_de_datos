

precisiones = []  # lista vacía para almacenar las precisiones

while True:
    entrada = input("Ingresa la precisión de la época (o 'fin' para terminar): ")
    if entrada.lower() == "fin":
        break
    try:
        valor = float(entrada)
        precisiones.append(valor)
    except ValueError:
        print("Por favor ingresa un número válido o 'fin'.")

if len(precisiones) > 0:
    precision_final = precisiones[-1]
    precision_maxima = max(precisiones)

    print("\n--- Resultados del entrenamiento ---")
    print("Precisión final:", precision_final)
    print("Precisión más alta:", precision_maxima)
else:
    print("No se registraron precisiones.")
