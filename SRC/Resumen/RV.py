# Resumen de venta
from Calculo.CC import calcular_venta

cliente, cantidad, precio_unitario, es_vip, subtotal, descuento, total = calcular_venta()

def imprimir_resumen_venta():
    print("\n--- Resumen de Venta ---")
    print(f"Cliente: {cliente}")
    print(f"Cantidad: {cantidad}")
    print(f"Precio unitario: ${precio_unitario:.2f}")
    print(f"Subtotal: ${subtotal:.2f}")
    if es_vip:
        print(f"Descuento VIP: ${descuento:.2f}")
    print(f"Total a pagar: ${total:.2f}")
