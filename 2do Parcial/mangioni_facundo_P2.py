# La funcion cargaHerramientas recibe la lista inventario y la modifica
def cargaHerramientas(inventario):
    while True:
        try:
            # EL USUARIO INGRESA CANTIDAD DE HERRAMIENTAS A INGRESAR
            cantidad = input("Ingrese la cantidad de herramientas a ingresar: ").strip()

            if not cantidad:
                raise ValueError("Error: cantidad vacio.")            
            if not cantidad.isdigit():
                raise ValueError("Error: cantidad no es un numero.")            
            if int(cantidad) <=0:
                raise ValueError("Error: cantidad es negativo o cero.")                          
                    
            cantidad = int(cantidad)
            break

        except ValueError as e:
            print(f"{e}\n")

    # Se hace un loop que se ejecuta una cantidad de veces igual a la cantidad ingresada previamente por el user
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
                
                # Hago busqueda en inventario por coincidencias. Si encuentra algo devuelve error por que se intenta ingresar una herramienta ya ingresada.
                for ele in inventario:
                    if ele["herramienta"] == nombre:
                        raise ValueError("Error: nombre ya cargado previamente.")
                break
            
            except ValueError as e:
                print(f"{e}\n")

        # Se valida y se ingresa el stock de la herramienta
        while True:
            try:

                cant = input(f'Ingrese la cantidad de stock para "{nombre}": ')

                if not cant:
                    raise ValueError("Error: cantidad vacio.")
                
                if not cant.isdigit():
                    raise ValueError("Error: cantidad no es un numero.")
                
                if int(cant) <=0:
                    raise ValueError("Error: cantidad es negativo o cero.")                          
                        
                cant = int(cant)
                break

            except ValueError as e:
                print(f"{e}\n")

        # Agreaga bajo las keys HERRAMIENTA y CANTIDAD el nombre ingresado con la cantidad ingresada al set paraAgregar.
        paraAgregar["herramienta"] = nombre
        paraAgregar["cantidad"] = cant

        # Se agrega paraAgregar a la lista INVENTARIO. Despues se vuelve a iterar el loop for para agregar la siguiente herramienta.
        inventario.append(paraAgregar)
    print("\n")

# Funcion que recorre los elementos de lista INVENTARIO y imprime todos los pares key|value de cada diccionario en inventario.  
def mostrarInventario(inventario):
    if len(inventario) == 0:
        print("No hay herramientas cargadas.")
    else:
        print(f"=== INVENTARIO ===")
        for ele in inventario:
            for key, value in ele.items():
                print(f"{key}: {value}")
    print("\n")

# Funcion que recorre el array que se le pase, busca el nombre en el key herramienta en los elementos de INVENTARIO y, si encuentra un match, devuelve mensaje con herramienta y su cantidad.
def buscarHerramienta(inventario):
    try:
        nombre = input("Ingresar herramienta para buscar: ").strip()

        if not nombre:
            raise ValueError("Error: nombre vacio.")
        if not nombre.replace(" ", "").isalpha():
            raise ValueError("Error: nombre invalido (solo letras).")
        
        nombre = nombre.lower()
        
        mensaje = ""
        for ele in inventario:
            if ele["herramienta"] == nombre:
                mensaje = f'Herramienta "{ele["herramienta"]}" tiene {ele["cantidad"]} unidades.\n'
        if mensaje == "":
            print(f'No se encontro la herramienta "{nombre}".\n')
        else:
            print(mensaje)

    except ValueError as e:
        print(f"{e}\n")

