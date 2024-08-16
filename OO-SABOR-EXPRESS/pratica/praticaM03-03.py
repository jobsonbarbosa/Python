'''
Crie uma classe chamada ContaBancaria com um construtor que aceita os parâmetros titular e saldo. Inicie o atributo ativo como False por padrão.
'''

class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        self._ativo = False #atributo protegido
    '''
    Na classe ContaBancaria, adicione um método especial __str__ que retorna uma mensagem formatada com o titular e o saldo da conta. Crie duas instâncias da classe e imprima essas instâncias.
    '''
    def __str__(self):
        return f'Conta de {self.titular} - Saldo: R${self.saldo}'
    
    @classmethod
    def ativar_conta(cls, conta):
        conta._ativo = True

conta1 = ContaBancaria('Jobson', 5200)
conta2 = ContaBancaria('Jobs IT', 4800)

print(conta1)
print(conta2)   

'''
Adicione um método de classe chamado ativar_conta à classe ContaBancaria que define o atributo ativo como True. Crie uma instância da classe, chame o método de classe e imprima o valor de ativo.
'''

conta3 = ContaBancaria('Jomesson', 3800)
print(f'Antes de ativar: {conta3._ativo}')

ContaBancaria.ativar_conta(conta3)
print(f'Depois de ativar: {conta3._ativo}')


'''
Refatore a classe ContaBancaria para utilizar a abordagem "pythonica" na criação de atributos. Utilize propriedades, se necessário.

Crie uma instância da classe e imprima o valor da propriedade titular.

Crie uma classe chamada ClienteBanco com um construtor que aceita 5 atributos. Instancie 3 objetos desta classe e atribua valores aos seus atributos através do método construtor.

Crie um método de classe para a conta ClienteBanco.
'''