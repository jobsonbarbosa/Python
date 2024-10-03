from openai import OpenAI
from dotenv import load_dotenv ## funçaõ de leitura do ambiente virtual | acessar as chaves de acesso da OpenIA
import os

# Ler as chaves de acessos
load_dotenv()

# Criar um objeto para acessar a openAI

cliente = OpenAI(api_key=os.getenv("OPEN_API_KEY"))
modelo = "gpt-4"

def categoriza_produto(nome_produto, lista_categorias_possiveis):  
    prompt_sistema = f""" 

        Você é um categorizador de produtos.
        Você deve assumir as categorias presentes na lista abaixo.

        # Lista de Categoria Válidas
        {lista_categorias_possiveis.split(",")}

        # Formato de Saída
        Produto: Nome do Produto
        Categoria: apresente a categoria do produto

        # Exemplo de Saída
        Produto: Escova elétrica com recarga solar
        Categoria: Eletrônicos Verdes

    """

    resposta = cliente.chat.completions.create(
        messages=[
            {
                "role" : "system",
                "content" : prompt_sistema
            },
            {
                "role" : "user",
                "content" : nome_produto
            }
        ],
        model=modelo,
        temperature = 0,
        max_tokens=200,
    )

    return resposta.choices[0].message.content

categoriza_validas = input("Informe as categorias válidas, seperando por virgula: ")

while True:
    nome_produto = input("Digite o nome do produto: ")
    texto_resposta = categoriza_produto(nome_produto, categoriza_validas)
    print(texto_resposta)