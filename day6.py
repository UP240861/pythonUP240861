# 1. Crea una tupla vacía
tupla_vacia = ()

# 2. Crea una tupla con los nombres de tus hermanos y hermanas
hermanos = ("Ramiro", "Alejandro")
hermanas = ("Sofia", "Jaqueline") 

# 3. Une las tuplas y asígnalas a "hermanos"
hermanos = hermanos + hermanas

# 4. ¿Cuántos hermanos tienes?
print("Total de hermanos:", len(hermanos))

# 5. Añade a tus padres y crea "miembros de la familia"
padres = ("Mamá", "Papá")
miembros_familia = hermanos + padres
print("Miembros de la familia:", miembros_familia)


#ejercicio nivel 2 

# escomprime "hermanos" y "padres" de "miembros de la familia" 
hermanos = miembros_familia[:-2]
padres = miembros_familia[-2:]

# 2. Crea tuplas y únelas
frutas = ("manzana", "plátano")
verduras = ("zanahoria", "espinaca")
productos_animales = ("leche", "huevo")
comida_cosa_tp = frutas + verduras + productos_animales

# 3. Convierte en lista
comida_cosa_lt = list(comida_cosa_tp)

# 4. Separar elementos del medio
medio = comida_cosa_tp[len(comida_cosa_tp)//2]
tres_primeros = comida_cosa_lt[:3]
tres_ultimos = comida_cosa_lt[-3:]

# 5. Eliminar tupla
del comida_cosa_tp

# 6. Comprobar si un elemento existe en la tupla/lista
print("manzana" in comida_cosa_lt)

# 7. Comprobar si "Estonia" es un país nórdico
paises_nordicos = ("Islandia", "Noruega", "Suecia", "Finlandia", "Dinamarca")
print("Estonia" in paises_nordicos)
print("Islandia" in paises_nordicos)




