with open("productos.txt", "r") as archivo:
    for line in archivo:
        datos = line.strip().split(",")
        print(f"Producto: {datos[0]} | Precio: {datos[1]} | Cantidad: {datos[2]}")

producto = input("Ingrese un nuevo producto (nombre, precio,cantidad): ")
lista_limpia = [p.strip() for p in producto.split(",")]

with open("productos.txt", "a") as archivo:
    archivo.write(f"\n{lista_limpia[0]},{lista_limpia[1]},{lista_limpia[2]}")