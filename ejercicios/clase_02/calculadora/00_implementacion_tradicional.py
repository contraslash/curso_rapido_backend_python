class Calculadora(object):

    def sumar(self, a, b):
        return a + b


    def restar(self, a, b):
        return a - b


    def multiplicar(self, a, b):
        return a * b


    def dividir(self, a, b):
        return a / b


calculadora = Calculadora()
print(calculadora.sumar(1, 2))
print(calculadora.restar(1, 2))
print(calculadora.multiplicar(1, 2))
print(calculadora.dividir(1, 2))