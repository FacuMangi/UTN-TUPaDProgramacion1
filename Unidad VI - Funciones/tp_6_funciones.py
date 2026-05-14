while True:
    ejercicio = input(f"Elija un ejercicio del 1 al 10 (0 para cortar): ")
    match ejercicio:
        case "1":
        # Ejercicio 1
            def imprimir_hola_mundo():
                print("Hola Mundo!")

            imprimir_hola_mundo()

        # Ejercicio 2
        case "2":
            def saludar_usuario(nombre):
                print(f"Hola {nombre}!")

            saludar_usuario()
        # Ejercicio 3
        case "3":
            def nformacion_personal(nombre, apellido, edad, residencia):
                print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

            nombreIngresado = input("Ingrese su nombre: ")
            apellidoIngresado = input("Ingrese su apellido: ")
            edadIngresado = input("Ingrese su edad: ")
            residenciaIngresado = input("Ingrese su lugar de residencia: ")

            nformacion_personal(nombreIngresado, apellidoIngresado, edadIngresado, residenciaIngresado)

        # Ejercicio 4
        case "4":
            def calcular_area_circulo(r):
                area=3.14*(r**2)
                print(f"Area: {area}")

            def calcular_perimetro_circulo(r):
                perimetro=2*3.14*r
                print(f"Perimetro: {perimetro}")
            while True:
                radioUser = input("Ingrese radio: ")
                if radioUser.strip().lstrip("+-").isdigit():
                    radioUser = int(radioUser.strip().lstrip("+-"))
                    break

            calcular_area_circulo(radioUser)
            calcular_perimetro_circulo(radioUser)

        # Ejercicio 5
        case "5":
            def segundos_a_horas(segundo):
                horas = segundo/(60**2)
                print(f"Segundos a horas: {"{0:.2f}".format(horas)}")
            while True:
                segUser = input("Ingrese segundos: ")
                if segUser.strip().lstrip("+-").isdigit():
                    segUser = int(segUser.strip().lstrip("+-"))
                    break

            segundos_a_horas(segUser)

        # Ejercicio 6
        case "6":
            def tabla_multiplicar(numero):
                tabla = ""
                for i in range(1, 10 + 1):
                    tabla += "7 * " + str(i) + " = " + str(numero*i) + "\n "
                return(tabla)
            
            while True:
                numUser = input("Ingrese numero: ")
                if numUser.strip().lstrip("+-").isdigit():
                    numUser = int(numUser.strip().lstrip("+-"))
                    break
            print(f"La tabla del {numUser} es: \n {tabla_multiplicar(numUser)}")

        # Ejercicio 7
        case "7":
            def operaciones_basicas(a, b):
                suma = a + b
                resta = a - b
                prod = a * b
                div = a / b
                
                return(suma, resta, prod, div)
            
            resultados = operaciones_basicas(10, 2)
            print(resultados)

        # Ejercicio 8
        case "8":
            def calcular_imc(peso, altura):
                imc = peso/(altura**2)
                return(imc)
            
            while True:
                kgUser = input("Ingrese peso en Kg: ")
                if kgUser.strip().lstrip("+-").isdigit():
                    kgUser = int(kgUser.strip().lstrip("+-"))
                    break
            
            while True:
                alUser = input("Ingrese altura en M: ")
                if alUser.strip().lstrip("+-").replace(".", "", 1).isdigit():
                    alUser = float(alUser.strip().lstrip("+-"))
                    break

            print(f"IMC: {"{0:.2f}".format(calcular_imc(kgUser, alUser))}")

        # Ejercicio 9
        case "9":
            def celsius_a_fahrenheit(celsius):
                fahrenheit = (celsius * 9 / 5) + 32
                return fahrenheit

            while True:
                celUser = input("Ingrese temperatura en Celsius: ")
                if celUser.strip().lstrip("+-").replace(".", "", 1).isdigit():
                    celUser = float(celUser.strip().lstrip("+-"))
                    break

            print(f"La temperatura en fahrenheit es: {"{0:.2f}".format(celsius_a_fahrenheit(celUser))}")
        # Ejercicio 10
        case "10":
            def calcular_promedio(a, b, c):
                promedio = (a + b + c) / 3
                return promedio

            while True:
                aUser = input("Ingrese primer numero: ")
                if aUser.strip().lstrip("+-").isdigit():
                    aUser = int(aUser.strip().lstrip("+-"))
                    break
            while True:
                bUser = input("Ingrese primer numero: ")
                if bUser.strip().lstrip("+-").isdigit():
                    bUser = int(bUser.strip().lstrip("+-"))
                    break
            while True:
                cUser = input("Ingrese primer numero: ")
                if cUser.strip().lstrip("+-").isdigit():
                    cUser = int(cUser.strip().lstrip("+-"))
                    break
            
            print(f"El promedio de los numeros es: {calcular_promedio(aUser, bUser, cUser)}")

        case "0":
            print("Terminando programa...")
            break
        case _:
            print("Opcion no valida")
