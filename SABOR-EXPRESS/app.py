import os

restaurantes = [{'nome':'Jojo', 'categoria':'Japonesa', 'ativo':False},
                {'nome':'Mariposa', 'categoria':'Italiana', 'ativo':True},
                {'nome':'Tekai', 'categoria':'Chinesa', 'ativo':False}
]

#restaurantes = ['Jojo', 'Mariposa', 'Tekai', 'Dmeg']

def exibir_nome_do_programa():
    ''' Exibi o nome estilizado do programa '''
    print("""
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
    """)

def exibir_opcoes():
    ''' Exibir as opção disponiveis no menu principal '''
    print("1. Cadastrar restaurante")
    print("2. Listar restaurante")
    print("3. Alterar estado do restaurante")
    print("4. Sair \n")

def encerrar():
    ''' Exibi mensage de finalização do programa '''
    exibir_subtitulo('Encerrando o App.')

def voltar_menu_principal():
    ''' Solicita uma tecla para voltar ao menu principal '''
    input('\nDigite um tecla para voltar ao menu inicial ')
    main()

def opacao_invalida():
    ''' Exibi mensagem de opção inválida e retorna ao menu principal '''
    print('Opcão invalida \n')
    voltar_menu_principal()

def exibir_subtitulo(texto):
    ''' Limpa o terminar '''
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

#função para cadastrar novo restaurante
def cadastrar_novo_restaurante():
    ''' Essa função é responsavel por cadastrar um nono restaurante
    
    inputs:
        - Nome do restaurante
        - Categoria

    Output:
        - Adicionar restaurante a lista de restaurante

    '''
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categiria = input(f'Digite a categoria {nome_restaurante} ')

    dados_restaurante = {'nome': nome_restaurante, 'categoria':categiria, 'ativo':False}
    restaurantes.append(dados_restaurante)
    print(f'Restautante {nome_restaurante}\n \ncadastrado com sucesso! \n')
    voltar_menu_principal()

#listar restaurantes cadastrados
def listar_restaurantes():
    exibir_subtitulo('Listando restaurantes')

    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | {'Status'}')

    for restaurante in restaurantes:
        nome = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome.ljust(20)} | {categoria.ljust(20)} | {ativo}')
       
    voltar_menu_principal()

def alterar_estado():
    exibir_subtitulo('Alterando o estado do restaurante')

    nome_restaurante = input('Digite o nome do restaurante de deseja alterar o estado: ')
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante foi desativado com sucesso'
            print(mensagem)

    if not restaurante_encontrado:
        print('O restauranteo não foi encontrado')

    voltar_menu_principal()
'''
Foi aplicado o Try Except para tratar o erro com numero que não estejam nos contextos
dos match cases e princinpalmente quando digitado um string
onde o programa não é capaz de converte letra em numero
'''
def escolher_opcao():
    try:  
        opcao = int(input('Escolha uma opção: '))
        match opcao:
            case 1:
                #print('Listar resturante \n')
                cadastrar_novo_restaurante()
            case 2:
                listar_restaurantes()
            case 3:
                alterar_estado()
            case 4:
                encerrar()
            case _:
                opacao_invalida()
    except:
        opacao_invalida()
#INICIO
#------------------------------------------------------------------
    #print("Voce escolheu a opção: ", opcao)

    """ 
    a biblioteca OS é nativa do Python
    a bibliota OS é utilizada para executar interações com o sistema operacional,
    para usá-la basta importar a biblioteca
    """
"""    if opcao == 1:
        print('Cadastrar restaurante')
    elif opcao == 2:
        print('Listar restaurante')
    elif opcao == 3:
        print('Ativar restaurante')
    else:
        encerrar()
"""
#------------------------------------------------------------------
#FIM

"""a função def main define o arquivo como principal e onde é executado todas as funções
na inicializar do arquivo
"""
def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()



if __name__ == '__main__':
    main()

