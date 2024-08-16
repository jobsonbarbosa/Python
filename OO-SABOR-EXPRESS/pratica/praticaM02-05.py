'''
5 - Crie uma classe chamada Cliente e pense em 4 atributos. Em seguida, instancie 3 objetos desta classe e atribua valores aos seus atributos através de um método construtor.
'''

class Cliente():
    def __init__(self, nome, telefone, endereco, cidade):
        self.nome = nome
        self.telefone = telefone
        self.endereco = endereco
        self.cidade = cidade

'''
    def __str__(self):
        return (f'{self.nome}{self.telefone}{self.endereco}{self.cidade}')
'''

cliente1 = Cliente(nome="Jobson", telefone='71 994002274', endereco='Caminho 21, 34', cidade='Lauro de Freitas')

'''
cliente1.nome = 'Jobson'
cliente1.telefone = '71 994002274'
cliente1.endereco = 'Caminho 21, casa 34'
cliente1.cidade = 'Lauro de freitas'
'''
print(cliente1)