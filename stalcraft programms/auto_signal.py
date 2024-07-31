import keyboard
import pyautogui
import time
import win32gui

lampX = 691
lampY = 420
modeX = 1080
modeY = 800
scanX = 1350
scanY = 800
getSigX = 100
getSigY = 100
getSgLampX = 100
getSgLampY = 100


def pixel_color_at(x, y):
    hdc = win32gui.GetWindowDC(win32gui.GetDesktopWindow())
    c = int(win32gui.GetPixel(hdc,x, y))
    print(c)
    return (c & 0xff), ((c >> 8) & 0xff), ((c >> 16) & 0xff)

while True:
    keyboard.wait("f3")
    ahk = True
    has_signal = 0
    while ahk:
        keyboard.send("0")
        time.sleep(0.3)
        pix = pixel_color_at(lampX,lampY)
        for i in range(0,25):
            pix1 = pixel_color_at(lampX,lampY)
            if pix != pix1:
                has_signal = 1

        if has_signal == 1:
            ahk = False
            pyautogui.moveTo(modeX,modeY)
            pyautogui.leftClick()
            pyautogui.moveTo(scanX,scanY)
            pyautogui.leftClick()
            time.sleep(10.1)
            pyautogui.leftClick()
            

        else:
            keyboard.send("0")
