# Lista vacía
lista_vacia = []

# Lista con más de 5 elementos
lista = [1, 2, 3, 4, 5, 6]

# Longitud de la lista
print(len(lista))

# Primer, medio y último elemento
print(lista[0])
print(lista[len(lista)//2])
print(lista[-1])

# Lista con datos mixtos
datos = ['Ana', 25, 1.68, 'Soltera', 'Calle 12']

# Lista de empresas IT
empresas = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

print(empresas)
print(len(empresas))
print(empresas[0], empresas[len(empresas)//2], empresas[-1])

empresas[0] = 'Meta'
print(empresas)

empresas.append('Tesla')
print(empresas)

empresas.insert(len(empresas)//2, 'Netflix')
print(empresas)

for i in range(len(empresas)):
    if empresas[i] != 'IBM':
        empresas[i] = empresas[i].upper()

print(empresas)

print('#; '.join(empresas))

print('GOOGLE' in empresas)

empresas.sort()
print(empresas)

empresas.reverse()
print(empresas)

print(empresas[:3])
print(empresas[-3:])

n = len(empresas)
if n % 2 == 1:
    print(empresas[n//2])
else:
    print(empresas[n//2 - 1:n//2 + 1])

del empresas[0]
print(empresas)

n = len(empresas)
if n % 2 == 1:
    del empresas[n//2]
else:
    del empresas[n//2 - 1:n//2 + 1]

print(empresas)

del empresas[-1]
print(empresas)

empresas.clear()
print(empresas)

# del empresas  # comento para que no dé error si quieres usar después

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']

full_stack = front_end + back_end
print(full_stack)

full_stack.insert(full_stack.index('Redux') + 1, 'Python')
full_stack.insert(full_stack.index('Python') + 1, 'SQL')
print(full_stack)
