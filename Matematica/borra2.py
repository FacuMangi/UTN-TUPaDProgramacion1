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
                    stringBase2 = int(stringBase2)
                    break
                else:
                    print("Error: ingrese un número válido.")

            nBase2 = []
            nBase2Inv = nBase2[::-1]
            numero = 0
            for i in range(len(nBase2)):
                numero += nBase2Inv[i] *2**i
                print(f"{numero} = {nBase2Inv[i]} * 2 ** {i}")

            print(numero)