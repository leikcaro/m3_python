#utilidades del proyecto
print("Ingrese los siguientes datos para calcular las utilidades del proyecto:")
#variables
P = float(input("Precio de suscripción (P): "))
U = int(input("Número de usuarios (U): "))
GT = float(input("Gastos totales (GT): "))

#aviso sobre valores negativos o cero que podrían afectar el cálculo
if P <= 0 or U <= 0 or GT < 0:
    print("Advertencia: El precio de suscripción y el número de usuarios deben ser mayores que cero, y los gastos totales no deben ser negativos.")

utilidades = P * U - GT
print(f"Las utilidades del proyecto son: {utilidades}")
