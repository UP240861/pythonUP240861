#1
edades = [22, 19, 24, 25, 26, 24, 25, 24]
edades_unicas = set(edades)
print("Lista de edades:", edades)
print("Conjunto de edades únicas:", edades_unicas)
len_lista = len(edades)
len_conjunto = len(edades_unicas)
print("Longitud de la lista:", len_lista)
print("Longitud del conjunto:", len_conjunto)
comparaciones = {
    (True, False): "La lista es mayor porque contiene duplicados.",
    (False, False): "Ambos tienen la misma longitud.",
    (False, True): "El conjunto es mayor (lo cual es raro)."
}
resultado = comparaciones.get(
    (len_lista > len_conjunto, len_conjunto > len_lista)
)
print(resultado)
#2
oracion = "Soy profesor y me encanta inspirar y enseñar."
#3
oracion_limpia = oracion.replace(".", "").lower()
#4
palabras = oracion_limpia.split()
##Una string o cadena solo puede contener una palabra y que esta no se puede cambiar 
##Una lista ya puede contener mas cadenas por asi decirlo y a su vez a esta se le puede quitar y agregar
##contenido y En tuple no podemos modificarla y esta como las 2
##y los set pueden estar ordenados como desordenados y se pueden acoplar a otros sin necesidad de que se
##repitan strings
#5
palabras_unicas = set(palabras)
print("Palabras únicas:", palabras_unicas)
print("Número de palabras únicas:", len(palabras_unicas))