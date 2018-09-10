class Celula(object):
 
    def __init__(self, dado, anterior, proximo):
        self.__dado = dado
        self.__anterior = anterior
        self.__proximo = proximo

class ListaEncadeada(object):
 
    head = None
    tail = None
 
    def acrescentar(self, dado):
        no = Celula(dado, None, None)

        if self.head is None:
            self.head = no
            self.rabo = no
        else:
            no.anterior = self.rabo
            no.proximo = None
            self.rabo.proximo = no
            self.rabo = no
 
    def remover(self, dado):
        no_atual = self.head
        while no_atual is not None:
            if no_atual.dado == dado:
                if no_atual.anterior is None:
                    self.head = no_atual.proximo
                    no_atual.proximo.anterior = None
                else:
                    no_atual.anterior.proximo = no_atual.proximo
                    no_atual.proximo.anterior = no_atual.anterior
            no_atual = no_atual.proximo
 
    def mostrar(self):
        print "Lista Encadeada:"
        no_atual = self.head
        no = ""
        while no_atual is not None:
            if no_atual.anterior is None:
                no += "None "
            no += "<---> | " + str(no_atual.dado) + " | "
            if no_atual.proximo is None:
                no += "<---> None"
 
            no_atual = no_atual.proximo
        print no
        print "="*80