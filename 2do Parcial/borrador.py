def cargaHerramientas(cantidad: int) -> dict:
    inventario = {}
    # Se hace un loop que se ejecuta una cantidad de veces ingresada previamente por el user
    for _ in range(cantidad):
        # Se valida y se ingresa la herramienta
        while True:
            nombre = input("Ingrese el nombre de la herramienta: ").strip()
            if nombre and nombre.replace(" ", "").isalpha():
                nombre = nombre.lower()
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
    
def mostrarInventario(inventario):
    if len(inventario) == 0:
        print("No hay herramientas cargadas.")
    print(f"=== INVENTARIO ===")
    for ele in inventario:
        for key, value in ele.items():
            print(f"Herramienta: {key}, existencias: {value}")

def buscarHerramienta(inventario, nombre):
    # Recorre el array que se le pase, busca el nombre y se encuentra devuelve el valor asociado al nombre
    for item in inventario:
        if nombre in item:
            return item[nombre]
    return None
    
def menu():
    inventario = [{"martillo": 20}]
    running = True
    while running:
        print("Elige opcion:\n"
        "-1- Ingresar HERRAMIENTAS \n"
        "-2- Visualizar Inventario\n"
        "-3- Buscar Herramienta \n"
        "-4- Ingresar EXISTENCIAS\n"
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

            case 2:
            # Por ahora print a la lista de diccionarios
                mostrarInventario(inventario)

            case 3:
                # Se pide ingresar herramienta a buscar
                while True:
                    nombre = input("Ingrese el nombre de la herramienta: ").strip()
                    if nombre and nombre.replace(" ", "").isalpha():
                        nombre = nombre.lower()
                        break
                    else:
                        print("Error: nombre inválido (solo letras).")
                # Se llama funcion de busqueda, si da None imprime mensaje, sino imprime stock
                stock = buscarHerramienta(inventario, nombre)
                if stock is None:
                    print("La herramienta no se encuentra en el inventario.")
                else:
                    print(f"Stock de {nombre}: {stock}")
menu()