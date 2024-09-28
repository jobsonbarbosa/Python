from openai import OpenAI
from dotenv import load_dotenv ## funçaõ de leitura do ambiente virtual | acessar as chaves de acesso da OpenIA
import os

# Ler as chaves de acessos
load_dotenv()

# Criar um objeto para acessar a openAI

cliente = OpenAI(api_key=os.getenv("OPEN_API_KEY"))

resposta = cliente.chat.completions.create(
    messages=[
        {
            "role" : "system",
            "content" : "Listar apenas os nomes dos produtos, sem considerar a descrição."
        },
        {
            "role" : "user",
            "content" : "Liste 3 produtos sustentáveis."
        }
    ],
    model="gpt-4"
)

print(resposta.choices[0].message.content)