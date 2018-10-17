class Motor:
    def liga(self):
        print('Motor ligado')

    def desliga(self):
        print('Motor desligado')

class Luz:
    def liga(self):
        print('Luz ligada')

    def desliga(self):
        print('Luz desligada')

class Carro:
    def __init__(self, motor):
        self.motor = motor

    def liga(self):
        self.motor.liga()

    def desliga(self):
        self.motor.desliga()

if __name__ == "__main__":
    m = Motor()
    l = Luz()
    c1 = Carro(m) # carro tem motor
    c1.liga() # ok
    c1.desliga() # ok
    c2 = Carro(l) # carro tem luz como motor
    c2.liga() # em Python, isto e aceitavel
    c2.desliga()