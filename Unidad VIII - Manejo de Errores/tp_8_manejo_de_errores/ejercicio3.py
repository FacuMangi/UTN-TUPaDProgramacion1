a = 10
b = input("Introduce un número: ")

# Manejo del error TypeError
try:
    result = a/b 
    print(f"Resultado: {result}")
except TypeError as e:
    print(f"Error: {e}. No se puede dividir un numero por un texto.")

numbers = [1, 2, 3]
# Manejo del error IndexError
try:
    print(numbers[5])
except IndexError as e:
    print(f"Error: {e}. Fuera de rango.")