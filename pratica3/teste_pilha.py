import pilha

if __name__ == "__main__":
    p = pilha.Pilha()
    print('### Estado inicial')
    p.imprime()

    for i in range(3):
        p.empilha(i)

    print('### Apos empilhamento')
    p.imprime()

    for i in range(3):
        e = p.desempilha()
        print('Objeto removido: {}'.format(e))
        print('### Pilha')
        p.imprime()
