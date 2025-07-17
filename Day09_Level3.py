person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True, 
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# 1. Comprobar si tiene la clave 'skills' e imprimir la habilidad central
if 'skills' in person:
    skills = person['skills']
    middle_index = len(skills) // 2
    print(f"Habilidad central: {skills[middle_index]}")

# 2. Comprobar si tiene la habilidad 'Python'
if 'skills' in person:
    has_python = 'Python' in person['skills']
    print(f"¿Tiene habilidades en Python? {has_python}")

# 3. Determinar el tipo de desarrollador
if 'skills' in person:
    skills_set = set(person['skills'])
    
    if skills_set == {'JavaScript', 'React'}:
        print('Es desarrollador front-end')
    elif skills_set >= {'Node', 'Python', 'MongoDB'}:
        print('Es desarrollador back-end')
    elif skills_set >= {'React', 'Node', 'MongoDB'}:
        print('Es desarrollador fullstack')
    else:
        print('Título desconocido')

# 4. Verificar estado civil y país
if person.get('is_married') and person.get('country') == 'Finland':
    print(f"{person['first_name']} {person['last_name']} reside en {person['country']}. Está casado.")