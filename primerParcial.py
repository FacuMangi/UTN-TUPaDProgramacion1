herramientas = ["martillo", "taladro", "llave inglesa", "destornillador", "soplete"]
existencias = [50, 0, 30, 75, 0]
contador = 0

running = True
while running:
    print("Elige opcion:\n"
    "-1- Ingresar HERRAMIENTAS \n"
    "-2- Ingresar CANTIDADES \n"
    "-3- Visualizar Inventario\n"
    "-4- Buscar Herramienta\n"
    "-5- Reporte de Agotados\n"
    "-6- Alta de Nuevo Producto\n"
    "-7- Actualizacion de Stock\n"
    "-8- Salir")

    # USO UN SISTEMA DE MENU QUE CREE ANTERIORMENTE, DONDE EN UN ARRAY DE NUMEROS ESTAN LAS OPCIONES VALIDAS
    # 
    
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
            contador += cantidad #SETEO CONTADOR IGUAL A CANTIDAD Y SUMO MAS CANTIDADES SI ESTE NO ES 0

            for i in range(cantidad):
                while True:
                    herramienta = input("Ingrese el nombre de la herramienta: ").strip()
                    if herramienta.replace(" ", "").isalpha() and herramienta.lower() not in herramientas and herramienta != "":
                        herramientas.append(herramienta.lower())
                        break

        case 2:
            for h in range(len(herramientas), len(herramientas) + contador):
                existenciasH = input(f"Ingrese la cantidad para {herramientas[h]}: ")

                while not existenciasH.isdigit() or int(existenciasH) <0:
                    existenciasH = input(f"Ingrese la cantidad para {herramientas[h]}: ")
                existencias.append(int(existenciasH))
            contador = 0 #UNA VEZ INGRESADA LA CANTIDAD DE EXISTENCIAS DE CADA NUEVA HERRAMIENTA CONTADOR = 0

        case 3:
            print(f"=== INVENTARIO ===")
            for i in range(len(herramientas)):
                print(f"{herramientas[i]}: {existencias[i]}")

        case 4:
            while True:
                buscar = input("Ingrese el nombre de la herramienta: ").strip()
                if buscar.replace(" ", "").isalpha() and buscar != "":
                    buscar = buscar.lower()
                    break
            if buscar in herramientas:
                indice = herramientas.index(buscar)
                print(f"{herramientas[indice]}: {existencias[indice]}")
            else:
                print("No se encontro la herramienta en el catalogo.")

        case 5:
            print("Sin existencias: ")
            for i in range(len(existencias)):
                if existencias[i] == 0:
                    print(herramientas[i])

        case 6:
            herramienta = input("Ingrese el nombre de la herramienta: ").strip()
            if not herramienta.replace(" ", "").isalpha() or herramienta.lower() in herramientas or herramienta == "":                   
                continue
                        
            existenciasH = input(f"Ingrese la cantidad para {herramienta}: ")
            if not existenciasH.isdigit() or int(existenciasH) <0:
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

                    index = herramientas.index(herramienta)
                    menu = {1, 2}
                    print("-1- Agregar stock\n"
                          "-2- Restar stock")
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
                            existenciasH = input(f"Ingrese la cantidad a sumar para {herramienta}: ")
                            while not existenciasH.isdigit() or int(existenciasH) < 0:
                                print("Solo numeros postivios.")
                                existenciasH = input(f"Ingrese la cantidad a sumar para {herramienta}: ")
                            existencias[index] += (int(existenciasH))
                            break
                        case 2:
                            if existencias[index] == 0:
                                print(f"No hay suficientes existencias de {herramienta}.")
                                break

                            existenciasH = input(f"Ingrese la cantidad a restar para {herramienta}: ")
                            while not existenciasH.isdigit() or int(existenciasH) < 0:
                                print("Solo numeros postivios.")
                                existenciasH = input(f"Ingrese la cantidad a restar para {herramienta}: ")
                            if existencias[index] < int(existenciasH):
                                print(f"No hay suficientes existencias de {herramienta}.")
                                break
                            existencias[index] -= (int(existenciasH))
                            break
                    

        case 8:
            print("Terminando programa...")
            break

#OPCION 1 LA TENGO QUE DIVIDIR EN 2
#Informar mediante un mensaje claro si se intenta operar sobre una herramienta que no
#existe en el catálogo