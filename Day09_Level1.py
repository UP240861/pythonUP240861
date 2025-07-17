#ejercicio 1
edad=int(input('ingrese su edad :'))
if edad >=18:
    print('tiene la edad justa para conducir')
else:
    años_faltantes=18-edad
    print(f"Aún no tiene la edad suficiente para conducir. Espere {años_faltantes} años.")

#ejercicio 2
my_age = 18
your_age = int(input('Ingresa tu edad: '))

if my_age > your_age:
    diferencia = my_age - your_age
    if diferencia == 1:
        print(f'Yo soy mayor que tú por {diferencia} año')
    else:
        print(f'Yo soy mayor que tú por {diferencia} años')
elif my_age < your_age:
    diferencia = your_age - my_age
    if diferencia == 1:
        print(f'Tú eres mayor que yo por {diferencia} año.')
    else:
        print(f'Tú eres mayor que yo por {diferencia} años.')
else:
    print("¡Tenemos la misma edad!")

#ejercicio 3
a = int(input("Ingrese el número uno: "))
b = int(input("Ingrese el número dos: "))

# Comparar los números y mostrar el resultado
if a > b:
    print(f"{a} es mayor que {b}")
elif a < b:
    print(f"{a} es menor que {b}")
else:
    print(f"{a} es igual a {b}")