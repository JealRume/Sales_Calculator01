from Registro.RV import obtener_datos_cliente
# Calculos de ventas

def calcular_venta():
    cliente, cantidad, precio_unitario, es_vip = obtener_datos_cliente()

    subtotal = cantidad * precio_unitario
    descuento = 0.0
    if es_vip:
        descuento = subtotal * 0.1  # 10% de descuento para clientes VIP
    total = subtotal - descuento

    return cliente, cantidad, precio_unitario, es_vip, subtotal, descuento, total

