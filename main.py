from windowcapture import WindowCapture
import cv2
import os
import keyboard
from time import time
import numpy as nps
import pyautogui

# Указать название клиента
os.chdir(os.path.dirname(os.path.abspath(__file__)))
# Безымянный - Paint
# screen = WindowCapture('Безымянный - Paint')
screen = WindowCapture('GAMEE - Play games, WIN REAL CASH! — Личный: Microsoft​ Edge')
need = cv2.imread("img/need.jpg",)
w = need.shape[1]
h = need.shape[0]

print("Для старта скрипта нажмите: " + "s")
print("Для его остановки: " + "q")
pyautogui.PAUSE = 0.01
keyboard.wait("s")
loop_time = time()

def get_screen(screen):
    src = screen.get_screenshot()
    return src


def gui_click(max_val, max_loc):
    if max_val >= .40:
        # cv2.rectangle(scr, max_loc, (max_loc[0] + w, max_loc[1] + h), (0,255,255), 2)
        pyautogui.click(
            x = max_loc[0], 
            y = max_loc[1]
        )
    else:
        pyautogui.click(
            x = 41,
            y = 1370
        )

def rectangleDetect(scr, max_val, max_loc):
    if max_val >= .40:
        cv2.rectangle(scr, max_loc, (max_loc[0] + w, max_loc[1] + h), (0,255,255), 2)

while True:
      
    scr = get_screen(screen)
    
    result = cv2.matchTemplate(scr, need, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(result)
    
    # Для кликов
    gui_click(max_val, max_loc)
    # Для проверки 
    # rectangleDetect(scr, max_val, max_loc)
    
    # cv2.imshow('result', result)
    cv2.imshow('scr', scr)
    cv2.waitKey(1)
    
    if keyboard.is_pressed('q'): 
        break

    print('FPS {}'.format(1 / (time() - loop_time))) 
    
    loop_time = time() 
    
    
    
    