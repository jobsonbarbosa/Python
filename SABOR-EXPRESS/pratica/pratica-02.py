'''1 - Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else para determinar se o número é par ou ímpar.
'''
'''
numero = int(input('Digite um numero: '))

if numero % 2 == 0:
    print("Numero par")
else:
    print("Numero impar")

'''
#----------------------------------------------------

'''2 - Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para classificar a idade em categorias de acordo com as seguintes condições:

Criança: 0 a 12 anos;
Adolescente: 13 a 18 anos;
Adulto: acima de 18 anos.
'''

'''
idade = int(input('Digite seu idade: '))

if(idade >= 0 and idade <= 12):
    print('Criança')
elif(idade >= 13 and idade <= 18):
    print('Adolescente')
else:
    print('Adulto')
'''

# -----------------------------------------------------

'''3 - Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você. '''

name = 'Jobson'
pass1 = '123456'

nome = input('Digite o seu nome: ')
senha = input('Digite sua senha: ')

if(nome == name) and (senha == pass1):
    print('usuário valido')
else:
    print('Usuário ou senha incorrentos')