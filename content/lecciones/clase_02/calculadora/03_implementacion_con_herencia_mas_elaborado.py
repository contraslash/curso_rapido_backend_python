class Operador(object):
    operador1 = 0
    operador2 = 0


class Suma(Operador):
    sumar = lambda x, y: x+y


class Resta(Operador):
    restar  = lambda x, y: x -y


class Multiplicar(Operador):
    multiplicar = lambda x, y: x *y


class Dividir(Operador):
    dividir = lambda x, y: x / y


class Calculadora(Suma, Resta, Multiplicar, Dividir):
    pass



calculadora = Calculadora()
print(calculadora.sumar(1,2))
print(calculadora.restar(1,2))
print(calculadora.multiplicar(1,2))
print(calculadora.dividir())