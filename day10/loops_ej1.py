# 1. Itera del 0 al 10 usando for
for i in range(11):
    print(i)

# 1. Itera del 0 al 10 usando while
i = 0
while i <= 10:
    print(i)
    i += 1

# 2. Itera del 10 al 0 usando for
for i in range(10, -1, -1):
    print(i)

# 2. Itera del 10 al 0 usando while
i = 10
while i >= 0:
    print(i)
    i -= 1

# 3. Triángulo de #
for i in range(1, 8):
    print('#' * i)

# 4. Cuadro 8x8 de #
for i in range(8):
    for j in range(8):
        print('#', end=' ')
    print()

# 5. Tabla de cuadrados
for i in range(11):
    print(f"{i} x {i} = {i * i}")

# 6. Iterar lista de tecnologías
tech = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for item in tech:
    print(item)

# 7. Números pares del 0 al 100
for i in range(101):
    if i % 2 == 0:
        print(i)

# 8. Números impares del 0 al 100
for i in range(101):
    if i % 2 != 0:
        print(i)
