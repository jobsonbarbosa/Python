'''
Na classe ContaBancaria, adicione um método especial __str__ que retorna uma mensagem formatada com o titular e o saldo da conta. Crie duas instâncias da classe e imprima essas instâncias.
'''

class ContaBancaria():
    def __init__(self, titular, saldo, ativo = False):
        self.titular = titular
        self.saldo = saldo
        self.ativo = ativo
    def __str__(self):
             return(f'{self.titular} - {self.saldo} - {self.ativo}')
    
conta1 = ContaBancaria('Jobson', 99.00)
conta2 = ContaBancaria('Jomesson', 15, True)

print(conta1)
print(conta2)
