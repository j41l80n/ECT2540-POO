class UrnaEletronica:
    _candidatos = ['Mussum', 'Zacarias', 'Monteiro Lobato', 'Machado de Assis']

    def __init__(self, i=0):
        self._id_urna = i

    def registra_voto(self, v):
        if v not in UrnaEletronica._candidatos:
            print('Voto nulo')
        else:
            print('Voto registrado em {} na urna {}'.format(v, self._id_urna))

if __name__ == "__main__":
    u1 = UrnaEletronica(4001)
    u2 = UrnaEletronica(4002)
    u3 = UrnaEletronica(4003)

    u1.registra_voto('Jose')
    u1.registra_voto('Mussum')
    u2.registra_voto('Mussum')
    u3.registra_voto('Monteiro Lobato')