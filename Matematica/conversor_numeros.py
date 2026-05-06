# Se pide por consola el numero al usuario
while True:
        cociente = input("Ingrese numero en base 10 para convertir a base 2: ").strip()
        if cociente.lstrip("+-").isdigit():
            cociente = int(cociente)
            break
        else:
            print("Error: ingrese un número válido.")


base = 2

# Condicional para caso normal
if cociente >= 0:
    numero = []

    while True:
        # Caso limite 1
        if cociente == 0:
            numero.append(0)
            break

        # Caso limite 1
        if cociente == 1:
            numero.append(1)
            break

        # Agrego el resto al numero
        numero.append(cociente % base)
        # Redefino cociente como la division entera 
        cociente = cociente // base
        
        # Cuando el cociente llegue a 1 agrego un 1 extra, que es lo que se hace al final del proceso.
        if cociente == 1:
            numero.append(1)
            numero.append(0)
            break

    # Loop while que agrega ceros al array hasta que la cantidad de bits sea multiplo de 8
    if len(numero) % 8 != 0:
        while len(numero) % 8 != 0:
            numero.append(0)
            # Si la cantidad de bits en el array es multiplo de 8 Break
            if len(numero) % 8 == 0:
                break    

    palabra = len(numero)
    nBinario = numero[::-1]
    
    # Se imprime por pantalla el array invertido, con el bit menos significativo puesto al final.
    print(f"El numero en base 2 es: {nBinario} en un sistema de {palabra} bits")

# Condicional para numeros negativos
elif cociente < 0:

    base = 2

    numero = []
    while True:
        # Caso limite -1
        if cociente == -1:
            numero.append(1)
            break

        # Agrego el resto al numero
        numero.append(abs(cociente) % base)
        # Redefino cociente como la division entera 
        cociente = abs(cociente) // base
        
        # Cuando el cociente llegue a 1 agrego un 1 extra, que es lo que se hace al final del proceso.
        if cociente == 1:
            numero.append(1)
            break

    # Loop while que agrega ceros al array hasta que la cantidad de bits sea multiplo de 8
    if len(numero) % 8 != 0:
        while len(numero) % 8 != 0:
            numero.append(0)
            # Si la cantidad de bits en el array es multiplo de 8 Break
            if len(numero) % 8 == 0:
                break

    print(f"Numero en base 2: {numero[::-1]}")

    palabra = len(numero)
    nBinario = numero[::-1]

    for i in range(len(nBinario)):
        if nBinario[i] == 0:
            nBinario[i] = 1
        elif nBinario[i] == 1:
            nBinario[i] = 0

    complemento = nBinario
    print(f"Complemento 1: {complemento}")

    # Recorro el complemento desde la derecha a la izquierda
    # El loop recorre de derecha a izquierda cambiando todos los 1 por 0. Cuando se encuentra un 0, cambia este a 1 y se corta el loop. Esto es porque se usa el carry y a partir de ahi es lo mismo que ir sumando cero. O sea, no cambia el numero.
    for i in range(len(complemento)-1, -1, -1):
        if complemento[i] == 1:
            complemento[i] = 0
            if i == 0:
                complemento.insert(0, 1)
            continue
        if complemento[i] == 0:
            complemento[i] = 1
            break
    
    print(f"El numero en base 2 es: {complemento} en un sistema de {palabra} bits")

