import os

restaurantes = ['Jojo', 'Mariposa', 'Tekai', 'Dmeg']

def exibir_nome_do_programa():

    print("""
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
    """)

def exibir_opcoes():
    print("1. Cadastrar restaurante")
    print("2. Listar restaurante")
    print("3. Ativar restaurante")
    print("4. Sair \n")

def encerrar():
    exibir_subtitulo('Encerrando o App.')

def voltar_menu_principal():
    input('\nDigite um tecla para voltar ao menu inicial ')
    main()

def opacao_invalida():
    print('Opcão invalida \n')
    voltar_menu_principal()

def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)
    print()

#função para cadastrar novo restaurante
def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    restaurantes.append(nome_restaurante)
    print(f'Restautante {restaurantes} cadastrado com sucesso! \n')
    voltar_menu_principal()

#listar restaurantes cadastrados
def listar_restaurantes():
    exibir_subtitulo('Listando restaurantes')

    for restaurante in restaurantes:
        print(restaurante)
       
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
                print('Ativar restaurante \n')
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

