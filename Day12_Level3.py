import random

def shuffle_list(lista):
    lista_copiada = lista.copy()
    random.shuffle(lista_copiada)
    return lista_copiada

def numeros_aleatorios_unicos():
    numeros = list(range(10))  # Crear lista del 0 al 9
    numeros_mezclados = shuffle_list(numeros)
    return numeros_mezclados[:7]  # Devolver los primeros 7 elementos

# Ejemplo de uso
print(numeros_aleatorios_unicos())