# utilidades premium

print("Ingrese los siguientes datos para calcular las utilidades del proyecto con usuarios normales y premium:")
P = float(input("Precio de suscripción para usuarios normales (P): "))
Unormal = int(input("Número de usuarios normales (Unormal): "))
Upremium = int(input("Número de usuarios premium (Upremium): "))
GT = float(input("Gastos totales (GT): "))

if P <= 0 or Unormal < 0 or Upremium < 0 or GT < 0:
    print("Advertencia: El precio de suscripción debe ser mayor que cero, los números de usuarios no deben ser negativos, y los gastos totales no deben ser negativos.")

utilidades = (P * Unormal) + (1.5 * P * Upremium) - GT
print(f"Las utilidades del proyecto son: {utilidades}")
