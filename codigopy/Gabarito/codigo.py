# Passo 1: Entrar no sistema da empresa

import pandas
import pyautogui
import time


# pyautogui.write -> escrever texto
# pyautogui.click -> clicar com o mouse
# pyautogui.press -> apertar uma tecla
# pyautogui.hotkey -> apertar um atalho de teclado (Ctrl, C)

pyautogui.PAUSE = 0.5

# abrir o navegador
# apertar a tecla winfgjugb

pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")


# entrar no link: https://dlp.hashtagtreinamentos.com/python/intensivao/tabela


# Passo 2: Fazer login
pyautogui.write(
    "https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# Quero dar um pause de 2 segundos
time.sleep(2)
pyautogui.click(x=822, y=360)
pyautogui.write("uafaufb@hotmail.com")

# Passar para o proximo
pyautogui.press("tab")
pyautogui.write("fgjugb")

# Apertar no botão de login
pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(2)

# Passo 3: Importar a base de dados

tabela = pandas.read_csv("produtos.csv")
print(tabela)


# Passo 4: Cadastrar 1 produto
pyautogui.click(x=737, y=241)

# para cada linha da minha tabela

for linha in tabela.index:
    # texto = string
    pyautogui.click(x=737, y=241)
    # codigo
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    # marca
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")

    # tipo
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")

    # categoria
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    # preco unitario
    preco_unitario = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")

    # custo
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    # obs
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(str(obs))
    pyautogui.press("tab")

    # enviar
    pyautogui.press("enter")
    pyautogui.scroll(10000)
    # Passo 5: Repetir o processo de cadastro até acabar os produtos
