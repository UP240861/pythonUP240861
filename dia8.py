## 💻 Exercises: Day 8

## 1. Create an empty dictionary called dog
print('\nEjercicio 1')
dog = {}
print(dog)

## 2. Add name, color, breed, legs, age to the dog dictionary
print('\nEjercicio 2')
dog.update({
    'name': 'Jake',
    'color': 'Yellow',
    'breed': 'Bulldog England',
    'legs': 4,  # Números como enteros, no strings
    'age': 3    # Edad típica en años (34 sería demasiado para un perro)
})
print(dog)

## 3. Create student dictionary
print('\nEjercicio 3')
student = {
    'first_name': 'Leonardo',
    'last_name': 'Zamora',
    'gender': 'male',
    'age': 19,  # Entero en lugar de string
    'marital_status': 'Single',
    'skills': [
        'Beginner in cybersecurity', 
        'Beginner in Python', 
        'Support and maintenance technician', 
        'B1 English'
    ],
    'country': 'Mexico',  # Añadido que faltaba en el enunciado
    'city': 'Aguascalientes',
    'address': {
        'street': 'Estrella 456',
        'neighborhood': 'Mision de Santa Fe'
    }
}
print(student)

## 4. Get length of student dictionary
print('\nEjercicio 4')
print("Longitud:", len(student))

## 5. Get skills value and check data type
print('\nEjercicio 5')
skills = student['skills']
print("Habilidades:", skills)
print("Tipo de dato:", type(skills))

## 6. Modify skills by adding new ones
print('\nEjercicio 6')
student['skills'].extend(['Autodidact', 'Smart'])
print("Habilidades actualizadas:", student['skills'])

## 7. Get dictionary keys as list
print('\nEjercicio 7')
keys_list = list(student.keys())
print("Llaves:", keys_list)

## 8. Get dictionary values as list
print('\nEjercicio 8')
values_list = list(student.values())
print("Valores:", values_list)

## 9. Change dictionary to list of tuples
print('\nEjercicio 9')
items_list = list(student.items())
print("Items como tuplas:", items_list)

## 10. Delete one item
print('\nEjercicio 10')
removed_item = student.pop('marital_status')
print(f"Se eliminó '{removed_item}'")
print("Diccionario actualizado:", student)

## 11. Delete one dictionary
print('\nEjercicio 11')
del dog
try:
    print(dog)  # Esto fallará intencionalmente
except NameError:
    print("El diccionario 'dog' ha sido eliminado correctamente")

print("\nTodos los ejercicios completados correctamente!")
