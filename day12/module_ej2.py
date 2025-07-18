import random
import string

# 1. Función que retorna una lista con N colores hexadecimales aleatorios
def list_of_hexa_colors(n):
    colors = []
    chars = '0123456789abcdef'
    for _ in range(n):
        color = '#'
        for _ in range(6):
            color += random.choice(chars)
        colors.append(color)
    return colors

print(list_of_hexa_colors(3))
print(list_of_hexa_colors(1))

# 2. Función que retorna una lista con N colores RGB aleatorios
def list_of_rgb_colors(n):
    colors = []
    for _ in range(n):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        colors.append(f'rgb({r},{g},{b})')
    return colors

print(list_of_rgb_colors(3))
print(list_of_rgb_colors(1))

# 3. Función que genera colores hexadecimales o RGB según el tipo y la cantidad que recibe
def generate_colors(color_type, n):
    if color_type == 'hexa':
        return list_of_hexa_colors(n)
    elif color_type == 'rgb':
        return list_of_rgb_colors(n)
    else:
        return 'Tipo no soportado'

print(generate_colors('hexa', 3))
print(generate_colors('hexa', 1))
print(generate_colors('rgb', 3))
print(generate_colors('rgb', 1))
