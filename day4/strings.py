# 1. Concatenar 'Thirty', 'Days', 'Of', 'Python'
exercise_1 = 'Thirty' + ' ' + 'Days' + ' ' + 'Of' + ' ' + 'Python'

# 2. Concatenar 'Coding', 'For', 'All'
exercise_2 = 'Coding' + ' ' + 'For' + ' ' + 'All'

# 3. Declarar variable company
company = 'Coding For All'

# 4. Imprimir company
print(company)

# 5. Longitud de company
print(len(company))

# 6. Mayúsculas
print(company.upper())

# 7. Minúsculas
print(company.lower())

# 8. capitalize, title, swapcase
print(company.capitalize())
print(company.title())
print(company.swapcase())

# 9. Cortar la primera palabra
print(company[7:])

# 10. Verificar si contiene "Coding"
print(company.index('Coding'))
print(company.find('Coding'))
print('Coding' in company)

# 11. Reemplazar "Coding" por "Python"
print(company.replace('Coding', 'Python'))

# 12. Reemplazar en 'Python for Everyone'
print('Python for Everyone'.replace('Everyone', 'All'))

# 13. Split usando espacio
print(company.split())

# 14. Split por coma
print("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(', '))

# 15. Carácter en índice 0
print(company[0])

# 16. Último índice
print(company[-1])

# 17. Carácter en índice 10
print(company[10])

# 18. Acrónimo de 'Python For Everyone'
print(''.join([w[0] for w in 'Python For Everyone'.split()]))

# 19. Acrónimo de 'Coding For All'
print(''.join([w[0] for w in company.split()]))

# 20. Índice de la primera 'C'
print(company.index('C'))

# 21. Índice de la primera 'F'
print(company.index('F'))

# 22. Última ocurrencia de 'l'
print('Coding For All People'.rfind('l'))

# 23. Primera posición de 'because'
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.find('because'))

# 24. Última posición de 'because'
print(sentence.rindex('because'))

# 25. Slice de 'because because because'
print(sentence[sentence.find('because'):sentence.rindex('because') + len('because')])

# 26. Repetido del 23
print(sentence.find('because'))

# 27. Repetido del 25
print(sentence[sentence.find('because'):sentence.rindex('because') + len('because')])

# 28. ¿Empieza con 'Coding'?
print(company.startswith('Coding'))

# 29. ¿Termina con 'coding'?
print(company.endswith('coding'))

# 30. Quitar espacios laterales
print('   Coding For All      '.strip())

# 31. ¿Es identificador válido?
print('30DaysOfPython'.isidentifier())
print('thirty_days_of_python'.isidentifier())

# 32. Unir librerías con '# '
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('# '.join(libraries))

# 33. Separar con salto de línea
print('I am enjoying this challenge.\nI just wonder what is next.')

# 34. Separar con tabulación
print('Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki')

# 35. Área de un círculo con formato
radius = 10
area = 3.14 * radius ** 2
print('The area of a circle with radius {} is {} meters square.'.format(radius, int(area)))

# 36. Operaciones con formato
a, b = 8, 6
print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b))
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))
