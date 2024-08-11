import os

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
    os.system('cls')
    print('Encerrando o App. \n')

def escolher_opcao():  
    opcao = int(input('Escolha uma opção: '))
    match opcao:
        case 1:
            print('Cadatrar restaurante \n')
        case 2:
            print('Listar resturante \n')
        case 3:
            print('Ativar restaurante \n')
        case 4:
            encerrar()
        case _:
            print('Opção invalida \n')

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
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()



if __name__ == '__main__':
    main()

