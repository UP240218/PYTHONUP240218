# 1. Crear un tuple vacío
empty_tuple = ()

# 2. Tuple con nombres de herman@s (imaginarios)
brothers = ('Carlos', 'Miguel')
sisters = ('Laura', 'Ana')

# 3. Unir brothers + sisters → siblings
siblings = brothers + sisters

# 4. ¿Cuántos hermanos tienes?
num_siblings = len(siblings)

# 5. Modificar siblings para incluir padre y madre → family_members
parents = ('Padre', 'Madre')
family_members = siblings + parents

# 1. Unpack siblings y padres desde family_members
bro1, bro2, sis1, sis2, padre, madre = family_members

# 2. Crear tuples de alimentos y unirlos
fruits = ('apple', 'banana', 'orange')
vegetables = ('carrot', 'pepper', 'onion')
animal_products = ('milk', 'cheese', 'yoghurt')
food_stuff_tp = fruits + vegetables + animal_products

# 3. Convertir el tuple food_stuff_tp a una lista
food_stuff_lt = list(food_stuff_tp)

# 4. Extraer elemento(s) del medio de food_stuff
mid = len(food_stuff_tp) // 2
if len(food_stuff_tp) % 2 == 0:
    middle_items = food_stuff_tp[mid-1:mid+1]
else:
    middle_items = (food_stuff_tp[mid],)

# 5. Extraer los primeros 3 y los últimos 3 de la lista
first_three = food_stuff_lt[:3]
last_three = food_stuff_lt[-3:]

# 6. Eliminar completamente food_stuff_tp
del food_stuff_tp

# 7. Comprobar si un ítem existe en un tuple
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
estonia_present = 'Estonia' in nordic_countries  # False
iceland_present = 'Iceland' in nordic_countries  # True



