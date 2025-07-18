# 1. Verificar si un número es primo
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(11))  # True
print(is_prime(15))  # False


# 2. Verificar si todos los elementos en una lista son únicos
def all_unique(lst):
    return len(lst) == len(set(lst))

print(all_unique([1, 2, 3, 4]))  # True
print(all_unique([1, 2, 2, 4]))  # False


# 3. Verificar si todos los elementos en una lista son del mismo tipo
def all_same_type(lst):
    if not lst:
        return True
    tipo = type(lst[0])
    for item in lst:
        if type(item) != tipo:
            return False
    return True

print(all_same_type([1, 2, 3]))         # True
print(all_same_type([1, '2', 3]))       # False


# 4. Verificar si una variable es un nombre válido en Python
import keyword
def is_valid_variable(name):
    if not name.isidentifier():
        return False
    if keyword.iskeyword(name):
        return False
    return True

print(is_valid_variable('my_var'))    # True
print(is_valid_variable('2var'))      # False
print(is_valid_variable('for'))       # False


# 5. Función para obtener los idiomas más hablados en el mundo (usando datos de un archivo)
# Aquí asumiré que el archivo 'countries-data.py' tiene una variable 'countries_data' con los datos.
# Como no tengo acceso directo, haré un ejemplo de cómo sería la función.

def most_spoken_languages(countries_data, top=10):
    language_count = {}
    for country in countries_data:
        for lang in country.get('languages', []):
            language_count[lang] = language_count.get(lang, 0) + 1
    sorted_langs = sorted(language_count.items(), key=lambda x: x[1], reverse=True)
    return sorted_langs[:top]

# Ejemplo de uso (requiere archivo countries-data.py con datos)
# from countries_data import countries_data
# print(most_spoken_languages(countries_data, 10))


# 6. Función para obtener los países más poblados (de nuevo con datos del archivo)
def most_populated_countries(countries_data, top=10):
    sorted_countries = sorted(countries_data, key=lambda c: c.get('population', 0), reverse=True)
    return [(country['name'], country['population']) for country in sorted_countries[:top]]

# Ejemplo de uso:
# print(most_populated_countries(countries_data, 10))

