import time
import cv2
import mss
import pyautogui
from time import time, sleep
import keyboard
import numpy as np



pyautogui.PAUSE = 0
print("Для старта скрипта нажмите: " + "s")
print("Для его остановки: " + "q")
keyboard.wait('s')

need = cv2.imread("img/need.jpg")

sct = mss.mss()
monitor = {"top": 598, "left": 958, "width": 649, "height": 841}
x = 958
y = 598
w = need.shape[1]
h = need.shape[0]

fps_time = time()

while True:
    sct_img = np.array(sct.grab(monitor))
    scr_remove = sct_img[:,:,:3]
    result = cv2.matchTemplate(scr_remove, need, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(result)
    print(f"Max Val: {max_val} Max Loc: {max_loc}")
    src = sct_img.copy()
    if max_val >= .10:
        pyautogui.click(
            x = max_loc[0] + x, 
            y = max_loc[1] + y 
        )
    cv2.rectangle(sct_img, max_loc, (max_loc[0] + w, max_loc[1] + h), (0,255,255), 2)
    cv2.imshow('src', scr_remove)
    cv2.waitKey(1)
    
    # sleep(.001)
    if keyboard.is_pressed('q'):
        break

    print('FPS: {}'.format(1 / (time() - fps_time)))
    fps_time = time()
     

    
    