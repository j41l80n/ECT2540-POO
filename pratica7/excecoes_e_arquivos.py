class ErroModulo(Exception):
    pass

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.atividades = []

    def insere_atividade(self, a):
        self.atividades.append(a)

    def __repr__(self):
        s = 'Nome: {}, idade: {}\n'.format(self.nome, self.idade)
        s += 'Atividades: '
        for a in self.atividades:
            s += a + ', '
        return s

class LeitorPessoas:
    def __init__(self, nome_arquivo):
        self.nome_arquivo = nome_arquivo
        self.pessoas = []
        self.arquivo = None

    def _obtem_num_pessoas(self):
        """retorna a quantidade de pessoas em um arquivo"""
        arq = open(self.nome_arquivo, 'r') 
        arq = int(arq.readline())
        return arq

    def _obtem_nome(self):
        # Insira o seu código aqui
        pass

    def _obtem_idade(self):
        # Insira o seu código aqui
        pass

    def _obtem_atividades(self):
        # Insira o seu código aqui
        pass

    def processa(self):
        """processa o arquivo de pessoas"""
        for p in pessoas in range(LeitorPessoas._obtem_num_pessoas(self)):
            print('1')
        # pass
if __name__ == "__main__":
    leitor = LeitorPessoas('pessoas.txt')
    print(leitor._obtem_num_pessoas())
    # leitor.processa()
    # leitor.processa()
    # for p in leitor.pessoas:
    #     print(p)
