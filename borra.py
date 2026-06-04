def transform(string):
    try:
        if int(string) > 0:
            return int(string)
        raise ValueError("Hola")
    except ValueError as e:
        print(e)


def main():
    print("EJECUTANDO MAIN")
    try:
        numero = transform(input("Ingrese un numero positivo: "))
        if numero is None:
            raise 
        print(numero)
    except Exception as e:
        print(e)
#main()

def addTool(inventario):
    for i in range(2):
        toAdd = {}
        nombre = input("Herramienta: ")
        cantidad = int(input("Cantidad: "))

        toAdd["herramienta"] = nombre
        toAdd["cantidad"] = cantidad
        
        inventario.append(toAdd)

inventario = [{"herramienta": "martillo", "cantidad": 20}, {"herramienta": "soplete", "cantidad": 1},
              {"herramienta": "destornillador", "cantidad": 0}]
addTool(inventario)

print(inventario)

def mostrarInventario(inventario):
    if len(inventario) == 0:
        print("No hay herramientas cargadas.")
    print(f"=== INVENTARIO ===")
    for ele in inventario:
        for key, value in ele.items():
            print(f"{key}: {value}")

#mostrarInventario(inventario)

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

#buscarTool(inventario)

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
        
#mostrarAgotados(inventario)

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

#print(inventario)

#actualizarStock(inventario)