# print(235/2)
# print(234//2)
# print(1//2)
# print(1%2)

# print(bin(235))

# cocienteNegativo = abs(-235)
# print(cocienteNegativo)

cociente = -10

base = 2

#al estar iterando sobre un numero negativo, los 0 pasan a ser 1 y cuando un 1 pasa a ser un 0 es que avanzo en el digito y se debe cortar.

nBase2 = [1,1,1,1,1,0,0,0]

for i in range(len(nBase2)-1, -1, -1):
    if nBase2[i] == 1:
        nBase2[i] = 0
        if i == 0:
            nBase2.insert(0, 1)
        break
    nBase2[i] = 1

print(nBase2)

# Por que se calcula el complemento a 2? porque los numeros negativos estan desfazados de los positivos y cuando queres pasar un positivo y escribirlo como negativo, tenes que compensar ese desfasage sumando 1. Por eso, haces el complemento de invetir los bits (complemento 1) y le restas 0001 (sumas 1111). Eso es porque los negativos son los positivos pero con ceros tomando el lugar de unos.  