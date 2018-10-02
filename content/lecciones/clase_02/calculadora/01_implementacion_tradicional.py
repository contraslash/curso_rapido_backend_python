class Calculadora(object):
    operador1 = 0
    operador2 = 0

    def sumar(self):
        return self.operador1 + self.operador2


    def restar(self):
        return self.operador1 - self.operador2


    def multiplicar(self):
        return self.operador1 * self.operador2


    def dividir(self):
        return self.operador1 / self.operador2


calculadora = Calculadora()
calculadora.operador1 = 1
calculadora.operador2 = 2
print(calculadora.sumar())
print(calculadora.restar())
print(calculadora.multiplicar())
print(calculadora.dividir())