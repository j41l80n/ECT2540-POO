class Pessoa:
    #construtor
    def __init__(self, nome='', idade=0):
        #membros
        self.__nome_completo = nome
        self.__idade = idade

    #retorna o nome da instancia pessoa
    def get_nome(self):
        return self.__nome_completo
    
    #insere o nome da instancia pessoa
    def set_nome(self, nome):
        if type(nome) == str:
            self.__nome_completo = nome
        else:
            print('erro')

    #definindo propriedade
    nome = property(get_nome, set_nome)

    #retorna a idade da instancia pessoa
    def get_idade(self):
        return self.__idade
    
    #insere a idade da instancia pessoa
    def set_idade(self, idade):
        self.__idade = idade

    idade = property(get_idade, set_idade)

p1 = Pessoa() #atribui valores

#gera erro
#p1.set_nome(['ana'])
p1.set_nome('ana')
p1.set_idade(20)

print(p1.get_nome()) #ok
print(p1.get_idade()) #ok
