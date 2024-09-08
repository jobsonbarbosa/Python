from flask import Flask, render_template, request, redirect, session, flash, url_for
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
app.secret_key = 'pyhton'

#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:Mswat25@%@localhost/jogoteca'

 #criando cenexão com o banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD = 'mysql+mysqlconnector',
        usuario = 'root',
        senha = 'Mswat25',
        servidor = 'localhost',
        database = 'jogoteca'
    )

# instanciando o BD do SQLAlchemy
db = SQLAlchemy(app)

# Tabelas de Jogos
class Jogos(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), nullable=False)
    categoria = db.Column(db.String(40), nullable=False)
    console = db.Column(db.String(20), nullable=False)
    
    def __repr__(self):
        return '<Name %r>' % self.name

#Tabela de Usuários
class Usuarios(db.Model):
    nickname = db.Column(db.String(8), primary_key=True)
    nome = db.Column(db.String(20), nullable=False)
    senha = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.name      

@app.route('/')
def index():
    lista = Jogos.query.order_by(Jogos.id)
    return render_template('lista.html', titulo = 'Jogos', jogos = lista)

@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('novo')))
    return render_template('novo.html', titulo='Novo Jogo')

@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
        
    jogo = Jogos.query.filter_by(nome=nome).first()

    if jogo:
        flash('Jogos já existente!')
        return redirect(url_for('index'))

    novo_jogo = Jogos(nome=nome, categoria=categoria, console=console)
    db.session.add(novo_jogo)
    db.session.commit()

    return redirect(url_for('index'))
    

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima, titulo='login')

@app.route('/autenticar', methods=['POST',])
def autenticar():
    usuario = Usuarios.query.filter_by(nickname=request.form['usuario']).first()
    if usuario:
        if request.form['senha'] == usuario.senha:
            session['usuario_logado'] =  usuario.nickname
            flash(usuario.nickname + ' está logado com sucesso!')
            proxima_pagina = request.form["proxima"]
            return redirect(proxima_pagina)
    else:
        flash('Usuário não logado')
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso!')
    return redirect(url_for('index'))

app.run()