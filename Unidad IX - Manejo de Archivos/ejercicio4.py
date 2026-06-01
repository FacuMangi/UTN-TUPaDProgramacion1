productos = []

with open("productos.txt", "r", encoding="utf-8") as archivo:
    for linea in archivo:
        datos = linea.strip().split(",")
        
        producto_dicc = {
            "nombre": datos[0],
            "precio": float(datos[1]),
            "cantidad": int(datos[2])
        }
        
        productos.append(producto_dicc)

print(productos)
