from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# CLASSES NÃO UTLIZADAS
# class Jogo:
#     def __init__(self, nome, categoria, console):
#         self.nome = nome
#         self.categoria = categoria
#         self.console = console
        
# jogo1 = Jogo('Tetris', 'Puzzle', 'Atari')
# jogo2 = Jogo('God of War', 'Rack n Slash', 'PS2')
# jogo3 = Jogo('Mortal Kombat', 'Luta', 'PS2')
# lista = [jogo1, jogo2, jogo3]

# class Usuario:
#     def __init__(self, nome, nickname, senha):
#         self.nome = nome
#         self.nickname = nickname
#         self.senha = senha


# usuario1 = Usuario('Jobson Barbosa', 'Jobs', '1234')
# usuario2 = Usuario('Carolina Barbosa', 'Carol', '4567')
# usuario3 = Usuario('Joelma Almeida', 'Jo', '7890')

# usuarios = { 
#     usuario1.nickname : usuario1,
#     usuario2.nickname : usuario2,
#     usuario3.nickname : usuario3,
# }

app = Flask(__name__)

app.config.from_pyfile('config.py')

# instanciando o BD do SQLAlchemy
db = SQLAlchemy(app)

from views import *

if __name__ == '__main__':
    app.run()