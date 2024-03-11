import math

# r y g 
r = float(input("Ingrese el radio (en metros): "))
g = float(input("Ingrese la constante gravitacional g (en m/s²): "))

# Calcular la velocidad de escape
v = math.sqrt(2 * g * r)

# Mostrar la velocidad de escape
print(f"La velocidad de escape es: {v} [m/s]")