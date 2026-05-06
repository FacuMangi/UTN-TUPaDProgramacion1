# Se pide por consola el numero al usuario
cociente = int(input("Ingrese numero en base 10 para convertir a base 2: "))

base = 2
# Condicionales para casos limite
if cociente == 0:
    print(f"Numero base 2: 0")

if cociente == 1:
    print(f"Numero base 2: 1")

# Condicional para caso normal
if cociente > 1:
    numero = []

    while True:
        # Agrego el resto al numero
        numero.append(cociente % base)
        # Redefino cociente como la division entera 
        cociente = cociente // base
        
        # Cuando el cociente llegue a 1 agrego un 1 extra, que es lo que se hace al final del proceso.
        if cociente == 1:
            numero.append(1)
            numero.append(0)
            break
    
    # Se imprime por pantalla el array invertido, con el bit menos significativo puesto al final.
    print(f"Numero base 2: {numero[::-1]}")

# Condicional para numeros negativos
elif cociente < 0:
    cociente = abs(cociente)
    numero = []

    # Primero convierto el valor absoluto a binario
    while True:
        # Agrego el resto al numero
        numero.append(cociente % base)
        # Redefino cociente como la division entera 
        cociente = cociente // base
        
        # Cuando el cociente llegue a 1 agrego un 1 extra, que es lo que se hace al final del proceso.
        if cociente == 1:
            numero.append(1)
            # si es positivo se agrega un cero
            if cociente > 0:
                numero.append(0)
            break

    numero = numero[::-1]

    # Segundo calculo su complemento a dos



# Agregar casosn limites (Numero 0, 1)
# Agregar casos numeros negativos