'''
1 - Crie uma lista para cada informação a seguir:
Lista de números de 1 a 10;
Lista com quatro nomes;
Lista com o ano que você nasceu e o ano atual.
lista_numeros = [1, 2, 3,]
lista_nomes = ['Jobson', 'Carolina']
lista_anos = [38, 15]

for numero in lista_numeros:
    print(numero)
for nome in lista_nomes:
    print(nome)
for ano in lista_anos:
    print(ano)

#------------------------------------------------------------------------------------

2 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.
lista = ['Jobson', 'Computador', 37]
for item in lista:
    print(item)

#----------------------------------------------------------------------------------

3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.
lista_numero = [1, 2, 3, 4, 5, 6, 7, 8, 9]
soma_impares = 0

for numero in lista_numero:
    if(numero % 2 == 1):
        soma_impares = soma_impares + numero
        print(numero)
print(soma_impares)

#------------------------------------------------------------------

4 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.
'''
for i in range(10, 0, -1):
    print(i)

'''
5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.

6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.

7 - Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.
'''