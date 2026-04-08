herramientas = ["martillo", "taladro", "llave inglesa", "destornillador", "soplete"]
existencias = [50, 0, 30, 75, 0]
contador = 0

running = True
while running:
    print("Elige opcion:\n"
    "-1- Ingresar HERRAMIENTAS \n"
    "-2- Ingresar EXISTENCIAS \n"
    "-3- Visualizar Inventario\n"
    "-4- Buscar Herramienta\n"
    "-5- Reporte de Agotados\n"
    "-6- Alta de Nuevo Producto\n"
    "-7- Actualizacion de Stock\n"
    "-8- Salir")

    # USO UN SISTEMA DE MENU QUE CREE ANTERIORMENTE, DONDE EN UN ARRAY DE NUMEROS ESTAN LAS OPCIONES VALIDAS
    # ESTE VALIDA QUE LA OPCION SEA UN NUMERO Y QUE ESTE ESTE EN EL ARRAY
    
    menu = {1, 2, 3, 4, 5, 6, 7}
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
        # EL USUARIO INGRESA CANTIDAD DE HERRAMIENTAS A INGRESAR
        # SE VALIDA QUE SEA UN NUMERO POSITIVO Y SE LE SUMA ESE VALOR A CONTADOR
        # POR DEFAULT CONTADOR ES 0
            cantidad = input("Ingrese la cantidad de herramientas a ingresar: ")

            while not cantidad.isdigit() or int(cantidad) <0:
                print("Error: ingrese un número entero positivo.")
                cantidad = input("Ingrese la cantidad de herramientas a ingresar: ")
            cantidad = int(cantidad)
            # SETEO CONTADOR IGUAL A CANTIDAD Y SUMO MAS CANTIDADES SI ESTE NO ES 0
            contador += cantidad 
            for i in range(cantidad):
                while True:
                    # LA VALIDACION ES VERIFICAR QUE TODOS LOS CARACTERES SEAN ALPHA (MOMENTANEAMENTE SE SCA EL ESPACIO PARA ESO), QUE NO ESTE EN HERRAMIENTAS Y QUE NO SEA UN VACIO
                    herramienta = input("Ingrese el nombre de la herramienta: ").strip()
                    if herramienta.replace(" ", "").isalpha() and herramienta.lower() not in herramientas and herramienta != "":
                        herramientas.append(herramienta.lower())
                        break

        case 2:
        # PARA INGRESAR LAS EXISTENCIAS SE ITERA SOBRE LA LISTA DE HERRAMIENTAS
        # UN FOR EMPIEZA RECORRIENDO DESDE:
        # EL ULTIMO ELEMENTO HACIA ATRAS UNA CANTIDAD {CONTADOR} DE VECES (ESTO SERIA DESDE EL PRIMER LUGAR DE LAS NUEVAS HERRAMIENTAS INGRESADAS)
        # HASTA EL ULTIMO ELEMENTO DE HERRAMIENTAS + 1 (PORQUE LA FUNCION RANGE SOLO VA HASTA EL NUMERO ANTERIOR AL FINAL) (ESTO SERIA HASTA EL ULTIMO LUGAR DE LAS HERRAMIENTAS INGRESADAS)
        # ESTO ES PARA MANTENER COHERENCIA ENTRE LA LISTA HERRAMIENTAS Y LA LISTA EXISTENCIAS
            if contador > 0:
                for h in range(herramientas.index(herramientas[-contador]), herramientas.index(herramientas[-1])+1):
                    existenciasH = input(f"Ingrese la cantidad para {herramientas[h]}: ")

                    while not existenciasH.isdigit() or int(existenciasH) < 0:
                        existenciasH = input(f"Ingrese la cantidad para {herramientas[h]}: ")
                    existencias.append(int(existenciasH))
                # UNA VEZ INGRESADA LA CANTIDAD DE EXISTENCIAS DE CADA NUEVA HERRAMIENTA CONTADOR = 0
                contador = 0
            else:
                print ("No hay herramientas cargadas.") 

        case 3:
            # EL FOR RECORRE UN RANGO IGUAL A LA CANTIDAD DE ELEMENTOS EN EXISTENCIAS
            # ESTO ES ASI PARA QUE SI SE ESTAN INGRESANDO HERRAMIENTAS PERO AUN NO SE INGRESARON LAS CANTIDADES, NO SALTE UN ERROR A LA HORA DE RECORRER AMBOS ARRAYS
            print(f"=== INVENTARIO ===")
            for i in range(len(existencias)):
                print(f"-- {herramientas[i]}: {existencias[i]}")

        case 4:
            # EL USUARIO INGRESA EL NOMBRE DE LA HERRAMIENTA A BUSCAR
            while True:
                buscar = input("Ingrese el nombre de la herramienta: ").strip()
                # SE VALIDA EL INPUT
                if buscar.replace(" ", "").isalpha() and buscar != "":
                    buscar = buscar.lower()
                    break
            # VERIFICA QUE LA HERRAMIENTA ESTE EN HERRAMIENTAS
            if buscar in herramientas:
                # SI ESTA, SACO EL INDEX DE ESA HERRAMIENTA EN HERRAMIENTAS
                indice = herramientas.index(buscar)
                # PARA ASEGURAR QUE LA VALIDACION ESTE BIEN HECHA TENGO QUE FIJARME DE QUE INDICE TOMA. SI HAY COSAS REPETIDAS EN LA LISTA, CUANDO BUSQUE INDEX DE ESO ME VA A DEVOLVER LA PRIMER COINCIDENCIA.
                # LA VALIDACION DE QUE LA HERRAMIENTA TENGA EXISTENCIAS ES QUE SU INDICE SEA MENOR QUE LA CANTIDAD DE INDICES QUE TENGA EXISTENCIAS (USANDO LEN Y RESTANDO 1)
                if len(existencias)-1 >= indice:
                    print(f"{herramientas[indice]}: {existencias[indice]}")
                else:
                    print(f'No hay existencias cargadas para "{buscar}"')
            else:
                print("No se encontro la herramienta en el catalogo.")

        case 5:
            # LOOPEO SOBRE LA LISTA EXISTENCIAS Y SI EL VALOR ES 0 IMPRIME LA HERRAMIETNTA CORRESPONDIENTE AL INDICE DE ESA EXISTENCIA CON VALOR 0
            print("Sin existencias: ")
            for i in range(len(existencias)):
                if existencias[i] == 0:
                    print(herramientas[i])

        case 6:
            # EL USUARIO INGRESA EL NOMBRE DE LA HERRAMIENTA A AGREGAR
            herramienta = input("Ingrese el nombre de la herramienta: ").strip()
            # SE VALIDA EL INPUT, QUE NO TENGA NUMEROS, QUE NO ESTE EN HERRAMIENTAS Y QUE NO SEA UN VACIO
            if not herramienta.replace(" ", "").isalpha() or herramienta.lower() in herramientas or herramienta == "":                   
                continue
                        
            existenciasH = input(f"Ingrese la cantidad para {herramienta}: ")
            if not existenciasH.isdigit() or int(existenciasH) < 0:
                continue

            herramientas.append(herramienta.lower())
            existencias.append(int(existenciasH))

        case 7:
            while True:
                herramienta = input("Ingrese el nombre de la herramienta: ").strip()
                if herramienta.replace(" ", "").isalpha() and herramienta != "":
                    #VERIFICA QUE ESTE EN EL CATALOGO
                    if herramienta.lower() not in herramientas:
                        print("La herramienta no esta en el catalogo.")
                        break 
                    # INICIALIZO VARIABLE INDEX COMO EL INDEX DE LA HERRAMIENTA
                    index = herramientas.index(herramienta)
                    menu = {1, 2}
                    print("-1- Agregar stock\n"
                          "-2- Restar stock")
                    # VERIFICACION DE INPUT SOLO OPCIONES VALIDAS 
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
                        # SE INICIALIZA Y SE VALIDA (QUE SEA NUMERO Y POSITIVO O CERO) EL NUMERO PARA SUMAR A EXISTENCIAS DE LA HERRAMIENTA
                        case 1:
                            existenciasH = input(f"Ingrese la cantidad a sumar para {herramienta}: ")
                            while not existenciasH.isdigit() or int(existenciasH) < 0:
                                print("Solo numeros postivios.")
                                existenciasH = input(f"Ingrese la cantidad a sumar para {herramienta}: ")
                            # A EXISTENCIA CON INDEX IGUAL A HERRAMIENTA SE LE SUMA EL NUMERO
                            existencias[index] += (int(existenciasH))
                            break
                        case 2:
                            # ANTES DE PREGUNTAR SE VERIFICA QUE EXISTENCIA DE HERRAMIENTA NO SEA 0
                            if existencias[index] == 0:
                                print(f"No hay suficientes existencias de {herramienta}.")
                                break

                            existenciasH = input(f"Ingrese la cantidad a restar para {herramienta}: ")
                            while not existenciasH.isdigit() or int(existenciasH) < 0:
                                print("Solo numeros postivios.")
                                existenciasH = input(f"Ingrese la cantidad a restar para {herramienta}: ")
                            # SI EXISTENCIA DE HERRAMIENTA ES MENOR AL INPUT RESTA DA MENOS QUE 0 Y NO SE PERMITE
                            if existencias[index] < int(existenciasH):
                                print(f"No hay suficientes existencias de {herramienta}.")
                                break
                            # A EXISTENCIA CON INDEX IGUAL A HERRAMIENTA SE LE RESTA EL NUMERO
                            existencias[index] -= (int(existenciasH))
                            break
                    
        case 8:
            print("Terminando programa...")
            break

#OPCION 1 LA TENGO QUE DIVIDIR EN 2
#Informar mediante un mensaje claro si se intenta operar sobre una herramienta que no
#existe en el catálogo