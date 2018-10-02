a = ""
datos = list()
while a != "salir":
    a = input("Escriba su dato: ")
    existe = False
    for elemento in datos:
        if a == elemento:
            existe = True
    if not existe:
        datos.append(a)

print(datos)