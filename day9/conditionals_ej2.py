# Ejercicio 1: Calificación según nota
def grade(score):
    if score >= 80:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 60:
        return "C"
    elif score >= 50:
        return "D"
    else:
        return "F"

nota = int(input("Ingresa la nota: "))
print("Calificación:", grade(nota))

print("\n-------------------\n")

# Ejercicio 2: Estación según mes
def season(month):
    month = month.lower()
    if month in ['september', 'october', 'november']:
        return "Autumn"
    elif month in ['december', 'january', 'february']:
        return "Winter"
    elif month in ['march', 'april', 'may']:
        return "Spring"
    elif month in ['june', 'july', 'august']:
        return "Summer"
    else:
        return "No sé que estación es esa."

mes = input("Ingresa el mes: ")
print("Estación:", season(mes))

print("\n-------------------\n")

# Ejercicio 3: Lista de frutas
frutas = ['banana', 'orange', 'mango', 'lemon']

nueva_fruta = input("Ingresa una fruta: ").lower()

if nueva_fruta in frutas:
    print("Esa fruta ya está en la lista")
else:
    frutas.append(nueva_fruta)
    print("Lista actualizada:", frutas)
