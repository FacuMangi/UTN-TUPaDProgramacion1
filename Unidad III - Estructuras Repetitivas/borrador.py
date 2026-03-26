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
                    print(">> Golpe conectado por 5 de daño!")
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