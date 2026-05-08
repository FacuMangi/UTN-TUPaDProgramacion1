running = True
while running:
    print("Elige opcion:\n"
    "-1- Convertir de base 2 a base 10 \n"
    "-2- Convertir de base 10 a base 2 \n"
    "-3- Salir")

    # USO UN SISTEMA DE MENU QUE CREE ANTERIORMENTE, DONDE EN UN ARRAY DE NUMEROS ESTAN LAS OPCIONES VALIDAS
    # ESTE VALIDA QUE LA OPCION SEA UN NUMERO Y QUE ESTE ESTE EN EL ARRAY
    
    menu = {1, 2, 3}
    while True:
        opcion = input("Opcion: ").strip()
        if opcion.lstrip("+-").isdigit():
            opcion = int(opcion)
            if opcion in menu:
                break
            print("Error: opcion fuera de rango.")
        else:
            print("Error: ingrese un número válido.")

    match opcion:
        #CARGA INICIAL DE HERRAMIENTAS
        case 1:
            while True:
                stringBase2 = input("Ingrese numero en base 2 para convertir a base 10: ").strip()
                if stringBase2.lstrip("+-").isdigit():
                    break
                else:
                    print("Error: ingrese un número válido.")

            nBase2 = []
            for i in range(len(stringBase2)):
                nBase2.append(int(stringBase2[i]))

            nBase2Inv = nBase2[::-1]
            numero = 0
            for i in range(len(nBase2)):
                numero += nBase2Inv[i] *2**i

            print(numero)

        case 2:
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
                if 127 < cociente <= 32767:
                    palabra = 16
                elif cociente > 32767:
                    palabra = 32
                    print(palabra)
                else:
                    palabra = 8
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
                        break

                # Loop while que agrega ceros al array hasta que la cantidad de bits sea igual a palabra
                if len(numero) < palabra:
                    while len(numero) < palabra:
                        numero.append(0)
                        # Si la cantidad de bits en el array es igual a palabra break
                        if len(numero) == palabra:
                            break  

                bits = len(numero)
                nBinario = numero[::-1]
                stringNBinario = "".join(str(n) for n in nBinario)

                # Se imprime por pantalla el array invertido, con el bit menos significativo puesto al final.
                print(f"El numero en base 2 es: {stringNBinario} en un sistema de {bits} bits")

            # Condicional para numeros negativos
            elif cociente < 0:
                if -32768 <= cociente < -128:
                    palabra = 16
                elif cociente < -32768:
                    palabra = 32
                    print(palabra)
                else:
                    palabra = 8

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

                # Loop while que agrega ceros al array hasta que la cantidad de bits sea igual a palabra
                if len(numero) < palabra:
                    while len(numero) < palabra:
                        numero.append(0)
                        # Si la cantidad de bits en el array es igual a palabra break
                        if len(numero) == palabra:
                            break

                bits = len(numero)
                nBinario = numero[::-1]

                # Calcula complemento 1
                for i in range(len(nBinario)):
                    if nBinario[i] == 0:
                        nBinario[i] = 1
                    elif nBinario[i] == 1:
                        nBinario[i] = 0

                complemento = nBinario

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
                
                print(f"El numero en base 2 es: {complemento} en un sistema de {bits} bits")

        case 3:
            print("Terminando programa...")
            break