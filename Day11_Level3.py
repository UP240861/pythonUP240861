import re
import math
from typing import List, Any, Union, Dict
from collections import Counter

# 1
def es_primo(numero: int) -> bool:
    """
    Verifica si un número es primo.
    Args:
    numero: Entero a verificar 
    Returns:
    True si el número es primo, False en caso contrario
    """
    if numero <= 1:
        return False
    if numero == 2:
        return True
    if numero % 2 == 0:
        return False
    
    for i in range(3, int(math.sqrt(numero)) + 1, 2):
        if numero % i == 0:
            return False
    return True

# 2
def todos_unicos(elementos: List[Any]) -> bool:
    """
    Verifica si todos los elementos en una lista son únicos.
    Args:
    elementos: Lista de elementos a verificar
    Returns:
    True si todos los elementos son únicos, False en caso contrario
    """
    return len(elementos) == len(set(elementos))

# 3
def mismo_tipo(elementos: List[Any]) -> bool:
    """
    Verifica si todos los elementos en una lista son del mismo tipo.
    
    Args:
        elementos: Lista de elementos a verificar
        
    Returns:
        True si todos los elementos son del mismo tipo, False en caso contrario
    """
    if not elementos:
        return True
    primer_tipo = type(elementos[0])
    return all(isinstance(elemento, primer_tipo) for elemento in elementos[1:])

# 4
def es_variable_valida(nombre: str) -> bool:
    """
    Verifica si una cadena es un nombre de variable válido en Python.
    
    Args:
        nombre: Cadena a verificar
        
    Returns:
        True si la cadena es un nombre de variable válido, False en caso contrario
    """
    return bool(re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', nombre))

# 5
def lenguajes_mas_hablados(datos_paises: List[Dict], cantidad: int = 10) -> List[Dict]:
    """
    Obtiene los lenguajes más hablados en el mundo.
    
    Args:
        datos_paises: Lista de diccionarios con datos de países
        cantidad: Número de lenguajes principales a devolver (10 o 20)
        
    Returns:
        Lista de diccionarios con lenguaje y conteo, ordenados descendentemente
    """
    conteo_lenguajes = {}
    
    for pais in datos_paises:
        for lenguaje in pais['languages']:
            conteo_lenguajes[lenguaje] = conteo_lenguajes.get(lenguaje, 0) + 1
    
    lenguajes_ordenados = sorted(conteo_lenguajes.items(), key=lambda x: x[1], reverse=True)
    return [{'lenguaje': lang, 'conteo': count} for lang, count in lenguajes_ordenados[:cantidad]]

def paises_mas_poblados(datos_paises: List[Dict], cantidad: int = 10) -> List[Dict]:
    """
    Obtiene los países más poblados del mundo.
    
    Args:
        datos_paises: Lista de diccionarios con datos de países
        cantidad: Número de países principales a devolver (10 o 20)
        
    Returns:
        Lista de diccionarios con país y población, ordenados descendentemente
    """
    paises_ordenados = sorted(datos_paises, key=lambda x: x['population'], reverse=True)
    return [{'pais': pais['name'], 'poblacion': pais['population']} 
            for pais in paises_ordenados[:cantidad]]