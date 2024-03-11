# utilidades con razón

print("Ingrese los siguientes datos para calcular las utilidades del proyecto y la razón respecto al año anterior:")
P = float(input("Precio de suscripción (P): "))
U = int(input("Número de usuarios (U): "))
GT = float(input("Gastos totales (GT): "))
Uanterior = float(input("Utilidades del año anterior (Uanterior): "))

if P <= 0 or U <= 0 or GT < 0 or Uanterior == 0:
    print("Advertencia: El precio de suscripción y el número de usuarios deben ser mayores que cero, los gastos totales no deben ser negativos y las utilidades del año anterior no deben ser cero para evitar división por cero.")

utilidades = P * U - GT
razon = utilidades / Uanterior
print(f"Las utilidades actuales son: {utilidades}")
print(f"La razón entre las utilidades actuales y las del año anterior es: {razon:.2f}")
