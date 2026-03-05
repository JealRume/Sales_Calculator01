# Calculos de ventas

def calcular_totales(cantidad, precio_unitario, es_vip):
    subtotal = cantidad * precio_unitario
    descuento = 0.0

    if es_vip:
        descuento = subtotal * 0.1  # 10% de descuento para clientes VIP
    total = subtotal - descuento

    return subtotal, descuento, total


