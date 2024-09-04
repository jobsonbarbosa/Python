#Automação em Python
# 1- Instalar e usar as bibliotecas
# 2 - Iniciar a Automação (pandas, pyautogui, time)
#   2.1 - Replicar a tarefa do usuário para cadastro
#   2.2 - Ler a base de dados
#   2.3 - Fazer cadastro de aluno por aluno


import pandas as pd
import pyautogui
import time


# Iniciar a automação

pyautogui.PAUSE = 0.5

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# Entrar no link
# sigte: http://www.sauer.pro.br/python/automacao/
pyautogui.write("http://www.sauer.pro.br/python/automacao/")
pyautogui.press("enter")
time.sleep(3)

pyautogui.click(x=525, y=267)
pyautogui.write("admin")
pyautogui.press("tab")
pyautogui.write("SimplificaPython")
pyautogui.press("tab")
pyautogui.press("enter")

# Importanto a base de dados de alunos
tabela = pd.read_csv('alunos.csv')
time.sleep(2)

# o comanda index tira a numeração dos dados da tabela
for linha in tabela.index:
    pyautogui.click(x=482, y=346)
    nome = tabela.loc[linha, "Nome"]
    pyautogui.write(nome)
    pyautogui.press("tab")

    pyautogui.click(x=484, y=439)
    email = tabela.loc[linha, "Email"]
    pyautogui.write(email)
    pyautogui.press("tab")

    pyautogui.click(x=476, y=525)
    endereco = tabela.loc[linha, "Endereco"]
    pyautogui.write(endereco)
    pyautogui.press("tab")

    pyautogui.click(x=470, y=608)
    telefone = tabela.loc[linha, "Telefone"]
    pyautogui.write(telefone)
    pyautogui.press("tab")
    pyautogui.scroll(5000)

    pyautogui.press("enter")




