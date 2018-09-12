print('\nclasse Refrigerante')
class Refrigerante:
    #construtor
    def __init__(self, nome='', preco=0):
        #membros
        self.__nome = nome
        self.__preco = preco
        self.__quantidade = 0

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_preco(self):
        return self.__preco

    def set_preco(self, preco):
        self.__preco = preco

    def get_quantidade(self):
        return self.__quantidade

    def set_quantidade(self, quantidade):
        self.__quantidade = quantidade

    nome = property(get_nome, set_nome)
    preco = property(get_preco, set_preco)
    quantidade = property(get_quantidade, set_quantidade)



refri = Refrigerante('Corote', 100)
print(refri.nome);
print(refri.preco)

print('\nclasse MaquinaDeRefrigerante')
# class MaquinaDeRefrigerante:
#     #construtor
#     def __init__(self, cedulas=None):
#         #membros
#         self.__cedulas = {20:0, 10:0, 5:0, 2:0}
#         self.__refrigerantes = []
#         self.__quantidade = 0;
#
#     def get_cedulas(self):
#         return self.__cedulas
#
#     def set_cedulas(self, nome):
#         self.__cedulas = nome
#
#     cedulas = property(get_cedulas, set_cedulas)
#
#     def inserir_lata(self, Refrigerante, quantidade):
#
#         # self.__refrigerantes = refrigerante.append(Refrigerante);
#         self.__quantidade = quantidade;
#
#     def buscar_lata(self):
#         for lata in refrigerantes
#             print(lata.nome)
# #
# #     def listar_lata(self):
# #         pass
# #
# #     def alterar_lata(self):
# #         pass
# #
# #    def inserir_cedulas(self):
# #        pass
# #
# #     def listar_cedulas(self):
# #         pass
# #
# #     def calcular_troco(self):
# #         pass
# #
# #     def vender(self):
# #         pass
#
# maquina = MaquinaDeRefrigerante()
# print(maquina.cedulas)
# maquina.inserir_lata(refri, 10)
# maquina.buscar_lata
