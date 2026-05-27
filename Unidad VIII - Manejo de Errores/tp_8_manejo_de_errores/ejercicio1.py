a = 10
b = input("Introduce un número: ")
result = a / b  # TypeError. 'b' es un string porque input() siempre devuelve un string, y no se puede dividir un número por texto.
print(f"Resultado: {result}")
numbers = [1, 2, 3]
print(numbers[5]) # IndexError. El índice 5 está fuera de rango; la lista solo tiene elementos hasta el índice 2.