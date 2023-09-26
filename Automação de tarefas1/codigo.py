import pandas
import pyautogui
import time

pyautogui.PAUSE = 1
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press('enter')

time.sleep(5)


# pyautogui.click(x=1265, y=437)
# pyautogui.click(x=1649, y=-920)
pyautogui.click(x=1163, y=-900)


time.sleep(3)

pyautogui.write('alissonbc@gmail.com')
pyautogui.press('tab')
time.sleep(1)

pyautogui.write('sua senha aqui')
pyautogui.press('tab')
pyautogui.press('enter')

time.sleep(3)


tabela = pandas.read_csv("./produtos.csv")
print(tabela)

# pyautogui.click(x=1265, y=437)

# pyautogui.click(x=1738, y=-1045)


for linha in tabela.index:

    pyautogui.click(x=1058, y=-1042)

    codigo = tabela.loc[linha, 'codigo']

    pyautogui.write(str(codigo))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'marca']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'tipo']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'categoria']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'preco_unitario']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'custo']))
    pyautogui.press('tab')

    obs = tabela.loc[linha, 'obs']
    if not pandas.isna(obs):
        pyautogui.write(str(obs))

    pyautogui.press('tab')
    pyautogui.press('enter')

    pyautogui.scroll(50000)
