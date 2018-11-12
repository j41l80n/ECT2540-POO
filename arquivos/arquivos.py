class Arquivo:
    arq = open('arq.txt', 'r')

    def __init__(self):
        for l in arq.readlines():
            print(l)

    def escrever(self, texto):
        arq.write(texto)

arquivo = Arquivo()
print(arquivo)
arquivo.escrever('novo teste')
print(arquivo)