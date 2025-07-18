# Nivel 2 - Ejercicios con tuplas y listas

# Suponiendo que tenemos family_members de nivel 1
siblings = ('Juan', 'Pedro', 'Ana', 'Luisa')
parents = ('Carlos', 'María')
family_members = siblings + parents

# 1. Desempaquetar siblings y parents de family_members
# Sabemos que los primeros 4 son siblings y los últimos 2 son parents
siblings_unpack = family_members[:4]
parents_unpack = family_members[4:]
print("Siblings desempaquetados:", siblings_unpack)
print("Parents desempaquetados:", parents_unpack)

# 2. Crear tuplas de frutas, verduras y productos animales
fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('tomato', 'potato', 'cabbage', 'onion', 'carrot')
animal_products = ('milk', 'egg', 'meat')

# Unir las tres tuplas en food_stuff_tp
food_stuff_tp = fruits + vegetables + animal_products
print("Food stuff tuple:", food_stuff_tp)

# 3. Cambiar la tupla food_stuff_tp a lista food_stuff_lt
food_stuff_lt = list(food_stuff_tp)
print("Food stuff list:", food_stuff_lt)

# 4. Sacar el o los items del medio de food_stuff_tp o food_stuff_lt
# Para esto, primero obtenemos el índice medio
mid_index = len(food_stuff_lt) // 2
# Si es par, hay dos items en medio, si es impar solo uno
if len(food_stuff_lt) % 2 == 0:
    middle_items = food_stuff_lt[mid_index-1:mid_index+1]
else:
    middle_items = [food_stuff_lt[mid_index]]
print("Items del medio:", middle_items)

# 5. Sacar los primeros tres y últimos tres items de food_stuff_lt
first_three = food_stuff_lt[:3]
last_three = food_stuff_lt[-3:]
print("Primeros tres items:", first_three)
print("Últimos tres items:", last_three)

# 6. Borrar la tupla food_stuff_tp completamente
del food_stuff_tp
# print(food_stuff_tp)  # Esto causaría un error porque ya fue borrada

# 7. Verificar si un item existe en una tupla
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
print("¿Estonia es país nórdico?", 'Estonia' in nordic_countries)
print("¿Iceland es país nórdico?", 'Iceland' in nordic_countries)
