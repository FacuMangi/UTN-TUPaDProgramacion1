while True:
    ejercicio = input(f"Elija un ejercicio del 1 al 10 (0 para cortar): ")
    match ejercicio:
        case "1":
        # Ejercicio 1
            edad = int(input("Ingrese su edad: "))
            if edad >= 18:
                print("Es mayor de edad")

        # Ejercicio 2
        case "2":
            nota = int(input("Ingrese su nota: "))
            if nota >= 6:
                print("Aprobado")
            else:
                print("Desaprobado")

        # Ejercicio 3
        case "3":
            numero = int(input("Ingrese su numero: "))
            if numero % 2 == 0:
                print("Ha ingresado un numero par.")
            else:
                print("Por favor ingrese un numero par.")

        # Ejercicio 4
        case "4":
            edad = int(input("Ingrese su edad: "))
            if edad < 12:
                print("Niño")
            elif 12 <= edad < 18:
                print("Adolescente")
            elif 18 <= edad < 30:
                print("Adulto joven")
            elif edad >= 30:
                print("Adulto")

        # Ejercicio 5
        case "5":
            contraseña = input("Ingrese su contraseña entre 8 y 14 caracteres: ")
            if 8 <= len(contraseña) <= 14:
                print("Ha ingresado una contraseña correcta")
            else:
                print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres.")

        # Ejercicio 6
        case "6":
            

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
