while True:
    ejercicio = input(f"Elija un ejercicio del 1 al 5 (0 para cortar): ")
    match ejercicio:
        # Ejercicio 1
        case "1":
            nombreCliente = input("Ingrese nombre del cliente: ").strip()
            
            while not nombreCliente.isalpha():
                print("Nombre invalido, solo letras sin numeros.")
                nombreCliente = input("Ingrese nombre cliente: ").strip()
            
            numeroProductos = input("Cuantos productos va a comprar? ").strip()

            while not (numeroProductos.isdigit() and int(numeroProductos) > 0):
                print("Numero invalido. Ingrese un valor numerico mayor a cero.")
                numeroProductos = input("Cuantos productos va a comprar? ").strip()
            
            numeroProductos =int(numeroProductos)

            totalProductos = 0
            totalDescuentos = 0
            
            detalle = ""

            for p in range(1, numeroProductos + 1):
                precio = input("Introduzca el precio: ").strip()
                while not (precio.isdigit() and int(precio) > 0):
                    print("Introduzca un precio valido.")
                    precio = input("Introduzca el precio: ").strip()
                precio = int(precio)
                totalProductos += precio

                descuento = input("Tiene descuento? S/N: ").strip().upper()
                while descuento not in ("S", "N"):
                    descuento = input("Tiene descuento? Solo S(si) o N (no):").strip().upper()
                
                if descuento == "S":
                    totalDescuentos += precio/10
                
                detalle += f"Producto {p} - Precio: {precio} Descuento (S/N): {descuento.lower()}\n"
                
            promedio = totalProductos/numeroProductos

            print(f"Cliente: {nombreCliente}\n"
                  f"Cantidad de productos: {numeroProductos}")
            
            print(detalle, end="")

            print(
                  f"Total sin descuentos: ${totalProductos}\n"
                  f"Total con descuentos: ${totalProductos - totalDescuentos}\n"
                  f"Ahorro: ${totalDescuentos}\n"
                  f"Promedio por producto: ${promedio:.2f}"
                  )            
        # Ejercicio 2
        case "2":
            usuarioCorrecto  = "alumno"
            claveCorrecta = "python123"
            logeado = False

            for i in range(1, 4):
                user = input("Ingrese su nombre de usuario: ").strip()
                password = input("Ingrese su contraseña: ").strip()

                if user == usuarioCorrecto and password == claveCorrecta:
                    logeado = True
                    print("Acceso concedido.")
                    break

                print(f"Intento {i}/3 - Usuario: {user}\n"
                      f"Clave: xxx\n"
                      f"Error: credenciales invalidas.")

            if not logeado:
                print("Cuenta bloqueada")

            while logeado:
                validos = {"1","2","3","4"}
                print("1) Estado    2) Cambiar clave    3) Mensaje    4) Salir")
                while True:
                    opcion = input("Opcion: ").strip()
                    if opcion.lstrip("+-").isdigit():
                        if opcion in validos:
                            break
                        print("Error: opcion fuera de rango")
                    else:
                        print("Error: ingrese un numero valido.")

                match opcion:
                    case "1":
                        print("Inscripto.")
                    case "2":
                        while True:
                            nuevaPass = input("Nueva clave: ")
                            confirm = input("Confirmar nueva clave: ")
                            if nuevaPass != confirm:
                                print("Error: las contraseñas no coinciden.")
                            elif len(nuevaPass) < 6:
                                print("Error: minimo 6 caracteres.")
                            else:
                                print("Clave actualizada.")
                                break
                    case "3":
                        print("Ganbatte! estudiante-kun")
                    case "4":
                        print("Fin de ejecucion.")
                        break
        # Ejercicio 3
        case "3":
            print("Ingrese nombre del operador.")
            while True:
                op = input("Nombre:").strip().lower()
                if op.isalpha():
                    break
                else:
                    print("Error: Ingrese solo letras")

            turnosLunes = 4
            turnosMartes = 3
            info1 = "Dia Lunes - "
            info2 = "Dia Martes - "
            
            while True:
                validos = {"1","2","3","4","5"}
                print("\n"f"1) Reservar turno\n"
                      f"2) Cancelar turno (por nombre)\n"
                      f"3) Ver agenda del dia\n"
                      f"4) Ver resumenn general\n"
                      f"5) Cerrar sistema\n")        
                while True:
                    opcion = input("Opcion: ").strip()
                    if opcion.lstrip("+-").isdigit():
                        if opcion in validos:
                            break
                        print("Error: opcion fuera de rango")
                    else:
                        print("Error: ingrese un numero valido.")
                    
                match opcion:
                    case "1":
                        # Activa flag para Loop 1
                        active = True
                        # Loop 1
                        while active:
                            print("Elegir dia: 1 = Lunes, 2 = Martes")
                            # Loop 2
                            while True:
                                dia = input("Dia: ").strip()
                                # Validacion que sea digito
                                if dia.lstrip("+-").isdigit():
                                    if dia == "1":
                                        # Validacion nombre
                                        while True:
                                            paciente = input("Ingrese nombre del paciente: ").strip()
                                            if all(part.isalpha() for part in paciente.split()):
                                                break
                                            else:
                                                print("Error: Ingrese solo letras")
                                        # Validacion turno repetido
                                        if paciente in info1:
                                            print("El paciente ya tiene turno para ese dia.")
                                        elif turnosLunes == 0:
                                            print("No quedan turnos para ese dia.")
                                        else:
                                            info1 += f"{paciente} - "
                                            turnosLunes -= 1
                                            print(f"{info1}\nQuedan {turnosLunes} turnos para el Lunes.")
                                            # Desactiva flag para Loop 1, cuando salga del loop 2 active sera False y Loop 1 no volvera a ejecutarse
                                            active = False
                                            # Sale del Loop 2
                                            break
                                    elif dia == "2":
                                        # Validacion nombre
                                        while True:
                                            paciente = input("Ingrese nombre del paciente: ").strip()
                                            if all(part.isalpha() for part in paciente.split()):
                                                break
                                            else:
                                                print("Error: Ingrese solo letras")
                                        # Validacion turno repetido
                                        if paciente in info2:
                                            print("El paciente ya tiene turno para ese dia.")
                                        elif turnosMartes == 0:
                                            print("No quedan turnos para ese dia.")
                                        else:
                                            info2 += f"{paciente} - "
                                            turnosMartes -= 1
                                            print(f"{info2}\nQuedan {turnosMartes} turnos para el Martes.")
                                            # Desactiva flag para Loop 1, cuando salga del loop 2 active sera False y Loop 1 no volvera a ejecutarse
                                            active = False
                                            # Sale del Loop 2
                                            break
                                    else:
                                        print("Ingrese un dia valido.\n")
                                        # Vuelve a iniciar Loop 2
                                else:
                                    print("Error: ingrese un digito\n")
                                    # Vuelve a iniciar Loop 1
                    case "2":
                        # Activa flag para Loop 1
                        active = True
                        # Loop 1
                        while active:
                            print("Elegir dia: 1 = Lunes, 2 = Martes")
                            # Loop 2
                            while True:
                                dia = input("Dia: ").strip()
                                # Validacion que sea digito
                                if dia.lstrip("+-").isdigit():
                                    if dia == "1":
                                        print("Lunes\n")
                                        # Validacion nombre
                                        while True:
                                            paciente = input("Ingrese nombre del paciente: ").strip()
                                            if all(part.isalpha() for part in paciente.split()):
                                                break
                                            else:
                                                print("Error: Ingrese solo letras")
                                        if paciente in info1:
                                            turnosLunes += 1
                                            info1 = info1.replace(f"{paciente} - ", "")
                                            print(f"Turno para {paciente} cancelado.\nQuedan {turnosLunes} turnos para el Lunes.")
                                        else:
                                            print(f"No se encontro a {paciente} en la lista de turnos para el lunes.")
                                        # Desactiva flag
                                        active = False
                                        break
                                    elif dia == "2":
                                        print("Martes\n")
                                        while True:
                                            paciente = input("Ingrese nombre del paciente: ").strip()
                                            if paciente.isalpha():
                                                break
                                            else:
                                                print("Error: Ingrese solo letras")
                                        if paciente in info2:
                                            turnosMartes += 1
                                            info2 = info2.replace(f"{paciente} - ", "")
                                            print(f"Turno para {paciente} cancelado.\nQuedan {turnosMartes} turnos para el Martes.")
                                        else:
                                            print(f"No se encontro a {paciente} en la lista de turnos para el Martes.")
                                        # Desactiva flag
                                        active = False
                                        break
                                    else:
                                        print("Ingrese un dia valido.")
                                else:
                                    print("Ingrese solo digitos.")
                    case "3":
                        print(f"---Turnos Lunes---")
                        for i in range(1, 5):
                            if i <= 4 - turnosLunes:
                                print(f"Turno {i} (ocupado).")
                            else:
                                print(f"Turno {i} (libre).")
                        print(f"---Turnos Martes---")
                        for i in range(1, 4):
                            if i <= 3 - turnosMartes:
                                print(f"Turno {i} (ocupado).")
                            else:
                                print(f"Turno {i} (libre).")
                    case "4":
                        ocupadosLun = 4 - turnosLunes
                        ocupadosMar = 3 - turnosMartes
                        print(f"---Lunes---\n"
                              f"Disponibles: {turnosLunes}\n" 
                              f"Ocupados: {ocupadosLun}\n"
                              f"---Martes---\n"
                              f"Disponibles: {turnosMartes}\n"
                              f"Ocupados: {ocupadosMar}")
                        if ocupadosLun > ocupadosMar:
                            print("Dia con mas turnos ocupados: Lunes")
                        elif ocupadosLun < ocupadosMar:
                            print("Dia con mas turnos ocupados: Martes")
                        elif ocupadosLun == ocupadosMar:
                            print("Ambos dias tienen la misma cantidad de turnos ocupados.")
                    case "5":
                        print("Fin de ejecucion.")
                        break            
        # Ejercicio 4
        case "4":
            # El programa arranca con el nombre del agente.
            while True:
                agente = input("Nombre del agente: ").strip()
                if agente.isalpha():
                    corriendo = True
                    break
                else:
                    print("Error: Ingrese solo letras")
            #Seteando variables
            energia = 100
            tiempo = 12
            cerraduras_abiertas = 0
            cerradura_bloqueada = False
            alarma = False
            codigo_parcial = ""
            codigo = "passwordextralarge"
            intentosCerradura = 0
            intentosHack = 0

            while corriendo:
                # Mientras corriendo sea True el juego se desarrolla, modificando los valores de las variables
                estado = f"\n---ESTADO---\n*Energia de {agente}: {energia}*   *Tiempo restante: {tiempo}*   *Cerradurasa restantes: {3 - cerraduras_abiertas}*"
                if alarma == True:
                    estado += "  *¡Alarma encendida!*"
                print(estado)
                
                if energia <= 0 or tiempo <= 0:
                    print(">> Perdiste. \n---Fin del juego---")
                    break
                elif (alarma == True and tiempo <= 3) or cerradura_bloqueada == True:
                    print(">> Se bloqueo la cerradura. \n---Fin del juego---")
                    break
                elif cerraduras_abiertas == 3:
                    print(">> Has abierto las 3 cerraduras.\nGanaste.")
                    break

                print("\n-1- Forzar cerradura --- (-20 energia, -2 tiempo)\n"
                    "-2- Hackear panel --- (-10 energia, -3 tiempo)\n"
                    "-3- Descansar --- (+15 energia (max 100), -1 tiempo; con alarma: -10 a energia extra)")
                
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
                        numeros1 = {"1", "2", "3"}
                        energia -= 20
                        tiempo -= 2
                        intentosCerradura += 1

                        if intentosCerradura == 3:
                            print(">> Se trabo la cerradura"
                                "\n>> Ha sonado la alarma!")
                            alarma = True
                            break

                        if energia < 40 and alarma == False:
                            print("\n>> Estas cansado y hay riesgo de activar la alarma.")
                            print(">> Elija un numero: 1, 2 o 3 ")
                            while True:
                                numero = input("Numero: ").strip()
                                if numero.lstrip("+-").isdigit():
                                    if numero in numeros1:
                                        if numero == "3":
                                            print(">> Ha sonado la alarma!")
                                            alarma = True
                                        else:
                                            print(">> Todo tranquilo...")
                                            cerraduras_abiertas += 1
                                        break
                                    print("Error: Debe ser un nunmero entre 1 y 3.")
                                else:
                                    print("Error: Debe ser un numero.")
                        else:
                            cerraduras_abiertas += 1

                    case "2":
                        intentosHack += 1
                        intentosCerradura = 0
                        energia -= 20
                        tiempo -= 2

                        if intentosHack == 4:
                            print(">> ¡El panel ha explotado!")
                        elif intentosHack >=4:
                            print(">> El panel ha explotado... hackear ya no es una opcion.")
                        else:
                            if len(codigo_parcial) != len(codigo):
                                for p in range(1, 5):
                                    print(f">> Codigo: {codigo_parcial}")
                                    while True:
                                        intento = input("Letra del codigo: ").strip().lower()
                                        if intento.isalpha():
                                            break
                                        else:
                                            print("Error: solo se aceptan letras.")
                                    if intento == codigo[len(codigo_parcial)]:
                                        codigo_parcial += intento                                  
                                    print(f">> Progreso: {p*25}%")
                                print(f">> Codigo: {codigo_parcial}")

                                if len(codigo_parcial) >= 8:
                                    cerraduras_abiertas += 1 

                    case "3":
                        intentosCerradura = 0
                        tiempo -= 1
                        if alarma == False:
                            if energia >= 85:
                                energia = 100
                            else:
                                energia += 15
                            print(">> Te tomas un descanso...\n" \
                            ">> Energia +15\n" \
                            ">> Tiempo -1")
                        else:
                            if energia >= 95:
                                energia = 100
                            else:
                                energia += 5
                            print(">> Te tomas un descanso...\n" \
                            ">> Energia +5\n" \
                            ">> Tiempo -1")
        # Ejercicio 5
        case "5":
            # El programa arranca con el nombre. Validado
            while True:
                print("--- BIENVENIDO A LA ARENA ---")
                nombre = input("¡Di tu nombre GLADIADOR!: ").strip()
                if nombre.isalpha():
                    print(f"¡Bienvenido a la arena! {nombre}")
                    corriendo = True
                    break
                else:
                    print("¡Ese no es un nombre de GLADIADOR!")

            #Seteando variables
            vidaJugador = 100
            vidaEnemigo = 100
            pociones = 3
            ataqueP = 15
            dañoEnemigo = 12
            turnoJugador = True
            critico = ataqueP * 1.5
            titulo = 0

            while corriendo:
                # Mientras corriendo sea True el juego se desarrolla, modificando los valores de las variables
                if titulo == 0:
                    titulo = 1
                    estado = f"\n=== INICIO DEL COMBATE ===\n{nombre} (HP: {vidaJugador}) VS Enemigo: (HP: {vidaEnemigo}) | Pociones restantes: {pociones}"
                else:
                    estado = f"\n=== NUEVO TURNO ===\n{nombre} (HP: {vidaJugador}) VS Enemigo: (HP: {vidaEnemigo}) | Pociones restantes: {pociones}"  
                print(estado)

                if vidaJugador <= 0:
                    print("DERROTA.\nHas caido en combate.")
                    break
                elif vidaEnemigo <= 0:
                    print(f"¡VICTORIA! \n{nombre} ha ganado la batalla!")
                    break

                while turnoJugador:
                    print("Elige acción:\n"
                        "-1- Ataque Pesado \n"
                        "-2- Ráfaga Veloz\n"
                        "-3- Curar")
                    
                    menu = {"1", "2", "3"}
                    while True:
                        accion = input("Accion: ").strip()
                        if accion.lstrip("+-").isdigit():
                            if accion in menu:
                                break
                            print("Error: accion fuera de rango")
                        else:
                            print("Error: ingrese un número válido.")
                    
                    match accion:
                        case "1":
                            if vidaEnemigo <= 20:
                                print(">> Eso fue CRITICO!") 
                                vidaEnemigo -= critico
                                print(f">> ¡Aatacaste al enemigo por {critico} puntos de daño!")
                            else:
                                vidaEnemigo -= ataqueP
                                print(f">> ¡Aatacaste al enemigo por {ataqueP} puntos de daño!")                
                            turnoJugador = False

                        case "2":
                            for r in range(1, 4):
                                vidaEnemigo -= 5
                                print(">Golpe conectado por 5 de daño!")
                            turnoJugador = False

                        case "3":
                            if vidaJugador == 100:
                                print(">> ¡Estas full vida!")
                            if pociones > 0:
                                pociones -= 1
                                if vidaJugador >= 70:
                                    vidaJugador = 100
                                else:
                                    vidaJugador += 30
                            else:
                                print(">> ¡No te quedan pociones!")
                            turnoJugador = False
                
                while not turnoJugador:
                        vidaJugador -= dañoEnemigo
                        print(f">> ¡El enemigo ataca por {dañoEnemigo} puntos de daño!")
                        turnoJugador = True    
        case "0":
            print("Terminando programa...")
            break
        case _:
            print("Opcion no valida")
