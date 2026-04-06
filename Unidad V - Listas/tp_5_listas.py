import random
while True:
    ejercicio = input(f"Elija un ejercicio del 1 al 13 (0 para cortar): ")
    match ejercicio:
        # Ejercicio 1 ---------------------------------------------------
        case "1":
            alumnos = [7, 4, 8, 5, 6, 6, 9, 7, 7, 10]
            suma = 0
            for i in range(len(alumnos)):
                suma += alumnos[i]
            print(f"Lista: {alumnos}")
            print(f"Nota mas alta: {max(alumnos)}\n"
            f"Nota mas baja: {min(alumnos)}")
            print(f"El promedio de las notas es:{suma/10}")
        # Ejercicio 2 ---------------------------------------------------    
        case "2":
            listaProductos = []
            for i in range(5):
                nombre = input("Ingrese nombre: ").strip().lower()
                listaProductos.append(nombre)
            listaProductos = sorted(listaProductos)
            print(f"Lista: {listaProductos}")
            eliminar = input("Que cosa desea eliminar?").strip().lower()
            if eliminar in listaProductos:
                listaProductos.remove(eliminar)
            print(f"Nueva lista: {listaProductos}")
        # Ejercicio 3 ---------------------------------------------------
        case "3":
            listaRandom = random.sample(range(1, 101), 15)
            pares = []
            impares = []
            for i in range(15):
                if listaRandom[i]%2 == 0:    
                    pares.append(listaRandom[i])
                else:
                    impares.append(listaRandom[i])
            print(f"Pares: {len(pares)}\n"
                  f"Impares: {len(impares)}")
            print(pares)
            print(impares)
        # Ejercicio 4 ---------------------------------------------------
        case "4":
            datos = [1, 3, 5, 7, 1, 9, 5, 3]
            datosUni = []
            for i in range(len(datos)):
                if datos[i] not in datosUni: #usar count()
                    datosUni.append(datos[i])
            print(f"datos:{datos}\ndatosUni: {datosUni}")
        # Ejercicio 5 ---------------------------------------------------
        case "5":
            corriendo = True
            listaAlumnos = ["facundo", "tomas", "candela", "juan", "camila", "estefania", "lorenzo", "monica"]
            while corriendo:
                print(f"Alumnos: {listaAlumnos}")
                print("\n-1- Agregar estudiante\n"
                    "-2- Eliminar estudiante\n"
                    "-3- Salir")
                
                menu = {"1", "2", "3"}
                while True:
                    accion = input("Accion: ").strip()
                    if accion.lstrip("+-").isdigit():
                        if accion in menu:
                            break
                        print("Error: accion fuera de rango")
                    else:
                        print("Error: ingrese un numero valido.")
                
                match accion:
                    case "1":
                        while True:
                            nuevoAlumno = input("Ingrese al nuevo alumno: ").strip().lower()
                            if nuevoAlumno.isalpha():
                                break
                            else:
                                print("Ingrese nombre valido.")
                        listaAlumnos.append(nuevoAlumno)
                    case "2":
                        while True:
                            borrarAlumno = input("Ingrese alumno a eliminar: ").strip().lower()
                            if borrarAlumno.isalpha():
                                break
                            else:
                                print("Ingrese nombre valido.")
                        listaAlumnos.remove(borrarAlumno)
                    case "3":
                        corriendo = False
            print(f"Alumnos: {listaAlumnos}")
        # Ejercicio 6 ---------------------------------------------------
        case "6":
            lista = [1,2,3,4,5,6,7]
            lista = [lista[-1]] + lista[:-1]
            print(lista)
        # Ejercicio 7 ---------------------------------------------------
        case "7":
            matriz = [[18, 14], [20, 15], [24, 22], [26, 23], [25, 22], [27, 24], [20, 18]]
            sumaMax = 0
            sumaMini = 0
            mayorAmp = 0
            dia = 0
            for i in range(len(matriz)):
                sumaMax += matriz[i][0]
                sumaMini += matriz[i][1]
                if matriz[i][0] - matriz[i][1] > mayorAmp:
                    mayorAmp = matriz[i][0] - matriz[i][1]
                    dia = i
            print(f"Promedio maximas = {sumaMax/7:.2f}\nPromedio minimas = {sumaMini/7:.2f}\nCon mayor amplitod el dia {dia}")
        # Ejercicio 8 ---------------------------------------------------
        case "8":
            estudiantes = [[7,6,8],[7,7,6],[9,8,10],[6,5,6],[7,7,8]]
            suma1 = 0
            suma2 = 0
            suma3 = 0
            for e in range(len(estudiantes)):
                suma1 += estudiantes[e][0]
                suma2 += estudiantes[e][1]
                suma3 += estudiantes[e][2]
                sumaN = 0
                for n in range(len(estudiantes[e])):
                    sumaN += estudiantes[e][n]
                print(f"Promedio de estudiantes: {sumaN/len(estudiantes[e]):.2f}")
            print(f"Promedio materia 1: {suma1/len(estudiantes):.2f}")
            print(f"Promedio materia 2: {suma2/len(estudiantes):.2f}")
            print(f"Promedio materia 3: {suma3/len(estudiantes):.2f}")
        # Ejercicio 9 ---------------------------------------------------
        case "9":
            tablero = [["-","-","-"], ["-","-","-"], ["-","-","-"]]
            for fila in range(len(tablero)):
                print(tablero[fila])
            while True:
                turnoX = True            
                while turnoX:
                    print("==== TURNO X ====")
                    posiciones = {0,1,2}
                    while True:
                        posicionFx = input("Ingrese fila: ").strip()
                        if posicionFx.isdigit():
                            posicionFx = int(posicionFx)
                            if posicionFx in posiciones:
                                break
                            else:
                                print("Ingrese posicion valida.")
                        else:
                            print("Ingrese posicion valida.")
                    while True:    
                        posicionCx = input("Ingrese columna: ").strip()
                        if posicionCx.isdigit():
                            posicionCx = int(posicionCx)
                            if posicionCx in posiciones:
                                break
                            else:
                                print("Ingrese posicion valida.")
                        else:
                            print("Ingrese posicion valida.")

                    if tablero[posicionFx][posicionCx] == "-":
                        tablero[posicionFx][posicionCx] = "X"
                        turnoX = False
                    else:
                        print("Posicion invalida.")
                for fila in range(len(tablero)):
                    print(tablero[fila])
                if ["X","X","X"] in tablero:
                    print("Partida finalizada. Gana X.")
                    break
                elif tablero[0][0] == "X" and tablero[1][1] == "X" and tablero[2][2] == "X":
                    print("Partida finalizada. Gana X.")
                    break
                elif tablero[0][2] == "X" and tablero[1][1] == "X" and tablero[2][0] == "X":
                    print("Partida finalizada. Gana X.")
                    break
                while not turnoX:
                    print("==== TURNO O ====")
                    posiciones = {0,1,2}
                    while True:
                        posicionFo = input("Ingrese fila: ").strip()
                        if posicionFo.isdigit():
                                posicionFo = int(posicionFo)
                                if posicionFo in posiciones:
                                    break
                                else:
                                    print("Ingrese posicion valida.")
                        else:
                            print("Ingrese posicion valida.")
                    while True:    
                        posicionCo = input("Ingrese columna: ").strip()
                        if posicionCo.isdigit():
                            posicionCo = int(posicionCo)
                            if posicionCo in posiciones:
                                break
                            else:
                                print("Ingrese posicion valida.")
                        else:
                            print("Ingrese posicion valida.")
                    if tablero[posicionFo][posicionCo] == "-":
                        tablero[posicionFo][posicionCo] = "O"
                        turnoX = False
                    else:
                        print("Posicion invalida")
                    turnoX = True
                for fila in range(len(tablero)):
                    print(tablero[fila])
                if ["O","O","O"] in tablero:
                    print("Partida finalizada. Gana O.")
                    break
                elif tablero[0][0] == "O" and tablero[1][1] == "O" and tablero[2][2] == "O":
                    print("Partida finalizada. Gana O.")
                    break
                elif tablero[0][2] == "O" and tablero[1][1] == "O" and tablero[2][0] == "O":
                    print("Partida finalizada. Gana O.")
                    break
                
        # Ejercicio 10 --------------------------------------------------
        case "10":
            productos = [[40,2,3,4,5,6,7], [5,2,3,4,5,6,7], [3,2,3,4,5,6,7], [4,2,3,4,5,6,7]]
            vendidosMax = 0
            diaMax = 0
            prod = 0
            cont=[0,0,0,0,0,0,0]
            for i in range(len(productos)):
                vendidos = 0
                for j in range(len(productos[i])):
                    vendidos += productos[i][j]
                    cont[j] += productos[i][j]
                if vendidos > vendidosMax:
                    vendidosMax = vendidos
                    prod = i+1
                print(f"Se vendio {vendidos} de producto {i+1}")
            print(f"El producto mas vendido fue el {prod}")
            print(f"El dia que mas se vendio fue el dia {cont.index(max(cont))+1}")
        # Ejercicio 11 --------------------------------------------------
        case "11":
            lista = [
            "Ana Garcia", 
            "Bruno Lopez", 
            "Carla Martinez", 
            "Diego Fernandez", 
            "Elena Rodriguez", 
            "Facundo Gomez", 
            "Gisela Perez", 
            "Hugo Sanchez", 
            "Irene Diaz", 
            "Juan Torres"
            ]
            buscarEstudiante = input("Ingrese nombre de estudiante: ").strip()
            if buscarEstudiante in lista:
                print(f"El estudiante esta en la lista en el lugar {lista.index(buscarEstudiante)}.")
            else:
                print("El estudiante no esta en la lista.")
        # Ejercicio 12 --------------------------------------------------
        case "12":
            lista = []
            while len(lista)<=8:
                while True:
                    nuevoN = input("Ingrese numero: ").strip()
                    if nuevoN.isdigit: 
                        nuevoN = int(nuevoN)
                        lista.append(nuevoN)
                        break
                    else:
                        print("Solo numeros.")
            print(f"Lisa original: {lista}")
            
            lista = sorted(lista)
            print(f"Lista de menor a mayor {lista}")

            lista = sorted(lista, reverse=True)
            print(f"Lista de mayor a menor: {lista}")
        # Ejercicio 13 --------------------------------------------------
        case "13":
            puntajes = [450, 1200, 875, 990, 300, 1500, 640]
            reverse_sorted = sorted(puntajes, reverse=True)
            print(f"Puntaje mas alto: {max(puntajes)}. \nPuntaje mas bajo: {min(puntajes)}.")
            print(f"Ranking: {reverse_sorted}")
            print(f"El puntaje 990 se encuentra en la posicion: {reverse_sorted.index(990)}")
        case "0":
            print("Terminando programa...")
            break
        case _:
            print("Opcion no valida")
