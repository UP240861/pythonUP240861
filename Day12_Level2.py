import random

def list_of_hexa_colors(num_colors=1):
    """
    Genera una lista de colores hexadecimales.
    
    Args:
        num_colors (int): Número de colores a generar (por defecto 1).
    
    Returns:
        list: Lista de colores hexadecimales en formato '#xxxxxx'.
    """
    colors = []
    hex_chars = '0123456789abcdef'
    
    for _ in range(num_colors):
        color = '#'
        for _ in range(6):
            color += random.choice(hex_chars)
        colors.append(color)
    
    return colors
#ejercicio 2

def list_of_rgb_colors(num_colors=1):
    """
    Genera una lista de colores RGB.
    
    Args:
        num_colors (int): Número de colores a generar (por defecto 1).
    
    Returns:
        list: Lista de colores RGB en formato 'rgb(x, y, z)'.
    """
    colors = []
    
    for _ in range(num_colors):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        colors.append(f'rgb({r}, {g}, {b})')
    
    return colors

#ejercicio 3
def generate_colors(color_type, num_colors):
    """
    Genera colores hexadecimales o RGB según se especifique.
    
    Args:
        color_type (str): Tipo de color a generar ('hexa' o 'rgb').
        num_colors (int): Número de colores a generar.
    
    Returns:
        list: Lista de colores en el formato especificado.
    
    Raises:
        ValueError: Si el tipo de color no es 'hexa' o 'rgb'.
    """
    if color_type.lower() == 'hexa':
        return list_of_hexa_colors(num_colors)
    elif color_type.lower() == 'rgb':
        return list_of_rgb_colors(num_colors)
    else:
        raise ValueError("El tipo de color debe ser 'hexa' o 'rgb'")