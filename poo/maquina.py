import refrigerante

class MaquinaDeRefrigerante:
    #construtor
    def __init__(self, cedulas=None):
        #membros
        self.__cedulas = {20:0, 10:0, 5:0, 2:0}
        self.__refrigerantes = []
        self.__quantidade = 0;

    def get_cedulas(self):
        return self.__cedulas

    def set_cedulas(self, nome):
        self.__cedulas = nome

    cedulas = property(get_cedulas, set_cedulas)

    def inserir_lata(self, Refrigerante, quantidade):

        # self.__refrigerantes = refrigerante.append(Refrigerante);
        self.__quantidade = quantidade;

    def buscar_lata(self):
        for lata in refrigerantes
            print(lata.nome)
#
#     def listar_lata(self):
#         pass
#
#     def alterar_lata(self):
#         pass
#
#    def inserir_cedulas(self):
#        pass
#
#     def listar_cedulas(self):
#         pass
#
#     def calcular_troco(self):
#         pass
#
#     def vender(self):
#         pass

maquina = MaquinaDeRefrigerante()
print(maquina.cedulas)
maquina.inserir_lata(refri, 10)
maquina.buscar_lata
