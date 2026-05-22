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

        # # Ejercicio 5
        # case "5":
            

        # # Ejercicio 6
        # case "6":
            

        # # Ejercicio 7
        # case "7":
            

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