# La funcion cargaHerramientas recibe un valor cantidad y el inventario y devuelve un diccionario con herramientas nuevas que se agregaran a inventario mas adelante.
def cargaHerramientas(inventario):
    while True:
        try:
            # EL USUARIO INGRESA CANTIDAD DE HERRAMIENTAS A INGRESAR
            cantidad = input("Ingrese la cantidad de herramientas a ingresar: ")

            if not cantidad:
                raise ValueError("Error: cantidad vacio.")
            
            if not cantidad.isdigit():
                raise ValueError("Error: cantidad no es un numero.")
            
            if int(cantidad) <=0:
                raise ValueError("Error: cantidad es negativo o cero.")                          
                    
            cantidad = int(cantidad)
            break

        except ValueError as e:
            print(e)

    # Se hace un loop que se ejecuta una cantidad de veces ingresada previamente por el user
    for _ in range(cantidad):
        paraAgregar = {}
        # Se valida y se ingresa la herramienta
        while True:
            try:
                nombre = input("Ingrese el nombre de la herramienta: ").strip()

                if not nombre:
                    raise ValueError("Error: nombre vacio.")
                if not nombre.replace(" ", "").isalpha():
                    raise ValueError("Error: nombre invalido (solo letras).")
                                
                nombre = nombre.lower()
                
                # Uso buscarHerramienta para verificar que la herramienta no este en inventario
                if buscarHerramienta(inventario, nombre) is not None:
                    raise ValueError("Error: nombre ya cargado previamente.")
                break
            
            except ValueError as e:
                print(e)

        # Se valida y se ingresa el stock
        while True:
            try:
                # EL USUARIO INGRESA CANTIDAD DE STOCK
                cant = input(f"Ingrese la cantidad de stock para {nombre}: ")

                if not cant:
                    raise ValueError("Error: cantidad vacio.")
                
                if not cant.isdigit():
                    raise ValueError("Error: cantidad no es un numero.")
                
                if int(cant) <=0:
                    raise ValueError("Error: cantidad es negativo o cero.")                          
                        
                cant = int(cant)
                break

            except ValueError as e:
                print(e)

            # Agreaga el nombre de la herramienta con su cantidad, si la herramienta ya esta en inventario, le agrega mas valor al que ya tenga
            paraAgregar["herramienta"] = nombre
            paraAgregar["cantidad"] = cant

            inventario.append(paraAgregar)
    
def mostrarInventario(inventario):
    if len(inventario) == 0:
        print("No hay herramientas cargadas.")
    print(f"=== INVENTARIO ===")
    for ele in inventario:
        for key, value in ele.items():
            print(f"{key}: {value}")

# Funcion que recorre el array que se le pase, busca el nombre en el key herramienta y si encuentra un match devuelve mensaje con herramienta y cantidad
def buscarHerramienta(inventario):
    nombre = input("Ingresar herramienta para buscar: ")
    nombre = nombre.strip().lower()
    mensaje = ""
    for ele in inventario:
        if ele["herramienta"] == nombre:
            mensaje = f'Herramienta "{ele["herramienta"]}" tiene {ele["cantidad"]} unidades.'
    if mensaje == "":
        print(f'No se encontro la herramienta "{nombre}".')
    else:
        print(mensaje)
# Funcion que devuelve la herramienta con su posicion en el inventario
def encontrar_item(inventario, nombre):
    nombre = nombre.strip().lower()
    for i, item in enumerate(inventario):
        if nombre in item:
            return i, item
    return None, None

def mostrarAgotados(inventario):
    contador = 0
    mensaje = "Herramientas sin stock:\n"
    for ele in inventario:
        if ele["cantidad"] == 0:
            contador += 1
            mensaje += f"{ele["herramienta"]}\n"
    if contador == 0:
        print("No hay herramientas con stock faltante.")
    else:
        print(mensaje)

# La funcion cargaNuevoProd recibe el inventario y devuelve un diccionario con el producto nuevo
def cargaNuevoProd(inventario):
    paraAgregar = {}
    # Se valida y se ingresa la herramienta
    while True:
        try:
            nombre = input("Ingrese el nombre de la herramienta: ").strip()

            if not nombre:
                raise ValueError("Error: nombre vacio.")
            if not nombre.replace(" ", "").isalpha():
                raise ValueError("Error: nombre invalido (solo letras).")
                            
            nombre = nombre.lower()
            
            # Uso buscarHerramienta para verificar que la herramienta no este en inventario
            if buscarHerramienta(inventario, nombre) is not None:
                raise ValueError("Error: nombre ya cargado previamente.")
            break
        
        except ValueError as e:
            print(e)

    # Se valida y se ingresa el stock
    while True:
        try:
            # EL USUARIO INGRESA CANTIDAD DE STOCK
            cant = input(f"Ingrese la cantidad de stock para {nombre}: ")

            if not cant:
                raise ValueError("Error: cantidad vacio.")
            
            if not cant.isdigit():
                raise ValueError("Error: cantidad no es un numero.")
            
            if int(cant) <=0:
                raise ValueError("Error: cantidad es negativo o cero.")                          
                    
            cant = int(cant)
            break

        except ValueError as e:
            print(e)

        # Agreaga el nombre de la herramienta con su cantidad, si la herramienta ya esta en inventario, le agrega mas valor al que ya tenga
        paraAgregar["herramienta"] = nombre
        paraAgregar["cantidad"] = cant

        inventario.append(paraAgregar)

