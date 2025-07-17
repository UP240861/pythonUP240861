# 1
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
filtrados = [num for num in numbers if num <= 0]
print("1. Números negativos y cero:", filtrados)

# 2
list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
aplanada = [num for sublist in list_of_lists for subsublist in sublist for num in subsublist]
print("\n2. Lista aplanada:", aplanada)

# 3
lista_tuplas = [(i, 1, i, i*2, i3, i4, i*5) for i in range(11)]
print("\n3. Lista de tuplas:")
for tupla in lista_tuplas:
    print(tupla)

# 4
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
paises_formateados = [
    [pais[0].upper(), pais[0][:3].upper(), pais[1].upper()] 
    for sublist in countries for pais in sublist
]
print("\n4. Países formateados:", paises_formateados)

# 5
paises_diccionarios = [
    {'country': pais[0].upper(), 'city': pais[1].upper()}
    for sublist in countries for pais in sublist
]
print("\n5. Lista de diccionarios:")
for dic in paises_diccionarios:
    print(dic)

# 6
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
nombres_concatenados = [' '.join(nombre) for sublist in names for nombre in sublist]
print("\n6. Nombres concatenados:", nombres_concatenados)

# 7
pendiente = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1) if x2 != x1 else None

# 8
interseccion_y = lambda m, x, y: y - m * x

print("\n7. Ejemplo de funciones lambda:")
print("Pendiente entre (1,2) y (3,4):", pendiente(1, 2, 3, 4))
print("Intersección con Y (m=1.0 en (1,2)):", interseccion_y(1.0, 1, 2))