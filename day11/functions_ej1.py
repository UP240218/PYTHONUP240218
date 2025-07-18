# 1. Sumar dos números
def add_two_numbers(a, b):
    return a + b

print(add_two_numbers(3, 7))  # 10


# 2. Área de un círculo
def area_of_circle(r):
    pi = 3.1416
    return pi * r * r

print(area_of_circle(5))  # 78.54


# 3. Sumar cualquier cantidad de números
def add_all_nums(*numeros):
    total = 0
    for n in numeros:
        if not isinstance(n, (int, float)):
            return "Error: todos los elementos deben ser números"
        total += n
    return total

print(add_all_nums(1, 2, 3, 4))         # 10
print(add_all_nums(1, 'hola', 3))       # Error


# 4. Convertir de Celsius a Fahrenheit
def convert_celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

print(convert_celsius_to_fahrenheit(0))    # 32.0
print(convert_celsius_to_fahrenheit(25))   # 77.0


# 5. Verificar la estación del año
def check_season(month):
    month = month.lower()
    if month in ['december', 'january', 'february']:
        return 'Winter'
    elif month in ['march', 'april', 'may']:
        return 'Spring'
    elif month in ['june', 'july', 'august']:
        return 'Summer'
    elif month in ['september', 'october', 'november']:
        return 'Autumn'
    else:
        return 'Mes no válido'

print(check_season('April'))  # Spring


# 6. Calcular pendiente de una recta (slope)
def calculate_slope(x1, y1, x2, y2):
    if x2 - x1 == 0:
        return "Indefinida (división por cero)"
    return (y2 - y1) / (x2 - x1)

print(calculate_slope(2, 3, 6, 11))  # 2.0


# 7. Resolver ecuación cuadrática ax² + bx + c = 0
def solve_quadratic_eqn(a, b, c):
    import math
    discriminante = b**2 - 4*a*c
    if discriminante < 0:
        return "No hay soluciones reales"
    elif discriminante == 0:
        x = -b / (2 * a)
        return [x]
    else:
        x1 = (-b + math.sqrt(discriminante)) / (2 * a)
        x2 = (-b - math.sqrt(discriminante)) / (2 * a)
        return [x1, x2]

print(solve_quadratic_eqn(1, -3, 2))  # [2.0, 1.0]


# 8. Imprimir todos los elementos de una lista
def print_list(lista):
    for item in lista:
        print(item)

print_list(['manzana', 'banana', 'pera'])


# 9. Invertir lista usando bucle
def reverse_list(arr):
    reversed_arr = []
    for i in range(len(arr) - 1, -1, -1):
        reversed_arr.append(arr[i])
    return reversed_arr

print(reverse_list([1, 2, 3, 4, 5]))         # [5, 4, 3, 2, 1]
print(reverse_list(["A", "B", "C"]))         # ['C', 'B', 'A']


# 10. Capitalizar elementos de una lista
def capitalize_list_items(items):
    capitalized = []
    for i in items:
        capitalized.append(i.capitalize())
    return capitalized

print(capitalize_list_items(['pera', 'manzana', 'banana']))


# 11. Agregar ítem a una lista
def add_item(lista, item):
    lista.append(item)
    return lista

print(add_item(['Tomate', 'Papa'], 'Cebolla'))


# 12. Eliminar ítem de una lista
def remove_item(lista, item):
    if item in lista:
        lista.remove(item)
    return lista

print(remove_item(['Tomate', 'Papa', 'Cebolla'], 'Papa'))


# 13. Sumar del 0 hasta un número dado
def sum_of_numbers(n):
    total = 0
    for i in range(n + 1):
        total += i
    return total

print(sum_of_numbers(5))   # 15
print(sum_of_numbers(10))  # 55


# 14. Sumar impares hasta un número
def sum_of_odds(n):
    total = 0
    for i in range(n + 1):
        if i % 2 != 0:
            total += i
    return total

print(sum_of_odds(10))  # 25


# 15. Sumar pares hasta un número
def sum_of_even(n):
    total = 0
    for i in range(n + 1):
        if i % 2 == 0:
            total += i
    return total

print(sum_of_even(10))  # 30
