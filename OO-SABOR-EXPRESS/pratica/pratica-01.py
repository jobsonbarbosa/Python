''' 
Crie uma classe chamada Musica com os atributos: 
nome
artista
duracao
'''

class Musica:
    nome = ''
    artista = ''
    duracao = ''

rock = Musica()
rock.nome = 'Aerials'
rock.artista = ' System Of A Down'
rock.duracao = 4.03

print(vars(rock))