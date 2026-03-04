
# Entrada de datos
def obtener_datos_cliente():
    cliente = input("Nombre del cliente: ")
    cantidad = int(input("Cantidad: "))
    precio_unitario = float(input("Precio unitario: "))
    es_vip = input("¿Es cliente VIP? (s/n): ").lower() == 's'
    return cliente, cantidad, precio_unitario, es_vip
