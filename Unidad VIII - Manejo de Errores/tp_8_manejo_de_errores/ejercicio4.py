a = 10
b = input("Introduce un número: ")
numbers = [1, 2, 3]
try:
    result = a/b
    print(numbers[5])

except TypeError as e:
    print(f"Error: {e}. No se puede dividir un numero por un texto.")
   
except IndexError as e:
    print(f"Error: {e}. Fuera de rango.")