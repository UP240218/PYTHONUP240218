# Nivel 2 - Ejercicio 1: Suma de todos los números del 0 al 100
suma_total = 0
for i in range(101):
    suma_total += i
print("La suma de todos los números del 0 al 100 es:", suma_total)

# Nivel 2 - Ejercicio 2: Suma de todos los pares y suma de todos los impares
suma_pares = 0
suma_impares = 0

for i in range(101):
    if i % 2 == 0:
        suma_pares += i
    else:
        suma_impares += i

print("La suma de todos los números pares del 0 al 100 es:", suma_pares)
print("La suma de todos los números impares del 0 al 100 es:", suma_impares)
