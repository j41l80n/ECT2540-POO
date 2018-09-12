import fila

if __name__ == "__main__":
    f = fila.Fila()
    print('### Estado inicial')
    f.imprime()

    for i in range(3):
        f.enfileira(i)

    print('### Apos enfileiramento')
    f.imprime()

    for i in range(3):
        e = f.desenfileira()
        print('Objeto removido: {}'.format(e))
        print('### fila')
        f.imprime()
