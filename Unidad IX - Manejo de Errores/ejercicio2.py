with open("productos.txt", "r") as archivo:
    for line in archivo:
        datos = line.strip().split(",")
        print(f"Producto: {datos[0]} | Precio: {datos[1]} | Cantidad: {datos[2]}")