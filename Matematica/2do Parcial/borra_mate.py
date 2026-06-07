a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print("Unión a | b:", a | b)            # union()
print("Intersección a & b:", a & b)     # intersection()
print("Diferencia a - b:", a - b)       # difference()
print("Dif. simétrica a ^ b:", a ^ b)   # symmetric_difference()

a = {1, 2, 3}
b = {1, 2, 3, 4}

print("a ⊆ b ?", a.issubset(b))     # True
print("b ⊇ a ?", b.issuperset(a))   # True

# Atajos con operadores:
print("a <= b ?", a <= b)            # subset (incluyente)
print("b >= a ?", b >= a)            # superset (incluyente)

C = {1, 2, 3, 4}
D = {"a", "b", "c", "d"}

pares = [(c,d) for c in C for d in D]

print(pares)