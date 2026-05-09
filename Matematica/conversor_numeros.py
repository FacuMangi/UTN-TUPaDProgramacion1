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
        case 1:
            while True:
                stringBase2 = input("Ingrese numero en base 2 para convertir a base 10 (En sistema de 8, 26 o 32 bits): ").strip()
                if stringBase2.lstrip("+-").isdigit():
                    stringBase2 = stringBase2.lstrip("+-")
                    break
                else:
                    print("Error: ingrese un número válido.")

            # Seteando flag
            noBinario = False
            
            # Para hacer el array con el numero ingresado, se itera sobre el string y cada elemento de la cadena se convierte en un integer
            nBase2 = []

            for i in range(len(stringBase2)):
                # Como validacion extra se revisa que los valores de cada elemento de la cadena sean 1 o 0.
                if int(stringBase2[i]) != 1 and int(stringBase2[i]) != 0:
                    # Si NO son 1 y NO son 0, se activa la flag y sale del for loop.
                    noBinario = True
                    break
                nBase2.append(int(stringBase2[i]))
            
            
            # Si la flag esta activa se imprime un mensaje y se sale del case.
            if noBinario:
                print("El numero ingresado no es de base 2.")
                continue

            # Si el primer elemento de nBase2 es 0 (el bit mas significativo), quiere decir que el numero es positivo
            if nBase2[0] == 0:
                # Se invierte el array y empieza el proceso de conversion. Seria como arrancar de izquierda a derecha en el numero original.
                nBase2Inv = nBase2[::-1]
                # Se setea el numero en 0 para ir sumando las potencias de 2 multiplicadas por los 1 y 0
                numero = 0
                for i in range(len(nBase2)):
                    # Se hace la suma por cada elemento del array
                    numero += nBase2Inv[i] *2**i
            
            # Si el primer elemento de nBase2 es 1 (el bit mas significativo), quiere decir que es negativo.
            else:

                # Calcula complemento 1
                for i in range(len(nBase2)):
                    if nBase2[i] == 0:
                        nBase2[i] = 1
                    elif nBase2[i] == 1:
                        nBase2[i] = 0

                # Le sumo 1 
                for i in range(len(nBase2)-1, -1, -1):
                    if nBase2[i] == 1:
                        nBase2[i] = 0
                        if i == 0:
                            nBase2.insert(0, 1)
                        continue
                    if nBase2[i] == 0:
                        nBase2[i] = 1
                        break
                
                # Se invierte el array y empieza el proceso de conversion. Seria como arrancar de izquierda a derecha en el numero original.
                nBase2Inv = nBase2[::-1]
                # Se setea el numero en 0 para ir sumando las potencias de 2 multiplicadas por los 1 y 0
                numero = 0
                for i in range(len(nBase2)):
                    # Se hace la suma por cada elemento del array
                    numero += nBase2Inv[i] *2**i
                numero = -1*numero

            print(f"El numero en base 10 es: {numero}.")

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
                # Se invierte el array para que el numero en base 2 se lea de izquierda a derecha.
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

                # Se invierte el array para que el numero en base 2 se lea de izquierda a derecha.
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
                
                stringNBinario = "".join(str(n) for n in complemento)
                
                print(f"El numero en base 2 es: {stringNBinario} en un sistema de {bits} bits")

        case 3:
            print("Terminando programa...")
            break