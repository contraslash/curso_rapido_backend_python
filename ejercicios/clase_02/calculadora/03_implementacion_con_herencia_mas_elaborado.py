class Operador(object):
    x = 0
    y = 0

    operador1 = 0
    operador2 = 0

    def __init__(self, operador1, operador2):
        self.x = operador1
        self.y = operador2

    @property
    def operador1(self):
        return self.x

    @operador1.setter
    def operador1(self, x):
        self.x = x

    @property
    def operador2(self):
        return self.y

    @operador2.setter
    def operador2(self, y):
        self.y = y


class Suma(Operador):
    sumar = lambda s: s.x + s.y


class Resta(Operador):
    restar  = lambda s: s.x - s.y


class Multiplicar(Operador):
    multiplicar = lambda s: s.x * s.y


class Dividir(Operador):
    dividir = lambda s: s.x / s.y


class Calculadora(Suma, Resta, Multiplicar, Dividir):
    pass



calculadora = Calculadora(1,2)
print(calculadora.sumar())
print(calculadora.restar())
calculadora.operador1 = 2
calculadora.operador2 = 2
print(calculadora.multiplicar())
print(calculadora.dividir())