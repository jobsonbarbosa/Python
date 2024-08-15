'''
Agora é sua vez! Crie uma nova classe chamada Pessoa com atributos como nome, idade e profissão. Adicione um método especial __str__ para imprimir uma representação em string da pessoa. Implemente também um método de instância chamado aniversario que aumenta a idade da pessoa em um ano. Por fim, adicione uma propriedade chamada saudacao que retorna uma mensagem de saudação personalizada com base na profissão da pessoa.
'''

class Pessoa():
    def __init__(self, nome='', idade='', profissao=''):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao
    
    def __str__(self):
        return (f'{self.nome},{self.idade} anos, {self.profissao}')
    
    def saudacao(self):
        if self.profissao:
            return f'Olá, sou {self.nome}!Trabalho como {self.profissao}.'
        else:
            return f'Olá sou {self.nome}'

    def aniversario(self):
        self.idade += 1

pessoa1 = Pessoa(nome='Jobson', idade=38, profissao='Analista BI')
pessoa2 = Pessoa(nome='Luiza', idade=30, profissao='Desenvolvedor')
pessoa3 = Pessoa(nome='Jaque', idade=22)

print(pessoa1)
print(pessoa2)
print(pessoa3)
print()

pessoa1.aniversario()
pessoa3.aniversario()

print("Informações após aniversário:")
print(pessoa1)
print(pessoa3)
print()

print(pessoa1.saudacao)
print(pessoa2.saudacao)
print(pessoa3.saudacao)