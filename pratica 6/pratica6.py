class Relogio:
    def __init__(self, hora, minuto, segundo):
        self.__hora = hora
        self.__minuto = minuto
        self.__segundo = segundo

    @property
    def hora(self):
        return self.__hora

    @hora.setter
    def hora(self, hora):
        self.__hora = hora

    @property
    def minuto(self):
        return self.__minuto

    @minuto.setter
    def minuto(self, minuto):
        self.__minuto = minuto

    @property
    def segundo(self):
        return self.__segundo

    @segundo.setter
    def segundo(self, segundo):
        self.__segundo = segundo


    def configura_relogio(self):
        pass

    def tic(self):
        pass

    def __repr__(self):
        r = f'{self.__hora}h:{self.__hora}mim:{self.__hora}seg'
        return r

class Calendario:
    pass