while True:    
    try:
        entrada = input("Ingrese un numero: ").strip()
        # Valor para cortar la ejecucion del loop
        if entrada.lower() == "break":
            break

        numero = float(entrada)
        print(f"El numbero ingresado es: {numero}")
        break

    except ValueError:
        # Se triggerea cuando el usuario no introduce un numero
        print("Debe ingresar un valor valido.")

    except Exception as e:
        # Captura fallos generales
        print(f"Se produjo un error inesperado: {e}")