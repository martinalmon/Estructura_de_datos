# Definimos la matriz del inventario
# Cada fila es: [ID, cantidad en stock, precio unitario]
inventario=[
    [1001, 125, 27.99],
    [102, 85, 12.45],
    [101, 50, 20.5],   
    [102, 30, 15.0],   
    [103, 80, 7.5]
]


# Imprimir los datos del inventario antes de la compra de 10 unidades
print("=== Inventario Actual ===")
for fila in inventario:
    print(f"ID: {fila[0]}, Cantidad: {fila[1]}, Precio: {fila[2]}")

# Elegimos un producto específico (por ejemplo, el de índice 1 → producto con ID 102)
indice_producto = 1 

cantidad = inventario[indice_producto][1]
precio = inventario[indice_producto][2]

# Calculamos valor total del producto + iva 

valor_total = cantidad * precio
valor_con_iva=valor_total*1.16
print(f"\nValor total del producto con ID {inventario[indice_producto][0]}: {valor_con_iva}")

# Actualizar cantidad en stock después de vender 10 unidades
inventario[indice_producto][1] -= 10

print("\n=== Inventario después de la venta ===")
for fila in inventario:
    print(f"ID: {fila[0]}, Cantidad: {fila[1]}, Precio: {fila[2]}")
