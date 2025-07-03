A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
#1
A.update(B)
print("#1 A actualizado con B:", A)
#2
print("#2 Intersección de B y A:", B.intersection(A))
#3
print("#3 ¿Un set puede ser un set o subset o superset?")
print("¿A es subconjunto de B?:", A.issubset(B))
#4
print("#4 ¿A y B son disjuntos?:", A.isdisjoint(B))
#5
A.update(B)
B.update(A)
#6
print("#6 Diferencia A - B:", A.difference(B))
print("   Diferencia B - A:", B.difference(A))
#7
del A
del B
edades = [22, 19, 24, 25, 26, 24, 25, 24]