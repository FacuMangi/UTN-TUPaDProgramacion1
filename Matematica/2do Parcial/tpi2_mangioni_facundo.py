def inputNoVacio(mensaje):
	# Pide una cadena no vacía al usuario; vuelve a solicitar hasta
	# que reciba una entrada con algún carácter distinto de espacio.
	while True:
		v = input(mensaje).strip()
		if v:
			return v
		print("Entrada vacía. Intente de nuevo.")


def inputInt(mensaje, minimum=None, maximum=None):
	# Pide un entero al usuario con reintentos y validación opcional
	# de rango (minimum y maximum). Maneja ValueError internamente.
	while True:
		try:
			v = int(input(mensaje))
		except ValueError:
			print("Entrada inválida. Ingrese un número entero.")
			continue
		if minimum is not None and v < minimum:
			print(f"El número debe ser >= {minimum}.")
			continue
		if maximum is not None and v > maximum:
			print(f"El número debe ser <= {maximum}.")
			continue
		return v


def main():
	print("=== Cálculo de conjuntos ===")
	U = inputNoVacio("Ingresar descripción del universo: ")
	uNum = inputInt("Ingresar número total de elementos del universo: ", minimum=0)

	A = inputNoVacio('Ingresar descripción del primer conjunto "A": ')
	B = inputNoVacio('Ingresar descripción del segundo conjunto "B": ')
	C = inputNoVacio('Ingresar descripción del tercer conjunto "C": ')
	
	# Para inputInt minimo sera 0 y maximo el numero de elementos en el UNIVERSO.
	aNum = inputInt(f'Ingresar número de elementos del conjunto "{A}": ', minimum=0, maximum=uNum)
	bNum = inputInt(f'Ingresar número de elementos del conjunto "{B}": ', minimum=0, maximum=uNum)
	cNum = inputInt(f'Ingresar número de elementos del conjunto "{C}": ', minimum=0, maximum=uNum)

	anbnc = inputInt('Ingrese número de elementos en |A ∩ B ∩ C|: ', minimum=0, maximum=min(aNum, bNum, cNum))

    # Para inputInt, el minimo tiene que ser AnBnC, y el maximo debe ser el mayor entre los numeros en la interseccion.
	# Eto asegura que no te salgas de los limites de la triple interseccion y el maximo valor ingresado para la interseccion doble.
	anb = inputInt('Ingrese número de elementos en |A ∩ B|: ', minimum=anbnc, maximum=min(aNum, bNum))
	anc = inputInt('Ingrese número de elementos en |A ∩ C|: ', minimum=anbnc, maximum=min(aNum, cNum))
	bnc = inputInt('Ingrese número de elementos en |B ∩ C|: ', minimum=anbnc, maximum=min(bNum, cNum))


	# Calcular las regiones del diagrama de Venn de tres conjuntos:
	# - soloAnB: elementos en A∩B pero no en C
	# - soloAnC: elementos en A∩C pero no en B
	# - soloBnC: elementos en B∩C pero no en A
	# - soloA/soloB/soloC: elementos exclusivos de cada conjunto
	soloAnB = anb - anbnc
	soloAnC = anc - anbnc
	soloBnC = bnc - anbnc
	soloA = aNum - soloAnB - soloAnC - anbnc
	soloB = bNum - soloAnB - soloBnC - anbnc
	soloC = cNum - soloAnC - soloBnC - anbnc

    # Mas validaciones.
	if any(x < 0 for x in (soloA, soloB, soloC)):
		print("Datos inconsistentes: algunos recuentos resultaron negativos. Revise las entradas.")
		return

	# Sumar todas las regiones (incluida la intersección triple) para
	# calcular cuántos elementos quedan fuera de todos los conjuntos.
	union = soloAnB + soloAnC + soloBnC + soloA + soloB + soloC + anbnc
	ningunoTotal = uNum - union

	print("\nResultados:")
	print(f"Universo '{U}': {uNum} elementos")
	print(f"{A}: {aNum}  |  {B}: {bNum}  |  {C}: {cNum}")
	print(f"Solo A: {soloA}")
	print(f"Solo B: {soloB}")
	print(f"Solo C: {soloC}")
	print(f"Solo A∩B (sin C): {soloAnB}")
	print(f"Solo A∩C (sin B): {soloAnC}")
	print(f"Solo B∩C (sin A): {soloBnC}")
	print(f"A∩B∩C: {anbnc}")
	if union > uNum:
		print("Advertencia: la suma de los elementos de los conjuntos excede el universo indicado.")
	else:
		print(f"Elementos que no pertenecen a ningún conjunto: {ningunoTotal}")


if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		print("\nInterrupción del usuario. Saliendo.")