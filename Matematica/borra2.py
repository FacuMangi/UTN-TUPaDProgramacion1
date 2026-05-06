complementoUno = [1,1,1]
# Recorro el complementoUno desde la derecha a la izquierda
for i in range(len(complementoUno)-1, -1, -1):
    # Cuando se le suma 1 al bit del complemento 1, se le resta 1 al carry
    if complementoUno[i] == 1:
        complementoUno[i] = 0
        if i == 0:
            complementoUno.insert(0, 1)
        continue
    if complementoUno[i] == 0:
        complementoUno[i] = 1
        break
    
print(complementoUno)

# El loop recorre de derecha a izquierda cambiando todos los 1 por 0. Cuando se encuentra un 0, cambia este a 1 y se corta el loop. Esto es porque se usa el carry y a partir de ahi es lo mismo que ir sumando cero. O sea, no cambia el numero.