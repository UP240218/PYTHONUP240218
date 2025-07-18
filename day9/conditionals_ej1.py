# Ejercicio 1: Edad para conducir
age = int(input("Enter your age: "))
if age >= 18:
    print("You are old enough to learn to drive.")
else:
    years_left = 18 - age
    print(f"You need {years_left} more year{'s' if years_left > 1 else ''} to learn to drive.")

# Ejercicio 2: Comparar edades
my_age = 30  # Puedes cambiarlo por tu edad
your_age = int(input("Enter your age: "))
diff = abs(my_age - your_age)

if your_age > my_age:
    print(f"You are {diff} year{'s' if diff > 1 else ''} older than me.")
elif my_age > your_age:
    print(f"I am {diff} year{'s' if diff > 1 else ''} older than you.")
else:
    print("We are the same age.")

# Ejercicio 3: Comparar dos números
a = int(input("Enter number one: "))
b = int(input("Enter number two: "))

if a > b:
    print(f"{a} is greater than {b}")
elif a < b:
    print(f"{a} is smaller than {b}")
else:
    print(f"{a} is equal to {b}")
