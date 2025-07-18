# Nivel 1 - Ejercicios con tuplas

# 1. Crear una tupla vacía
empty_tuple = ()
print("Tupla vacía:", empty_tuple)

# 2. Crear tuplas con nombres de hermanos y hermanas (imaginarios)
brothers = ('Juan', 'Pedro')
sisters = ('Ana', 'Luisa')

# 3. Unir hermanos y hermanas en una tupla llamada siblings
siblings = brothers + sisters
print("Siblings:", siblings)

# 4. Contar cuántos hermanos y hermanas tienes
print("Número de siblings:", len(siblings))

# 5. Modificar siblings para agregar padre y madre y guardar en family_members
# Como las tuplas son inmutables, creamos una nueva concatenando
parents = ('Carlos', 'María')
family_members = siblings + parents
print("Family members:", family_members)
