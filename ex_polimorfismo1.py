class Pessoa:
    @staticmethod
    def _lista_pessoas(pessoas):
        media = 0
        for p in pessoas:
            print(p.idade)
            media += p.idade

        print(f'soma de idades: {media}')
        print(f'quantidade pessoas: {len(pessoas)}')
        
        return media / len(pessoas)

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __repr__(self):
        return 'Nome: {}, Idade: {}'.format(self.nome, self.idade)

    @staticmethod
    def compara_idades(p1, p2):
        """
        Retorna verdadeiro se p1 for mais novo que p2.
        """
        if isinstance(p1, Pessoa) and isinstance(p2, Pessoa):
            return p1.idade <= p2.idade
        else:
            print('Os objetos precisam ser derivados da classe pessoa')

class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula):
        Pessoa.__init__(self, nome, idade)
        self.matricula = matricula

    def __repr__(self):
        s = Pessoa.__repr__(self)
        s += '\nMatricula: {}'.format(self.matricula)
        return s

class Professor(Pessoa):
    def __init__(self, nome, idade, departamento):
        Pessoa.__init__(self, nome, idade)
        self.departamento = departamento

    def __repr__(self):
        s = Pessoa.__repr__(self)
        s += '\nDepartamento: {}'.format(self.departamento)
        return s

if __name__ == "__main__":
    #Pessoa p = Aluno('joaquim', 18, 123) # forma 1: incompativel com Python
    p = Pessoa('joao', 25)
    a = Aluno('hugo', 20, 111)
    prof = Professor('santos', 40, 'ECT')

    p1 = Pessoa('maria', 28)
    a1 = Aluno(p1.nome, p1.idade, 222) # forma 2: typecasting (?)
    
    print(Pessoa.compara_idades(prof, a)) # forma 3: método que recebe objetos derivados de pessoa

    for ps in [p, a, prof]:
        print(ps) # forma 4: sobrecarga de operadores

    lista = list()
    lista.append(p)
    lista.append(a)
    lista.append(prof)

    print(f'media de idades {a1._lista_pessoas(lista)}')