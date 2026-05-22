while True:
    ejercicio = input(f"Elija un ejercicio del 1 al 10 (0 para cortar): ")
    match ejercicio:
        case "1":
        # Ejercicio 1
            precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

            precios_frutas.update({'Naranja': 1200, 'Manzana': 1500, 'Pera': 2300})

            print(precios_frutas)

        # Ejercicio 2
        case "2":
            precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450, 'Naranja': 1200, 'Manzana': 1500, 'Pera': 2300}
            precios_frutas['Banana'] = 1330
            precios_frutas['Manzana'] = 1700
            precios_frutas['Melón'] = 2800
            print(precios_frutas)

        # Ejercicio 3
        case "3":
            precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

            precios_frutas.update({'Naranja': 1200, 'Manzana': 1500, 'Pera': 2300})

            precios_frutas['Banana'] = 1330
            precios_frutas['Manzana'] = 1700
            precios_frutas['Melón'] = 2800

            lista = []
            for k, v in precios_frutas.items():
                lista.append(k)
            print(lista)

        # Ejercicio 4
        case "4":
            contactos = {}
            agregando = True
            while agregando:
                while True:
                    nombre = input("Ingresa tu nombre: ").strip()
                    
                    # Valida que no esté vacío y que solo contenga letras y espacios
                    if nombre and all(caracter.isalpha() or caracter.isspace() for caracter in nombre):
                        break
                    print("Error: El nombre solo debe contener letras y no puede quedar vacío.")
                while True:
                    telefono = input("Ingresa tu número de teléfono: ").strip()
                    
                    if telefono.isdigit():
                            telefono = int(telefono)
                            break
                    print("Error: El teléfono debe contener solo números.")
                    
                contactos[nombre] = telefono
                respuesta = input("¿Deseas agregar otro contacto? (s/n): ").strip().lower()
                if respuesta != 's':
                    agregando = False
            print(contactos)

        # Ejercicio 5
        case "5":
            while True:
                listaPalabras = input("Ingresa la frase: ").split()
                if listaPalabras and all(caracter.isalpha() or caracter.isspace() for caracter in listaPalabras):
                        break
                print("Error: La frase solo debe contener letras y no puede quedar vacío.")
            elSet = set(listaPalabras)
            print(elSet)

            diccionario = {}
            for palabra in listaPalabras:
                diccionario[palabra] = listaPalabras.count(palabra)

            print(diccionario)
        # Ejercicio 6
        case "6":
            listaAlumnos = []
            for i in range(1, 4):
                while True:
                    alumno = input(f"Ingrese el alumno {i}: ").split()
                    if alumno and all(caracter.isalpha() or caracter.isspace() for caracter in alumno):
                            break
                    print("Error: El alumno solo debe contener letras y no puede quedar vacío.")
                    
                listaAlumnos.append(alumno)
            
            diccionarioAlumnos = {}
            for alumno in listaAlumnos:
                tuplaNotas = []
                for i in range(1, 4):
                    tuplaNotas.append(input(f"Ingrese la nota {i} para {alumno}: "))
                diccionarioAlumnos[alumno] = tuple(tuplaNotas)
            print(diccionarioAlumnos)

        # Ejercicio 7
        case "7":
            listaEmpleados = ["Ana", "Luis", "Ana", "Maria", "Luis", "Pedro", "Ana"]
            setEmpleados = set(listaEmpleados)
            for empleado in setEmpleados: print(empleado)
            diccionario = {}
            for empleado in listaEmpleados:
                diccionario[empleado] = listaEmpleados.count(empleado)
            for k, v in diccionario.items():
                print(f"{k} asistio {v} veces.")

        # # Ejercicio 8
        # case "8":
            

        # # Ejercicio 9
        # case "9":
            

        # # Ejercicio 10
        # case "10":
               

        case "0":
            print("Terminando programa...")
            break
        case _:
            print("Opcion no valida")