def actualizarStock(inventario):
    try:
        nombre = input("Ingrese el nombre de la herramienta: ").strip()
        if not nombre.isalpha():
            raise ValueError("Error: solo valores alfabeticos.")

        while True:
            print("-1- Agregar stock\n"
                  "-2- Restar stock")
            
            opcion = input("Opcion: ").strip()

            if not opcion.isdigit():
                raise ValueError("Error: opción inválida.")
            
            opcion = int(opcion)

            if opcion not in {1, 2}:
                raise ValueError("Error: opción fuera de rango.")
            
            break

        match opcion:
            case 1:
                nuevoStock = input(f"Ingrese la cantidad a sumar para {nombre}: ").strip()
                if not nuevoStock.isdigit():
                    raise ValueError("Error: cantidad invalida.")
                nuevoStock = int(nuevoStock)
                if nuevoStock <= 0:
                    raise ValueError("Error: cantidad debe ser > 0.")
                
                for ele in inventario:
                    if ele["herramienta"] == nombre:
                        ele["cantidad"] += nuevoStock
                        print(f"Stock actualizado para {nombre} quedando con un total de: {ele["cantidad"]}")

            case 2:
                nuevoStock = input(f"Ingrese la cantidad a restar para {nombre}: ").strip()
                if not nuevoStock.isdigit():
                    raise ValueError("Error: cantidad invalida.")
                nuevoStock = int(nuevoStock)
                if nuevoStock <= 0:
                    raise ValueError("Error: cantidad debe ser > 0.")
                
                for ele in inventario:
                    if ele["herramienta"] == nombre:
                        if ele["cantidad"] - nuevoStock >= 0:
                            ele["cantidad"] -= nuevoStock
                            print(f"Stock actualizado para {nombre} quedando con un total de: {ele["cantidad"]}")
                        else:
                            raise ValueError("Error: no hay suficiente stock.")

    except ValueError as e:
        print(e)
    
def menu():
    inventario = [{"herramienta": "martillo", "cantidad": 20}, {"herramienta": "soplete", "cantidad": 0}]
    running = True
    while running:
        print("Elige opcion:\n"
        "-1- Ingresar HERRAMIENTAS \n"
        "-2- Visualizar Inventario\n"
        "-3- Buscar Herramienta \n"
        "-4- Reporte de Agotados\n"
        "-5- Alta de Nuevo Producto\n"
        "-6- Actualizacion de Stock\n"
        "-7- Salir\n")

        menu = {1, 2, 3, 4, 5, 6, 7, 8}
        while True:
            try:
                opcion = input("Opcion: ").strip()
                if not opcion:
                    raise ValueError("Error: opcion vacia.")
                if not opcion.isdigit():
                    raise ValueError("Error: opcion no es un numero.")
                if int(opcion) not in menu:
                    raise ValueError("Error: opcion no esta en el menu.")
                opcion = int(opcion)
                break
            except ValueError as e:
                print(e)
            except Exception as e:
                # Captura fallos generales
                print(f"Se produjo un error inesperado en el MENU: {e}")

        match opcion:
            #CARGA INICIAL DE HERRAMIENTAS
            case 1:
                try:
                    # Llamo a cargaHerramientas, guardo el diccionario que devuelve en la variable herramientas
                    herramientas = cargaHerramientas(cantidad, inventario)

                    # Recorro las duplas de clave - valor y las agrego a la lista inventario
                    for nombre, cant in herramientas.items():
                        inventario.append({nombre: cant})

                except Exception as e:
                # Captura fallos generales
                    print(f"Se produjo un error inesperado en OPCION 1: {e}")

            case 2:
                try:
                # Por ahora print a la lista de diccionarios
                    mostrarInventario(inventario)
                except Exception as e:
                # Captura fallos generales
                    print(f"Se produjo un error inesperado en OPCION 2: {e}")

            case 3:
                try:
                    # Se pide ingresar herramienta a buscar
                    while True:
                        try:
                            nombre = input("Ingrese el nombre de la herramienta: ").strip()
                            if not nombre:
                                raise ValueError("Error: nombre vacio")
                            if not nombre.replace(" ", "").isalpha():
                                raise ValueError("Error: nombre invalido (solo letras).")
                                
                            nombre = nombre.lower()
                            break

                        except ValueError as e:
                            print(e)

                    # Se llama funcion de busqueda, si da None imprime mensaje, sino imprime stock
                    stock = buscarHerramienta(inventario, nombre)

                    if stock is None:
                        print("La herramienta no se encuentra en el inventario.")
                    else:
                        print(f"Stock de {nombre}: {stock}")

                except Exception as e:
                # Captura fallos generales
                    print(f"Se produjo un error inesperado en OPCION 3: {e}")
            
            case 4:
                try:
                    mensaje = mostrarAgotados(inventario)
                    print(mensaje)

                except Exception as e:
                # Captura fallos generales
                    print(f"Se produjo un error inesperado en OPCION 4: {e}")

            case 5:
                try:
                    prod = cargaNuevoProd(inventario)
                    if prod != None:
                        inventario.append(prod)
                except Exception as e:
                # Captura fallos generales
                    print(f"Se produjo un error inesperado en OPCION 5: {e}")
            
            case 6:
                try:
                    actualizarStock(inventario)
                except Exception as e:
                    print(f"Se produjo un error inesperado en OPCION 6: {e}")
            
            case 7:
                break

menu()