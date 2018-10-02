a = ""
datos = set()
while a != "salir":
    a = input("Escriba su dato: ")
    datos.add(a)

print(datos)

def inverso(b):
    try:
        return 1 / b
    except AssertionError:
        print("No paso nada")
    except ZeroDivisionError:
        print("Dividio por cero")



