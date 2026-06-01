inventario = [
    {"a":10},
    {"b":20}
]
# Funcion que recorre el array que se le pase, busca el nombre y si encuentra devuelve su valor asociado
def buscarHerramienta(inventario, nombre):
    for item in inventario:
        if nombre in item:
            return item[nombre]
    return None

# Funcion que devuelve la herramienta con su posicion en el inventario
def encontrar_item(inventario, nombre):
    nombre = nombre.strip().lower()
    for i, item in enumerate(inventario):
        if nombre in item:
            return i, item
    return None, None

def actualizarStock(inventario):
    nombre = input("Ingrese el nombre de la herramienta: ").strip()

    try:
        while True:
            print("-1- Agregar stock\n"
                  "-2- Restar stock")
            opcion = input("Opcion: ").strip()
            if not opcion.isdigit():
                raise ValueError("opción inválida")
            opcion = int(opcion)
            if opcion not in {1, 2}:
                raise ValueError("opción fuera de rango")
            break

        index, item = encontrar_item(inventario, nombre)
        if item is None:
            raise ValueError("Herramienta no encontrada.")

        stock_actual = item[nombre]

        match opcion:
            case 1:
                nuevoStock = input(f"Ingrese la cantidad a sumar para {nombre}: ")
                if not nuevoStock.isdigit():
                    raise ValueError("Error: cantidad invalida.")
                nuevoStock = int(nuevoStock)
                if nuevoStock <= 0:
                    raise ValueError("Error: cantidad debe ser > 0.")
                item[nombre] += nuevoStock

            case 2:
                nuevoStock = input(f"Ingrese la cantidad a restar para {nombre}: ")
                if not nuevoStock.isdigit():
                    raise ValueError("Error: cantidad invalida.")
                nuevoStock = int(nuevoStock)
                if nuevoStock <= 0:
                    raise ValueError("Error: cantidad debe ser > 0.")

                if stock_actual - nuevoStock >= 0:
                    item[nombre] -= nuevoStock
                else:
                    print("No alcanza el stock.")
    except ValueError as e:
        print(e)   # errores esperados de validación
    except Exception as e:
        print(f"Error inesperado: {e}")  # para depuración

actualizarStock(inventario)
print(inventario)

def actualizarStock(inventario):
    try:
        while True:
            while True:
                # Usuario ingresa el NOMBRE de le herramienta a actualizar stock
                try:
                    nombre = input("Ingrese el nombre de la herramienta: ").strip()
                    if not nombre:
                        raise ValueError("Error: nombre vacio.")
                    if not nombre.replace(" ", "").isalpha():
                        raise ValueError("Error: nombre invalido (solo letras).")
                                    
                    nombre = nombre.lower()

                    # Uso buscarHerramienta para verificar que la herramienta no este en inventario
                    if buscarHerramienta(inventario, nombre) is None:
                        raise ValueError("Error: no hay una herramienta con ese nombre.")
                    
                    break
                
                except ValueError as e:
                    print(e)
                
            menu = {1, 2}
            print("-1- Agregar stock\n"
                    "-2- Restar stock")
            # VERIFICACION DE INPUT SOLO OPCIONES VALIDAS 
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

            match opcion:
                # SE INICIALIZA Y SE VALIDA (QUE SEA NUMERO Y POSITIVO O CERO) EL NUMERO PARA SUMAR A EXISTENCIAS DE LA HERRAMIENTA
                case 1:
                    while True:
                        try:
                            nuevoStock = input(f"Ingrese la cantidad a sumar para {nombre}: ")
                            if not nuevoStock.isdigit():
                                raise ValueError("Error: la cantidad no es un numero.")
                            elif int(nuevoStock) <=0:
                                raise ValueError("Error: la cantidad es menor o igual a 0.")
                            nuevoStock = int(nuevoStock)
                            break
                        except ValueError as e:
                            print(e)

                    index, item = encontrar_item(inventario, nombre)
                    stock_actual = item[nombre]
                    item[nombre] = nuevoStock
                    
                case 2:
                    while True:
                        try:
                            nuevoStock = input(f"Ingrese la cantidad a restar para {nombre}: ")
                            if not nuevoStock.isdigit():
                                raise ValueError("Error: la cantidad no es un numero.")
                            elif int(nuevoStock) <=0:
                                raise ValueError("Error: la cantidad es menor o igual a 0.")
                            nuevoStock = int(nuevoStock)
                            break
                        except ValueError as e:
                            print(e)
                    
                    index, item = encontrar_item(inventario, nombre)
                    stock_actual = item[nombre]
                    if stock_actual - nuevoStock >= 0:
                        item[nombre] = stock_actual - nuevoStock
                    else:
                        print("No se puede restar esa cantidad, no hay suficiente stock.")

        
    except Exception as e:
        # Captura fallos generales
        print(f"Se produjo un error inesperado: {e}")