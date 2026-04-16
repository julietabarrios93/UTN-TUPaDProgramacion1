# Ejercicio 1— “Caja del Kiosco”


# Requisitos
# 1. Pedir nombre del cliente (solo letras, validar con .isalpha() en while).
# • No aceptar vacío en nombre (si queda vacío, es error).

nombre = input("Ingrese su nombre: ") 
while nombre == "" or not nombre.isalpha(): 
    nombre = input("Error, nombre inválido ingrese un nombre sólo letras: ")

# 2. Pedir cantidad de productos a comprar (número entero positivo, validar con
# .isdigit() en while).
# • Cantidad > 0 (si ingresa 0, volver a pedir).


cantidad = input("Ingrese la cantidad de productos a comprar: ")
while not cantidad.isdigit() or int(cantidad) <= 0:
    cantidad = input("Error, cantidad inválida ingrese un nombre sólo numeros enteros: ")

cantidad=int(cantidad)
total_sin_descuentos=0
total_con_descuentos=0
ahorro_total=0

print(f"Cliente: {nombre}")
print(f"Cantidad: {cantidad}")

# 3. Por cada producto (usar for):

for i in range(1, cantidad+1):

    # Pedir precio (entero, validar .isdigit()).

    precio = input(f"Producto {i} - Precio: ")
    while not precio.isdigit(): 
        precio = input("Error, ingrese un precio entero para el producto: ")

    precio=int(precio)

    # Pedir si tiene descuento S/N (validar con while, aceptar s o n en
    # cualquier mayuscula/minuscula).

    descuento = input("¿Tiene descuento? Elegir S/N: ")
    while not descuento in "SsNn":
        descuento = input("Error, ingrese una opcion valida S para SÍ o N para NO: ")

    # Si tiene descuento: aplicar 10% al precio de ese producto.
    if descuento in "Ss":
        ahorro = precio * 0.10
        precio_con_descuento = precio - ahorro
    else:
        ahorro=0
        precio_con_descuento = precio
    total_sin_descuentos+=precio
    total_con_descuentos+=precio_con_descuento
    ahorro_total+=ahorro
    print(f"Producto {i} - Precio: {precio} Descuento (S/N): {descuento}")
    

promedio_por_producto = total_con_descuentos/cantidad 

# 4. Al final mostrar:
# Total sin descuentos
# Total con descuentos
# Ahorro total
# Promedio por producto (usar float y formatear con :.2f:

print("----------------------------------------------")
print(f"Total sin descuentos: ${total_sin_descuentos}")
print(f"Total con descuentos: ${total_con_descuentos}")
print(f"Ahorro: ${ahorro_total}")
print(f"Promedio por producto: ${promedio_por_producto:.2f}")
