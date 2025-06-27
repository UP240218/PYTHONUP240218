# 1. Declarar lista vacía
empty_list = []

# 2. Lista con más de 5 ítems
my_list = ['manzana', 'pera', 'uvas', 'naranja', 'kiwi', 'melón']

# 3. Longitud de la lista
length = len(my_list)  # 6

# 4. Primer, medio, último elemento
first_item = my_list[0]
middle_item = my_list[len(my_list)//2]  # índice 3 → 'naranja'
last_item = my_list[-1]

# 5. mixed_data_types con info personal
mixed_data_types = ['TuNombre', 30, 1.75, False, 'MiCiudad']

# 6. it_companies inicial
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# 7.
print(it_companies)

# 8. Número de compañías
num_companies = len(it_companies)

# 9. Primero, medio, último
first = it_companies[0]
middle = it_companies[len(it_companies)//2]  # índice 3 → 'Apple'
last = it_companies[-1]

# 10. Modificar una compañía (por ej. cambiar 'IBM' por 'IBM Corp')
it_companies[it_companies.index('IBM')] = 'IBM Corp'

# 11. Añadir al final
it_companies.append('Netflix')

# 12. Insertar en medio
middle_index = len(it_companies)//2
it_companies.insert(middle_index, 'Spotify')

# 13. Cambiar uno a mayúsculas (ej. Google)
idx = it_companies.index('Google')
it_companies[idx] = it_companies[idx].upper()

# 14. Unir con '#; ' como separador
joined = '#; '.join(it_companies)

# 15. Verificar existencia
exists = 'Amazon' in it_companies  # True o False

# 16. Ordenar con sort()
it_companies.sort()

# 17. Invertir orden con reverse()
it_companies.reverse()

# 18. Primeras 3
first_three = it_companies[:3]

# 19. Últimas 3
last_three = it_companies[-3:]

# 20. Compañía(s) del medio
mid = len(it_companies)//2
if len(it_companies) % 2 == 0:
    middle_companies = it_companies[mid-1:mid+1]
else:
    middle_companies = [it_companies[mid]]

# 21. Eliminar la primera
it_companies.pop(0)

# 22. Eliminar la(s) del medio
if len(it_companies) % 2 == 0:
    m = len(it_companies)//2
    del it_companies[m-1:m+1]
else:
    m = len(it_companies)//2
    del it_companies[m]

# 23. Eliminar la última
it_companies.pop(-1)

# 24. Eliminar todas
it_companies.clear()

# 25. Destruir la lista
del it_companies

# 26. Unir front_end y back_end
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
joined_lists = front_end + back_end

# 27. Copiar en full_stack e insertar Python y SQL después de 'Redux'
full_stack = joined_lists.copy()
idx = full_stack.index('Redux') + 1
full_stack.insert(idx, 'Python')
full_stack.insert(idx+1, 'SQL')



# 1. Lista de edades
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Ordenar, mínimo y máximo
ages.sort()
min_age = ages[0]
max_age = ages[-1]

# Agregar min y max
ages.append(min_age)
ages.append(max_age)

# Mediana
n = len(ages)
if n % 2 == 0:
    med = (ages[n//2 - 1] + ages[n//2]) / 2
else:
    med = ages[n//2]

# Promedio
avg = sum(ages) / n

# Rango de edades
range_age = max_age - min_age

# Comparar |min-avg| y |max-avg|
diff1 = abs(min_age - avg)
diff2 = abs(max_age - avg)

# 2. País(es) del medio en lista countries
countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']
mid = len(countries)//2
if len(countries) % 2 == 0:
    middle_countries = countries[mid-1:mid+1]
else:
    middle_countries = [countries[mid]]

# 3. Dividir countries en dos mitades
half = (len(countries)+1)//2
first_half = countries[:half]
second_half = countries[half:]

# 4. Unpack con lista dada
c_list = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
first1, first2, first3, *scandic = c_list
