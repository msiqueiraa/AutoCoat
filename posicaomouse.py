import pyautogui
import time
from win32 import win32api
import win32.lib.win32con as win32con


time.sleep(1)


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0)
    time.sleep(1)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0)


rodar = True
while rodar == True:

    bixo = pyautogui.locateOnScreen('bixo.png', region=(
        0, 0, 1600, 900), confidence=0.7)
    if bixo != None:
        _location_ = pyautogui.center(bixo)
        x, y = _location_

    if bixo:
        time.sleep(1)
        click(x, y+150)
        time.sleep(1)
        print('achou', x, y+150)

    else:
        print('nao achou')
