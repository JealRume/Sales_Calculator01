from Datos.RV import obtener_datos 
from Calculo.CC import calcular_totales

cliente, cantidad, precio_unitario, es_vip = obtener_datos()


subtotal, descuento, total = calcular_totales(cantidad, precio_unitario, es_vip)

print("\n--- Resumen de Venta ---")
print(f"Cliente: {cliente}")
print(f"Cantidad: {cantidad}")
print(f"Precio unitario: ${precio_unitario:.2f}")
print(f"Subtotal: ${subtotal:.2f}")

if es_vip:
        print(f"Descuento VIP: ${descuento:.2f}")

print(f"Total a pagar: ${total:.2f}")
