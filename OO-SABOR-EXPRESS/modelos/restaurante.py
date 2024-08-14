class Restaurante:

    restaurantes = []

    ''' __init__ metodo construtor de uma classe
    '''
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        Restaurante.restaurantes.append(self)
    ''' __str__ função especial que define o valor da estacia do objeto que esta
        referenciando o local da memoria
    '''
    def __str__(self):
        return f'{self.nome} | {self.categoria} | {self.ativo}'

    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome} | {restaurante.categoria} | {restaurante.ativo}')

restaurante_jojo = Restaurante('Jojo', 'Japones')

restaurante_Tekai = Restaurante('Tekai', 'Chines')

Restaurante.listar_restaurantes()