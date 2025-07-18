ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Ordenar la lista
ages.sort()
print("Lista ordenada:", ages)

# Encontrar min y max
min_age = ages[0]
max_age = ages[-1]
print("Edad mínima:", min_age)
print("Edad máxima:", max_age)

# Agregar min y max otra vez a la lista
ages.append(min_age)
ages.append(max_age)
print("Lista después de agregar min y max otra vez:", ages)

# Encontrar la mediana
n = len(ages)
if n % 2 == 0:
    median = (ages[n//2 - 1] + ages[n//2]) / 2
else:
    median = ages[n//2]
print("Mediana:", median)

# Encontrar promedio
average = sum(ages) / n
print("Promedio:", average)

# Rango (max - min)
range_ages = max_age - min_age
print("Rango:", range_ages)

# Comparar |min - promedio| y |max - promedio|
diff_min = abs(min_age - average)
diff_max = abs(max_age - average)
print("Diferencia |min - promedio|:", diff_min)
print("Diferencia |max - promedio|:", diff_max)

# Lista de países
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']

# País(es) del medio
n_countries = len(countries)
if n_countries % 2 == 0:
    middle_countries = countries[n_countries//2 - 1 : n_countries//2 + 1]
else:
    middle_countries = [countries[n_countries//2]]
print("País(es) del medio:", middle_countries)

# Dividir la lista de países en dos mitades
if n_countries % 2 == 0:
    first_half = countries[:n_countries//2]
    second_half = countries[n_countries//2:]
else:
    first_half = countries[:(n_countries//2) + 1]
    second_half = countries[(n_countries//2) + 1:]
print("Primera mitad:", first_half)
print("Segunda mitad:", second_half)

# Unpacking primeros tres países y resto
first, second, third, *scandic = countries
print("Primer país:", first)
print("Segundo país:", second)
print("Tercer país:", third)
print("Países escandinavos:", scandic)
