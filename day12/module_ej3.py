import random

# 1. Función shuffle_list que toma una lista y devuelve la lista mezclada
def shuffle_list(lst):
    lst_copy = lst[:]  # hacer copia para no modificar original
    random.shuffle(lst_copy)
    return lst_copy

print(shuffle_list([1, 2, 3, 4, 5]))

# 2. Función que devuelve una lista con 7 números únicos aleatorios entre 0 y 9
def unique_random_numbers():
    numbers = set()
    while len(numbers) < 7:
        numbers.add(random.randint(0, 9))
    return list(numbers)

print(unique_random_numbers())
