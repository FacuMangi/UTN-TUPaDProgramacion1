codigo = "pito"
codigo_parcial = "" 

while True:

    for p in range(1, 5):
        print(codigo)
        print(f"Codigo: {codigo_parcial}")
        intento = input("Letra del codigo: ")
        if intento == codigo[len(codigo_parcial)]:
            codigo_parcial += intento                                  
        print(f"Progreso: {p*25}%")
    print(f"Codigo: {codigo_parcial}")

    break