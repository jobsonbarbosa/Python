SECRETE_KEY = 'pyhton'

 #criando cenexão com o banco de dados
SQLALCHEMY_DATABASE_URI = '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD = 'mysql+mysqlconnector',
        usuario = 'root',
        senha = 'Mswat25',
        servidor = 'localhost',
        database = 'jogoteca'
)