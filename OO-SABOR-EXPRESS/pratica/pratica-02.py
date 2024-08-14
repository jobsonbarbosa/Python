''' 
[x] Atribua o valor 'Italiana' ao atributo categoria da instância restaurante_praca da classe Restaurante.
[x] Acesse o valor do atributo nome da instância restaurante_praca da classe Restaurante.
[x] Verifique o valor inicial do atributo ativo para a instância restaurante_praca e exiba uma mensagem informando se o restaurante está ativo ou inativo.
[x] Acesse o valor do atributo de classe categoria diretamente da classe Restaurante e armazene em uma variável chamada categoria.
[x] Altere o valor do atributo nome para 'Bistrô'.

'''

class Restaurante:
    nome = ''
    categoria = ''
    ativo = False

restaurante1 = Restaurante()
restaurante1.nome = 'Jojo'
restaurante1.categoria = "Italiana"
restaurante1.ativo = True

print(restaurante1.nome)
print(restaurante1.categoria)

if(restaurante1.ativo == True):
    print('Restaurante Ativo')
else:
    print('Restaurante Inativo')

restaurante1.nome = 'Bistro'
print(restaurante1.nome)
