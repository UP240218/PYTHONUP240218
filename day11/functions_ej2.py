# 1. Contar pares e impares hasta un número dado
def evens_and_odds(n):
    evens = 0
    odds = 0
    for i in range(n + 1):
        if i % 2 == 0:
            evens += 1
        else:
            odds += 1
    return f'Los números pares son {evens}. Los impares son {odds}.'

print(evens_and_odds(100))
# Los números pares son 51. Los impares son 50.


# 2. Factorial de un número
def factorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

print(factorial(5))   # 120
print(factorial(0))   # 1


# 3. Verificar si está vacío o no
def is_empty(valor):
    return valor == '' or valor == [] or valor == {} or valor is None

print(is_empty(""))      # True
print(is_empty([]))      # True
print(is_empty("Hola"))  # False


# 4. Calcular promedio
def calculate_mean(lista):
    if len(lista) == 0:
        return 0
    return sum(lista) / len(lista)

# 5. Calcular mediana
def calculate_median(lista):
    lista_ordenada = sorted(lista)
    n = len(lista_ordenada)
    mitad = n // 2
    if n % 2 == 0:
        return (lista_ordenada[mitad - 1] + lista_ordenada[mitad]) / 2
    else:
        return lista_ordenada[mitad]

# 6. Calcular moda
def calculate_mode(lista):
    from collections import Counter
    contador = Counter(lista)
    max_frecuencia = max(contador.values())
    modas = [k for k, v in contador.items() if v == max_frecuencia]
    return modas if len(modas) > 1 else modas[0]

# 7. Calcular rango
def calculate_range(lista):
    return max(lista) - min(lista)

# 8. Calcular varianza
def calculate_variance(lista):
    media = calculate_mean(lista)
    suma_cuadrados = sum((x - media) ** 2 for x in lista)
    return suma_cuadrados / len(lista)

# 9. Calcular desviación estándar
def calculate_std(lista):
    import math
    return math.sqrt(calculate_variance(lista))

# Pruebas con una misma lista:
datos = [4, 5, 1, 2, 7, 5, 5]

print("Media:", calculate_mean(datos))
print("Mediana:", calculate_median(datos))
print("Moda:", calculate_mode(datos))
print("Rango:", calculate_range(datos))
print("Varianza:", calculate_variance(datos))
print("Desviación estándar:", calculate_std(datos))
