def cargaHerramientas(cantidad: int) -> dict:
    inventario = {}
    # Se hace un loop que se ejecuta una cantidad de veces ingresada previamente por el user
    for _ in range(cantidad):
        # Se valida y se ingresa la herramienta
        while True:
            nombre = input("Ingrese el nombre de la herramienta: ").strip()
            if nombre and nombre.replace(" ", "").isalpha():
                nombre = nombre.title()
                if nombre in inventario:
                    print("Error: herramienta ya ingresada.")
                else:
                    break
            else:
                print("Error: nombre inválido (solo letras).")
        # Se valida y se ingresa el stock
        while True:
            cant = input("Ingrese la cantidad para esa herramienta: ").strip()
            if cant.isdigit() and int(cant) >= 0:
                cant = int(cant)
                break
            print("Error: ingrese una cantidad entera no negativa.")

        # Agreaga el nombre de la herramienta con su cantidad, si la herramienta ya esta en inventario, le agrega mas valor al que ya tenga
        inventario[nombre] = inventario.get(nombre, 0) + cant

    return inventario

def menu():
    inventario = []
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

        menu = {1, 2, 3, 4, 5, 6, 7, 8}
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
                # EL USUARIO INGRESA CANTIDAD DE HERRAMIENTAS A INGRESAR
                cantidad = input("Ingrese la cantidad de herramientas a ingresar: ")
                while not cantidad.isdigit() or int(cantidad) <0:
                    print("Error: ingrese un número entero positivo.")
                    cantidad = input("Ingrese la cantidad de herramientas a ingresar: ")
                cantidad = int(cantidad)

                # Llamo a cargaHerramientas, guardo el diccionario que devuelve en la variable herramientas
                herramientas = cargaHerramientas(cantidad)
                # Recorro las duplas de clave - valor y las agrego a la lista inventario
                for nombre, cant in herramientas.items():
                    inventario.append({nombre: cant})

menu()