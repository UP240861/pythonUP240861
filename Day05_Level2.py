ages=[19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

#orden y edad minima y maxima
ages.sort()
print("Lista ordenada:", ages)
min_age = min(ages)
max_age = max(ages)
print("Edad mínima:", min_age)
print("Edad máxima:", max_age)

#edad minima y maxima
ages.append(min_age)
ages.append(max_age)
print("Lista con edades agregadas:", ages)

#edad media
ages.sort()  
n=len(ages)
if n%2==0:
    median=(ages[n//2-1]+ages[n//2])/2
else:
    median=ages[n//2]
print("Mediana:", median)

#media
average = sum(ages) / len(ages)
print("Promedio:", average)

#rango
range_age=max_age-min_age
print("Rango de edades:",range_age)

#comparacion
diff_min_avg = abs(min_age - average)
diff_max_avg = abs(max_age - average)
print("Diferencia min promedio:", diff_min_avg)
print("Diferencia max promedio:", diff_max_avg)

countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']

#pais medio
n = len(countries)
if n%2==1:
    middle_country=countries[n//2]
else:
    middle_country=countries[n//2-1:n//2+1]
print("País(es) del medio:", middle_country)

#partes iguales
half = (n + 1) // 2  # Si es impar, la primera mitad tiene 1 más
first_half = countries[:half]
second_half = countries[half:]
print("Primera mitad:", first_half)
print("Segunda mitad:", second_half)

country1, country2, country3, *scandic_countries = countries
print("Primer país:", country1)
print("Segundo país:", country2)
print("Tercer país:", country3)
print("Países escandinavos:", scandic_countries)