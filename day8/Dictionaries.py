#ejercicio 1
dog = {}
dog['name'] = 'Wasauski'
dog['color'] = 'gold'
dog['breed'] = 'Labrador'
dog['legs'] = 4
dog['age'] = 7

print(dog)

#ejercicio 2
student = {
    'first_name': 'María',
    'last_name': 'Sandoval',
    'gender': 'F',
    'age': 18,
    'marital_status': 'soltera',
    'skills': ['Python', 'Excel'],
    'country': 'México',
    'city': 'Aguascalientes',
    'address': {
        'street': 'San gerardo',
        'zipcode': '20342'
    }
}

#ejercicio 3
print(len(student))

#ejercicio 4
skills = student.get('skills')
print(skills, type(skills))

#ejercicio 5
student['skills'].append('JavaScript')
student['skills'].extend(['Git', 'SQL'])
print(student['skills'])

#ejercicio 6
keys = list(student.keys())
print(keys)

#ejercicio 7
values = list(student.values())
print(values)

#ejercicio 8
items = list(student.items())
print(items)

#ejerecicio 9 
student.pop('marital_status')
# o: del student['city']
print(student)

#ejercicio 10
del student
# Intentar imprimirlo ahora generará NameError porque ya no existe.



