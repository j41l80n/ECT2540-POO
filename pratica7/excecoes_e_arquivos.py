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
        try:
            self.arquivo = open(self.nome_arquivo, 'r') 
            n = int(self.arquivo.readline())
            self.arquivo.close()
            return n
        except Exception as err:
           print(f'Erro {err}')


    def _obtem_nome(self):
        """retorna o nome das pessoas em um arquivo"""
        try:
            self.arquivo = open(self.nome_arquivo, 'r') 
            for i in range(self._obtem_num_pessoas()):
                # print(i)
                # pessoas.append(i)
                pass
        except Exception as err:
           print(f'Erro {err}')

    def _obtem_idade(self):
        # Insira o seu código aqui
        pass

    def _obtem_atividades(self):
        # Insira o seu código aqui
        pass

    def processa(self):
        """processa o arquivo de pessoas"""
        self.arquivo.seek(1)
        # for p in pessoas in range(LeitorPessoas._obtem_num_pessoas(self)):
        #     print('1')
        pass
if __name__ == "__main__":
    leitor = LeitorPessoas('pessoas_erro4.txt')
    print(leitor._obtem_num_pessoas())
    leitor._obtem_nome()# leitor.processa()
    # leitor.processa()
    # for p in leitor.pessoas:
    #     print(p)
