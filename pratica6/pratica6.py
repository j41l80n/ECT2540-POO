from abc import ABC, abstractmethod

class Relogio:
    def __init__(self, hora=0, minuto=0, segundo=0):
        self.configura_relogio(hora, minuto,segundo)

    @property
    def hora(self):
        return self._hora

    @hora.setter
    def hora(self, hora):
        if hora < 0 or hora > 23:
            print('hora fora do intervalo')
        else:
            self._hora = hora

    @property
    def minuto(self):
        return self._minuto

    @minuto.setter
    def minuto(self, minuto):
        if minuto < 0 or minuto > 59:
            print('minuto fora do intervalo')
        else:
            self._minuto = minuto

    @property
    def segundo(self):
        return self._segundo

    @segundo.setter
    def segundo(self, segundo):
        if segundo < 0 or segundo > 59:
            print('segundo fora do intervalo')
        else:
            self._segundo = segundo

    def configura_relogio(self, hora, minuto, segundo):
        if hora < 0 or hora > 23:
            print('hora fora do intervalo')
        else:
            self._hora = hora
        
        if minuto < 0 or minuto > 59:
            print('minuto fora do intervalo')
        else:
            self._minuto = minuto
            
        if segundo < 0 or segundo > 59:
            print('segundo fora do intervalo')
        else:
            self._segundo = segundo

    def tic(self):
        self._segundo += 1 
        if self._segundo == 60:
            self._minuto += 1
            self._segundo = 0
        if self._minuto == 60:
            self._hora += 1
            self._minuto = 0
        if self._hora == 24:
            self._hora = 0
            self._minuto = 0
            self._segundo = 0

    def __repr__(self):
        r = f'{self._hora}h:{self._minuto}mim:{self._segundo}seg'
        return r

class Calendario:
    # atributo de classe
    _dias_por_mes = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

    def __init__(self, dia=28, mes=2, ano=2000):
        self.configura_calendario(dia, mes, ano)
    
    def configura_calendario(self, dia, mes, ano):
        if mes > 0 and mes < 13:
            self._mes = mes
            self._ano = ano
            if dia <= self._dias_por_mes[mes-1]:
                self._dia = dia
            else:
                print('dia invalido')
        else:
            print('data nao valida')

    def avanca(self):
        pass
    
    def __repr__(self):
        r = f'{self._dia}/{self._mes}/{self._ano}'
        return r

class RelogioCalendario(Relogio, Calendario):
   pass

if __name__ == "__main__":
    r = Relogio()
    r.configura_relogio(144, 20, 3)
    for i in range(360):   
        r.tic()

    print(r)

    c = Calendario()
    print(c)