from modelos.restaurante import Restaurante

restarurante_jojo = Restaurante('Jojo', 'Japones')
restarurante_jojo.receber_avaliacao('Jobson', 9)
restarurante_jojo.receber_avaliacao('Joelma', 10)
restarurante_jojo.receber_avaliacao('Carolina', 7)
restarurante_jojo.receber_avaliacao('Maura', 5)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()