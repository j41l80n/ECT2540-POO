class Superclasse1:
    def __init__(self, valor):
        print('Inicializador de super1')
        self.atrib_super = valor

    def metodo_super(self):
        print('Metodo super de Superclasse1')

class Superclasse2:
    def __init__(self, valor):
        print('Inicializador de super2')
        self.atrib_super = valor

    def metodo_super(self):
        print('Metodo super de Superclasse2')

class Subclasse(Superclasse2, Superclasse1):
    def __init__(self, valor):
        #Superclasse1.__init__(self, 0) # atribui 0 a atrib_super1
        #Superclasse2.__init__(self, 1) # atribui 1 a atrib_super2
        super().__init__(valor)
        self.atrib_sub = valor

    def metodo_sub(self):
        print('Metodo sub')

if __name__ == "__main__":
    obj = Subclasse(50)
    print(obj.atrib_super) # qual atrib_super e utilizado?
    obj.metodo_super() # qual metodo_super e chamado?