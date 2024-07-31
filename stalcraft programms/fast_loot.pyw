import pyautogui as pg
import keyboard as kb

while True:
    kb.wait("`",True)
    kb.press("shift")
    pg.tripleClick()
    pg.tripleClick()
    pg.tripleClick()
    kb.release("shift")