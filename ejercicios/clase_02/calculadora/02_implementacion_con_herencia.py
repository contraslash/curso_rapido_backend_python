class Operador(object):
    def __init__(self, operador1, operador2):
        self.operador1 = operador1
        self.operador2 = operador2


class Suma(Operador):
    def sumar(self):
        return self.operador1 + self.operador2


class Resta(Operador):
    def restart(self):
        return self.operador1 - self.operador2


class Multiplicar(Operador):
    def multiplicar(self):
        return self.operador1 * self.operador2


class Dividir(Operador):
    def dividir(self):
        return self.operador1 / self.operador2



class Calculadora(Suma, Resta, Multiplicar, Dividir):
    def __init__(self, operador1, operador2):
        super(Calculadora, self).__init__(operador1, operador2)



calculadora = Calculadora(1,2)
print(calculadora.sumar())
print(calculadora.restart())
print(calculadora.multiplicar())
print(calculadora.dividir())