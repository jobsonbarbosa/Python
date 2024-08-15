class Restaurante:


    restaurantes = []


    ''' __init__ metodo construtor de uma classe
    '''

    def __init__(self, nome, categoria):
        self._nome = nome.title()

        self._categoria = categoria.upper()

        self._ativo = False

        Restaurante.restaurantes.append(self)

    ''' __str__ função especial que define o valor da estacia do objeto que esta

        referenciando o local da memoria
    '''

    def __str__(self):

        return f'{self._nome} | {self._categoria} | {self._ativo}'


    @classmethod
    def listar_restaurantes(cls):

        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Status'}')

        for restaurante in cls.restaurantes:

            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante.ativo}')
    

    @property
    def ativo(self):

        return '✔️' if self._ativo else '❌'
    
    def alternar_estado(self):
        self._ativo = not self._ativo


restaurante_jojo = Restaurante('jojo', 'Japones')
restaurante_jojo.alternar_estado()

restaurante_Tekai = Restaurante('tekai', 'Chines')


Restaurante.listar_restaurantes()