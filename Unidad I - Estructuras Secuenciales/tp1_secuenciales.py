while True:
    ejercicio = input(f"Elija un ejercicio del 1 al 10 (0 para cortar): ")
    match ejercicio:
        case "1":
        # Ejercicio 1
            print("Hola Mundo!")

        # Ejercicio 2
        case "2":
            nombre = input("Ingrese su nombre: ")
            print(f"Hola {nombre}!")

        # Ejercicio 3
        case "3":
            nombre = input("Ingrese su nombre: ")
            apellido = input("Ingrese su apellido: ")
            edad = int(input("Ingrese su edad: "))
            residencia = input("Ingrese su lugar de residencia: ")
            print(f"Mi nombre es {nombre}. Tengo {edad} años. Mi casa esta en {residencia}.")

        # Ejercicio 4
        case "4":
            radio = int(input("Ingrese el radio del circulo: "))
            area = 3.14 * radio ** 2
            perimetro = 2 * 3.14 * radio
            print(f"Area: {area} \nPerimetro: {perimetro}")

        # Ejercicio 5
        case "5":
            seg = int(input("Ingrese cantidad de segundos: "))
            horas = seg / 60 ** 2
            print(f"{seg} segundos equivale a {horas} horas!")

        # Ejercicio 6
        case "6":
            numero = int(input("Ingrese un numero: "))
            print(f"1 * {numero} = {1 * numero}"
                  f"\n2 * {numero} = {2 * numero}"
                  f"\n3 * {numero} = {3 * numero}"
                  f"\n4 * {numero} = {4 * numero}"
                  f"\n5 * {numero} = {5 * numero}"
                  f"\n6 * {numero} = {6 * numero}"
                  f"\n7 * {numero} = {7 * numero}"
                  f"\n8 * {numero} = {8 * numero}"
                  f"\n9 * {numero} = {9 * numero}"
                  f"\n10 * {numero} = {10 * numero}")

        # Ejercicio 7
        case "7":
            while True:
                numero1 = int(input("Ingrese un numero entero distinto de cero: "))
                numero2 = int(input("Ingrese otro numero entero distinto de cero: "))
                if numero1 != 0 and numero2 != 0:
                    break
                else:
                    print("Debe ser distinto de cero.")

            print(f"{numero1} + {numero2} = {numero1 + numero2}"
                  f"\n{numero1} - {numero2} = {numero1 - numero2}"
                  f"\n{numero1} * {numero2} = {numero1 * numero2}"
                  f"\n{numero1} / {numero2} = {numero1 / numero2}"
                  )

        # Ejercicio 8
        case "8":
            altura = float(input("Ingrese su altura en metros: "))
            peso = int(input("Ingrese su peso en Kg: "))
            IMC = peso/altura**2
            print(f"Su IMC es: {IMC}")

        # Ejercicio 9
        case "9":
            cel = float(input("Ingrese temperatura en Celsius: "))
            fahr = 9*cel/5 + 32
            print(f"La temperatura en Fahrenheit es: {fahr}.")

        # Ejercicio 10
        case "10":
            num1 = int(input("Ingrese un numero: "))        
            num2 = int(input("Ingrese un numero: "))        
            num3 = int(input("Ingrese un numero: "))     
            promedio = (num1 + num2 + num3)/3
            print(f"El promedio es: {promedio}")   

        case "0":
            print("Terminando programa...")
            break
        case _:
            print("Opcion no valida")
