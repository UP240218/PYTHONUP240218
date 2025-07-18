import random
import string

# 1. Generar un ID de usuario de 6 caracteres aleatorios
def random_user_id():
    chars = string.ascii_letters + string.digits
    user_id = ''
    for i in range(6):
        user_id += random.choice(chars)
    return user_id

print(random_user_id())

# 2. Generar varios IDs con longitud y cantidad que el usuario elige
def user_id_gen_by_user():
    chars = string.ascii_letters + string.digits
    length = int(input("Cuántos caracteres por ID?: "))
    count = int(input("Cuántos IDs generar?: "))
    
    for _ in range(count):
        user_id = ''
        for i in range(length):
            user_id += random.choice(chars)
        print(user_id)

user_id_gen_by_user()

# 3. Generar un color RGB aleatorio
def rgb_color_gen():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"rgb({r},{g},{b})"

print(rgb_color_gen())
