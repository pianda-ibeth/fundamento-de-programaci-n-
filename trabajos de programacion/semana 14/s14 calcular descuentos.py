#Tarea de Programación: Cálculo de Descuento en Compras

def calcular_descuento(monto_total,porcentaje_descuento = 20):
 descuento= monto_total *(porcentaje_descuento/100)
 return descuento
  # primer llamado
monto=400
descuento=calcular_descuento(monto)
print(f"el monto de la compra es: {monto}, el descuento es de {descuento}")
# segundo llamado
descuento=calcular_descuento(40,10)
print(f"descuento es de {descuento}")
