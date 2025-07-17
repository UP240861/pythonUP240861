#ejercicio 1
numbers =[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in numbers:
    print(number)
i=0
while i<=10:
    print(i)
    i+=1

#ejercicio 2
numb=[10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
for num in numb:
    print(num)

while i>=0:
    print(i)
    i-=1

#ejercicio 4
for i in range(1, 8):
    print('#' * i)

for i in range(8):
    for j in range(8):
     print('#', end=' ')
    print( )

#ejercicio 5 
for i in range(11):
    print(f'{i} x {i}={i*i}')

#ejercicio 6
tecnologias=['Python', 'Numpy','Pandas','Django', 'Flask']
for tecnologia in tecnologias:
    print(tecnologia)

#ejercicio 7
lst=list(range(0,100,2))
print(lst)
lista=list(range(1,99,2))
print(lista)