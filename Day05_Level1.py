#1.
lista_vacia=[]

#2.
frutas=['pitaya','ciruelas',"uvas","naranjas"]

#3.
print(len(frutas))

#4.

print(frutas[0])                
print(frutas[len(frutas)//2])   
print(frutas[-1])               

#5.
mixed_data_types=['José Pablo Morales Esparza', 19, 1.83, 'Soltero', 'Valladolid']

#6.
compañias=['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

#7.
print(compañias)

#8.
print(len(compañias))

#9.
print(compañias[0])                
print(compañias[len(compañias)//2]) 
print(compañias[-1])  

#10.
compañias[1]='Alfabeto'

#11.
compañias.append('Twitter')
print(compañias)

#12.
medio=len(compañias)//2
compañias.insert(medio,'intel')
print(compañias)

#13.
compañias[0]=compañias[0].upper()
print(compañias)

#14.
print('#;'.join(compañias))

#15
print('google' in compañias)

#16.
compañias.sort()
print(compañias)

#17
compañias.reverse()
print(compañias)

#18
print(compañias[:3])

#19
print(compañias[:-3])

#20
long = len(compañias)
if long % 2 == 1:
    print([compañias[long//2]])
else:
    print(compañias[long//2-1:long//2+1])

#21
compañias.pop(0)
print(compañias)

#22.
medio = len(compañias)//2
if len(compañias)%2==1:
    compañias.pop(medio)
else:
    compañias.pop(medio)
    compañias.pop(medio-1)
print(compañias)

#23
compañias.pop()
print(compañias)

#24
compañias.clear()
print(compañias)

#25
del compañias

#26.
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
lleno = front_end + back_end
print(lleno)

#27
index_redux = lleno.index('Redux')
lleno.insert(index_redux + 1, 'Python')
lleno.insert(index_redux + 2, 'SQL')
print(lleno)