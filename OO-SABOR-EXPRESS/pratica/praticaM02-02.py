'''
2 - Crie uma classe chamada Restaurante com os atributos nome, categoria, ativo e crie mais 2 atributos. Instancie um restaurante e atribua valores aos seus atributos.
'''


class Restaurante():
    def __init__(self, nome, categoria, ativo=False):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo
    

jojo = Restaurante(nome='Jojo', categoria='Japones', ativo=True)

print(jojo.categoria)