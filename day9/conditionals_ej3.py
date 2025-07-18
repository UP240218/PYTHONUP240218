person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# 1. Verificar si tiene la key 'skills' y mostrar la habilidad del medio
if 'skills' in person:
    skills = person['skills']
    middle_index = len(skills) // 2
    print("Habilidad del medio:", skills[middle_index])

# 2. Revisar si 'Python' está en sus habilidades
if 'skills' in person:
    if 'Python' in person['skills']:
        print("Tiene Python en sus habilidades")
    else:
        print("No tiene Python en sus habilidades")

# 3. Clasificar tipo de desarrollador según habilidades
if 'skills' in person:
    skills = person['skills']
    if set(skills) == set(['JavaScript', 'React']):
        print("Es un desarrollador front end")
    elif 'Node' in skills and 'Python' in skills and 'MongoDB' in skills:
        print("Es un desarrollador backend")
    elif 'React' in skills and 'Node' in skills and 'MongoDB' in skills:
        print("Es un desarrollador fullstack")
    else:
        print("Título desconocido")

# 4. Mensaje si está casado y vive en Finlandia
if person.get('is_marred') and person.get('country') == 'Finland':
    print(f"{person['first_name']} {person['last_name']} vive en Finlandia. Está casado.")
