U = input("Ingresar descripcion del universo: ")
uNum = int(input("Ingresar numero de elementos de ese universo: "))

A = input('Ingresar descripcion de primer conjunto "A": ')
B = input('Ingresar descripcion de segundo conjunto "B": ')
C = input('Ingresar descripcion de tercer conjunto "C": ')

aNum = int(input('Ingresar NUMERO de elementos del primer conjunto "A": '))
bNum = int(input('Ingresar NUMERO de elementos del primer conjunto "B": '))
cNum = int(input('Ingresar NUMERO de elementos del primer conjunto "C": '))

anb = int(input('Ingrese NUMERO de elementos en |A ∩ B|: '))
anc = int(input('Ingrese NUMERO de elementos en |A ∩ C|: '))
bnc = int(input('Ingrese NUMERO de elementos en |B ∩ C|: '))

anbnc = int(input('Ingrese NUMERO de elementos en |A ∩ B ∩ C|: '))

soloAnB = anb - anbnc
soloAnC = anc - anbnc
soloBnC = bnc - anbnc
soloA = aNum - soloAnB - soloAnC - anbnc
soloB = bNum - soloAnB - soloBnC - anbnc
soloC = cNum - soloAnC - soloBnC - anbnc

soloTotal = soloAnB + soloAnC + soloBnC + soloA + soloB + soloC
nungunoTotal = uNum - soloTotal