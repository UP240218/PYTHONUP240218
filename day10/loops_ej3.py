# 1. Mostrar países que contienen "land"
paises = ['Finland', 'Sweden', 'Iceland', 'Norway', 'Denmark', 'Netherlands', 'Thailand', 'Poland', 'Switzerland']
con_land = []

for pais in paises:
    if 'land' in pais:
        con_land.append(pais)

print('Países que contienen "land":')
print(con_land)

# 2. Invertir lista de frutas usando loop
frutas = ['banana', 'orange', 'mango', 'lemon']
frutas_invertidas = []

for i in range(len(frutas) - 1, -1, -1):
    frutas_invertidas.append(frutas[i])

print('Frutas en orden inverso:')
print(frutas_invertidas)

# 3. Contar idiomas únicos en la lista de datos de países (simulación)
datos_paises = [
    {'name': 'China', 'population': 1403500365, 'languages': ['Chinese']},
    {'name': 'India', 'population': 1324171354, 'languages': ['Hindi', 'English']},
    {'name': 'USA', 'population': 331002651, 'languages': ['English']},
    {'name': 'Indonesia', 'population': 273523615, 'languages': ['Indonesian']},
    {'name': 'Pakistan', 'population': 220892340, 'languages': ['Urdu', 'English']},
    {'name': 'Brazil', 'population': 212559417, 'languages': ['Portuguese']},
    {'name': 'Nigeria', 'population': 206139589, 'languages': ['English']},
    {'name': 'Bangladesh', 'population': 164689383, 'languages': ['Bengali']},
    {'name': 'Russia', 'population': 145934462, 'languages': ['Russian']},
    {'name': 'Mexico', 'population': 128932753, 'languages': ['Spanish']},
    {'name': 'Germany', 'population': 83783942, 'languages': ['German']},
]

idiomas = []

for pais in datos_paises:
    for idioma in pais['languages']:
        if idioma not in idiomas:
            idiomas.append(idioma)

print('Cantidad de idiomas únicos:', len(idiomas))

# 4. Mostrar los 10 idiomas más hablados
conteo_idiomas = {}

for pais in datos_paises:
    for idioma in pais['languages']:
        if idioma in conteo_idiomas:
            conteo_idiomas[idioma] += 1
        else:
            conteo_idiomas[idioma] = 1

# Ordenamos por los más hablados
idiomas_mas_hablados = sorted(conteo_idiomas.items(), key=lambda x: x[1], reverse=True)[:10]

print('Los 10 idiomas más hablados:')
for idioma, cantidad in idiomas_mas_hablados:
    print(f'{idioma}: {cantidad} países')

# 5. Mostrar los 10 países más poblados
paises_ordenados = sorted(datos_paises, key=lambda x: x['population'], reverse=True)
top_10 = paises_ordenados[:10]

print('Los 10 países más poblados:')
for p in top_10:
    print(f"{p['name']}: {p['population']}")
