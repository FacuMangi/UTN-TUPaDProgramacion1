productos = []
# Leyendo los productos
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

# Sobre escribiendo archivo
with open("productos.txt", "w", encoding="utf-8") as archivo:
    # Recorro mi lista de diccionarios original, diccionario por diccionario
    for producto in productos:
        # Hago una lista con cada diccionario
        datos_linea=[            
            producto["nombre"],
            str(producto["precio"]),
            str(producto["cantidad"])
        ]
        # Uno los datos en un string
        linea = ",".join(datos_linea) + "\n"
        # Escribo la linea en el archivo
        archivo.write(linea)

print("Archivo productos actualizado.")

