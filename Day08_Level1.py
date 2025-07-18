
#1.
print('\nEjercicio 1')
dog = {}
print(dog)

#2.
print('\nEjercicio 2')
dog.update({
    'name': 'Jake',
    'color': 'Yellow',
    'breed': 'Bulldog England',
    'legs': 4,
    'age': 3
})
print(dog)

#3.
print('\nEjercicio 3')
student = {
    'first_name': 'Leonardo',
    'last_name': 'Zamora',
    'gender': 'male',
    'age': 19,
    'marital_status': 'Single',
    'skills': [
        'Beginner in cybersecurity', 
        'Beginner in Python', 
        'Support and maintenance technician', 
        'B1 English'
    ],
    'country': 'Mexico', 
    'city': 'Aguascalientes',
    'address': {
        'street': 'Estrella 456',
        'neighborhood': 'Mision de Santa Fe'
    }
}
print(student)

#4.
print('\nEjercicio 4')
print("Longitud:", len(student))

#5.
print('\nEjercicio 5')
skills = student['skills']
print("Habilidades:", skills)
print("Tipo de dato:", type(skills))

#6.
print('\nEjercicio 6')
student['skills'].extend(['Autodidact', 'Smart'])
print("Habilidades actualizadas:", student['skills'])

#7.
print('\nEjercicio 7')
keys_list = list(student.keys())
print("Llaves:", keys_list)

#8.
print('\nEjercicio 8')
values_list = list(student.values())
print("Valores:", values_list)

#9.
print('\nEjercicio 9')
items_list = list(student.items())
print("Items como tuplas:", items_list)

#10.
print('\nEjercicio 10')
removed_item = student.pop('marital_status')
print(f"Se eliminó '{removed_item}'")
print("Diccionario actualizado:", student)

#11.
print('\nEjercicio 11')
del dog
try:
    print(dog) 
except NameError:
    print("El diccionario 'dog' ha sido eliminado correctamente")

print("\nTodos los ejercicios completados correctamente!")
