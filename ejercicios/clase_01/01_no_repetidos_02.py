a = ""
datos = list()
while a != "salir":
    a = input("Escriba su dato: ")
    if a not in datos:
        datos.append(a)

print(datos)
