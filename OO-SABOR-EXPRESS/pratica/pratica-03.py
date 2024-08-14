class Musica:
    
    musica = []
    def __init__(self, nome, artista, duracao):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao
        Musica.musica.append(self)
    
    def __str__(self):
        return f'{self.nome} | {self.artista} | {self.duracao}'
    
    def listar():
        for item in Musica.musica:
            print(f'{item.nome} | {item.artista} | {item.duracao}')

    musica1 = Musica('Jobson', 'Rock', 1212)

    listar()

