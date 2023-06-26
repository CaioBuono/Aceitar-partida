import pyautogui
from time import sleep

def buscar_imagem():
    return pyautogui.locateOnScreen('aceitar.png')

imagem_encontrada = None

while True:
    localizar = buscar_imagem()
    imagem_encontrada = localizar
    if imagem_encontrada is not None:
        pyautogui.moveTo(imagem_encontrada,duration=1)
        pyautogui.click()
        break
    else:
        print('Imagem não encontrada')
        sleep(3)

