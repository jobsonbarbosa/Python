'''
Crie uma classe chamada ContaBancaria com um construtor que aceita os parâmetros titular e saldo. Inicie o atributo ativo como False por padrão.
'''

class ContaBancaria():
    def __init__(self, titular, saldo, ativo = False):
        self.titular = titular
        self.saldo = saldo
        self.ativo = ativo
    def __str__(self):
             return(f'{self.titular} - {self.saldo} - {self.ativo}')
    
conta1 = ContaBancaria('Jobson', 99.00)

print(conta1)