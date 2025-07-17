1
cadena_concatenada = "Treinta" + " " + "Días" + " " + "De" + " " + "Python"
print(cadena_concatenada)
#2
cadena_concatenada2 = "Codificación" + " " "Para" + " " + "Todos"
print(cadena_concatenada2)
#3
empresa= "Codificación Para Todos"
#4
print(empresa)
#5
print("longitud de la empresa:", len(empresa))
#6
print(empresa.upper())
#7
print(empresa.lower())
#8
print("capitalize()", empresa.capitalize())
print("title()", empresa.title())
print("swapcase():", empresa.swapcase())
#9
primera_palabra =empresa.split()[0]
print(primera_palabra)
#10
palabra="Codificación"
if  palabra in empresa:
    print(f'"{palabra}" esta en la cadena.')
else:
    print(f'"{palabra}"no esta en la cadena.')   
#11
cadena_modificada =cadena_concatenada2.replace("Codificación", "Python")
print(cadena_modificada)
#12
cadena_modificada2= cadena_modificada.replace("Todos", "Siempre")
print(cadena_modificada2)
#13
resultado = cadena_concatenada2.split(" ")
print(resultado)
#14
redes= "Facebook Google Microsoft Apple IBM Oracle Amazon"
totales = redes.split()
print(totales)
#15
caracter=empresa[0]
print(caracter)
#16
ultimo_indice=len(empresa)-1
print("el ultimo indice es:" ,ultimo_indice)
#17
carac = empresa[10]
print(carac)
#18
palabras=cadena_modificada2.split()
acronimo= "".join([palabra[0] for palabra in palabras])
print(acronimo)
#19
palabras=empresa.split()
acronimo= "".join([palabra[0] for palabra in palabras])
print(acronimo)
#20
posicion = empresa.find("C")
print(posicion)
#21
posicion = empresa.find("f")
print(posicion)
#22
variable= "Codigo para toda la gente"
posicion1=variable.rfind("l")
print(posicion1)
#23
frase="No se puede terminar una oración con 'because' porque es una conjunción"
posicion2= frase.find('because')
print(posicion2)
#24
posicion2= frase.rindex('because')
print(posicion2)
#25
frase_modificada=frase.replace("'because' porque es una conjunción" , " ")
print(frase_modificada)
#26
falla='No puedes terminar una oración con porque porque porque es una conjunción'
encontrada=falla.find('porque')
print(encontrada)
#27
frase_falla=falla.replace(' porque porque porque', " ")
print(frase_falla)
#28
resultado = empresa.startswith("Codificación")
print(resultado)  
#29
resultado = empresa.endswith("Codificación")
print(resultado) 
#30
frase3=" Codificación Para Todos "  
frase3_limpia=frase3.strip()
print(frase3_limpia)
#31
print("30DaysOfPython".isidentifier())        
print("thirteen_days_of_python".isidentifier())       
#32
bibliotecas=['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
resultado4=' # '.join(bibliotecas)
print(resultado4)
#33
print("I am enjoying this challenge.\nI just wonder what is next.")
#34
print("Nombre\t\tEdad\tPais\t\tCiudad")
print("JP\t         19\tMexico\t    \tAgs")
#35
radio = 10
area = 3.14 * radio ** 2
mensaje = "El area de un circulo con radio de {} es {} metros cuadrados.".format(radio, int(area))
print(mensaje)
#36
a = 8
b = 6

print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b:.2f}")
print(f"{a} % {b} = {a % b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} ** {b} = {a ** b}")