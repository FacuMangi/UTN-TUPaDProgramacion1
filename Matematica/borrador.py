# print(235/2)
# print(234//2)
# print(1//2)
# print(1%2)

# print(bin(235))

# cocienteNegativo = abs(-235)
# print(cocienteNegativo)

cociente = -72

base = 2

numero = []

while True:
    #print(f"cociente: {abs(cociente)}")
    #print(f"Resto: {abs(cociente) % base}")
    # Agrego el resto al numero
    numero.append(abs(cociente) % base)
    # Redefino cociente como la division entera 
    cociente = abs(cociente) // base
    
    # Cuando el cociente llegue a 1 agrego un 1 extra, que es lo que se hace al final del proceso.
    if cociente == 1:
        numero.append(1)
        break

# Loop while que agrega ceros al array hasta que la cantidad de bits sea multiplo de 8
if len(numero) % 8 != 0:
    while len(numero) % 8 != 0:
        numero.append(0)
        # Si la cantidad de bits en el array es multiplo de 8 Break
        if len(numero) % 8 == 0:
            break

print(f"Numero en base 2: {numero[::-1]}")

nBinario = numero[::-1]

for i in range(len(nBinario)):
    if nBinario[i] == 0:
        nBinario[i] = 1
    elif nBinario[i] == 1:
        nBinario[i] = 0

complementoUno = nBinario
print(f"Complemento 1: {complementoUno}")

# Recorro el complementoUno desde la derecha a la izquierda
for i in range(len(complementoUno)-1, -1, -1):
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
