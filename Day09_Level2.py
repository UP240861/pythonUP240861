#ejercicio 1
def calificar_estudiante(puntuacion):
    if 80 <= puntuacion <= 100:
        return "A"
    elif 70 <= puntuacion <= 79:
        return "B"
    elif 60 <= puntuacion <= 69:
        return "C"
    elif 50 <= puntuacion <= 59:
        return "D"
    elif 0 <= puntuacion <= 49:
        return "F"
    else:
        return "Puntuación inválida"
    
#ejerecicio 2
def determinar_temporada(mes):
    mes = mes.lower()  # Convertir a minúsculas para evitar problemas con mayúsculas
    if mes in ['septiembre', 'octubre', 'noviembre']:
        return "La temporada es otoño."
    elif mes in ['diciembre', 'enero', 'febrero']:
        return "La temporada es invierno."
    elif mes in ['marzo', 'abril', 'mayo']:
        return "La temporada es primavera."
    elif mes in ['junio', 'julio', 'agosto']:
        return "La temporada es verano."
    else:
        return "El mes ingresado no es válido."

#ejercicio 3
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit_to_check = 'apple'
if fruit_to_check in fruits:
    print('That fruit already exists in the list')
else:
    fruits.append(fruit_to_check)
    print('Fruit added to the list:', fruits)