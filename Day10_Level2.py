#ejercicio 1
suma=0
for numero in range(101):
    suma+=numero
    print(suma)

#ejercicio 2
suma_pares=0
suma_inpares=0
for numero in range(101):
    if numero % 2==0:
        suma_pares += numero
    else:
        suma_inpares+=numero
print(f'Suma de numeros pares: {suma_pares}')
print(f'numero de numeros impares: {suma_inpares}')