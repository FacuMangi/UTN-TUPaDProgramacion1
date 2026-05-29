productos = []

with open("productos.txt", "r", encoding="utf-8") as archivo:
    for linea in archivo:
        datos = linea.strip().split(",")
        # Mientras abro el archivo con with, recorro cada linea con un for 
        # y creo un diccionario para cada producto
        producto_dicc = {
            "nombre": datos[0],
            "precio": float(datos[1]),
            "cantidad": int(datos[2])
        }
        # Agrego los diccionarios a la lista creada al inicio
        productos.append(producto_dicc)

print(productos)

busqueda = input("Ingrese el nombre del producto: ").strip()

encontrado = False
# Loop que busca en la lista
for producto in productos:
    if producto["nombre"].lower() == busqueda.lower():
        print(f"Producto: {producto["nombre"]} | Precio: {producto["precio"]} | Cantidad: {producto["cantidad"]}")
        encontrado = True
        break

if not encontrado:
    print(f"\nError: {busqueda} no se encontro.")