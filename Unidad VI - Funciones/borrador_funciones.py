while True:
    aUser = input("Ingrese primer numero: ")
    bUser = input("Ingrese segundo numero: ")
    cUser = input("Ingrese tercer numero: ")
    if aUser.strip().lstrip("+-").isdigit() and bUser.strip().lstrip("+-").isdigit() and cUser.strip().lstrip("+-").isdigit():
        aUser = int(aUser.strip().lstrip("+-"))
        bUser = int(bUser.strip().lstrip("+-"))
        cUser = int(cUser.strip().lstrip("+-"))
        break