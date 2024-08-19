from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restarurante_jojo = Restaurante('Jojo', 'Japones')
bebida_suco = Bebida('Laranja', 5.0, 'grande')
prato_feijoada = Prato('Feijoada', 30.0, 'Feijoada da Nega Su')
restarurante_jojo.adicionar_no_cardapio(bebida_suco)
restarurante_jojo.adicionar_no_cardapio(prato_feijoada)

def main():
    restarurante_jojo.exibir_cardapio
    
if __name__ == '__main__':
    main()