# Funcion que recorre los elementos de la lista INVENTARIO y, si el valor de la key CANTIDAD es igual a 0, se agrega al mensaje esa herramienta y luego se imprime un mensaje con todas las herramientas que esten en cantidad igual a 0.
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
            
            # Hago busqueda en inventario por coincidencias. Si encuentra algo devuelve error por que se intenta ingresar una herramienta ya ingresada.
            for ele in inventario:
                if ele["herramienta"] == nombre:
                    raise ValueError("Error: nombre ya cargado previamente.")
            break
        
        except ValueError as e:
            print(f"{e}\n")

    # Se valida y se ingresa el stock
    while True:
        try:

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
            print(f"{e}\n")

        # Agreaga bajo las keys HERRAMIENTA y CANTIDAD el nombre ingresado con la cantidad ingresada al set paraAgregar.
    paraAgregar["herramienta"] = nombre 
    paraAgregar["cantidad"] = cant

    # Se agrega paraAgregar a la lista INVENTARIO.
    inventario.append(paraAgregar)
    print("\n")

# La funcion recibe la lista INVENTARIO, busca la herramienta ingresada y actualiza su valor de stock.
def actualizarStock(inventario):
    try:
        # Se valida y se ingresa la herramienta a actualizar.
        nombre = input("Ingrese el nombre de la herramienta: ").strip()
        if not nombre:
            raise ValueError("Error: nombre vacio.")
        if not nombre.replace(" ", "").isalpha():
            raise ValueError("Error: nombre invalido (solo letras).")
        
        nombre = nombre.lower()

        # Pequenio menu que presenta las opciones. El input aqui tambien se valida.
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
                # Se ingresa el nuevo stock, se valida que sea un numero positivo.
                nuevoStock = input(f"Ingrese la cantidad a sumar para {nombre}: ").strip()
                if not nuevoStock.isdigit():
                    raise ValueError("Error: cantidad invalida.")
                nuevoStock = int(nuevoStock)
                if nuevoStock <= 0:
                    raise ValueError("Error: cantidad debe ser mayor que 0.")
                
                # Se recorre INVENTARIO, cuando encuentra una coincidencia con la variable nombre para la key HERRAMIENTA del elemento iterado, le actualiza el valor a la key CANTIDAD.
                for ele in inventario:
                    if ele["herramienta"] == nombre:
                        ele["cantidad"] += nuevoStock
                        print(f"Stock actualizado para {nombre} quedando con un total de: {ele["cantidad"]}")

            case 2:
                # Se ingresa el nuevo stock, se valida que sea un numero positivo.
                nuevoStock = input(f"Ingrese la cantidad a restar para {nombre}: ").strip()
                if not nuevoStock.isdigit():
                    raise ValueError("Error: cantidad invalida.")
                nuevoStock = int(nuevoStock)
                if nuevoStock <= 0:
                    raise ValueError("Error: cantidad debe ser mayor que 0.")
                
                # Se recorre INVENTARIO, cuando encuentra una coincidencia con la variable nombre para la key HERRAMIENTA del elemento iterado, se verifica que la cantidad a restar no de un numero menor que cero.
                for ele in inventario:
                    if ele["herramienta"] == nombre:
                        if ele["cantidad"] - nuevoStock >= 0:
                            ele["cantidad"] -= nuevoStock
                            print(f"Stock actualizado para {nombre} quedando con un total de: {ele["cantidad"]}")
                        # Si la resta entre el valor de ele["cantidad"] y nuevo stock da un numero negativo, el stock no se actualiza y se crea un ValueError.
                        else:
                            raise ValueError("Error: no hay suficiente stock.")
        print("\n")

    except ValueError as e:
        print(f"{e}\n")
    
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
                print(f"{e}\n")
            except Exception as e:
                # Captura fallos generales
                print(f"Se produjo un error inesperado en el MENU: {e}")

        match opcion:
            #CARGA INICIAL DE HERRAMIENTAS
            case 1:
                try:
                    cargaHerramientas(inventario)
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
                    buscarHerramienta(inventario)
                except Exception as e:
                # Captura fallos generales
                    print(f"Se produjo un error inesperado en OPCION 3: {e}")
            
            case 4:
                try:
                    mostrarAgotados(inventario)
                except Exception as e:
                # Captura fallos generales
                    print(f"Se produjo un error inesperado en OPCION 4: {e}")

            case 5:
                try:
                    cargaNuevoProd(inventario)
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