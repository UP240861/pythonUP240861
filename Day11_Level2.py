#ejercicio 1
def evens_and_odds(n):
    """
    Cuenta el número de pares e impares desde 0 hasta n (inclusive).
    """
    if n < 0:
        return "El número debe ser positivo."
    
    pares = (n + 1) // 2 if n % 2 != 0 else n // 2 + 1
    impares = (n + 1) - pares
    
    return f"El número de impares es {impares}.\nEl número de pares es {pares}."

#ejercicio 2
def factorial(num):
    """
    Calcula el factorial de un número entero no negativo.
    """
    if num < 0:
        return "El factorial no está definido para números negativos."
    elif num == 0:
        return 1
    else:
        result = 1
        for i in range(1, num + 1):
            result *= i
        return result
#ejercicio 3
#media
def mean(numbers):
    """Calcula la media de una lista de números"""
    if not numbers:
        raise ValueError("La lista no puede estar vacía")
    return sum(numbers) / len(numbers)
#medina
def median(numbers):
    """Calcula la mediana de una lista de números"""
    if not numbers:
        raise ValueError("La lista no puede estar vacía")
    
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2
    
    if n % 2 == 1:
        return sorted_numbers[mid]
    else:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
#moda
def mode(numbers):
    """Calcula la moda de una lista de números"""
    if not numbers:
        raise ValueError("La lista no puede estar vacía")
    
    frequency = {}
    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1
    
    max_freq = max(frequency.values())
    modes = [num for num, freq in frequency.items() if freq == max_freq]
    
    return modes[0] if len(modes) == 1 else modes
#rango
def data_range(numbers):
    """Calcula el rango de una lista de números"""
    if not numbers:
        raise ValueError("La lista no puede estar vacía")
    return max(numbers) - min(numbers)
#varianza
def variance(numbers):
    """Calcula la varianza de una lista de números"""
    if not numbers:
        raise ValueError("La lista no puede estar vacía")
    
    m = mean(numbers)
    squared_diffs = [(x - m) ** 2 for x in numbers]
    return sum(squared_diffs) / len(numbers)
# desviacion estandar
def stdev(numbers):
    """Calcula la desviación estándar de una lista de números"""
    if not numbers:
        raise ValueError("La lista no puede estar vacía")
    return variance(numbers) ** 0.5