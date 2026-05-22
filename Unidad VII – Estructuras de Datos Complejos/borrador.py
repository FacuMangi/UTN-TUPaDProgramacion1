# miSet = set()
# print(miSet)

# array = [1, 2, 2, 3]

# for i in range(len(array)):
#     miSet.add(array[i])

# print(miSet)

elSet = set()

lista = ['a', 'b', 'a', 'c', 'b']

for i in range(len(lista)):
    elSet.add(lista[i])
print(elSet)

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print("Unión a | b:", a | b)            # union()
print("Intersección a & b:", a & b)     # intersection()
print("Diferencia a - b:", a - b)       # difference()
print("Dif. simétrica a ^ b:", a ^ b)   # symmetric_difference()

#Lista a Tupla y Tupla a Lista:
tupla = (1,2,3)
listaTupla = list(tupla)

lista = [1,2,3]
tuplaLista = tuple(lista)
#Estas conversiones no modifican el original, sino que crean una nueva estructura.

elementos_quimicos = {"Oxígeno":"O", "Nitrógeno":"N", "Sodio":"Na","Hierro":"Fe"}
print(elementos_quimicos.values())