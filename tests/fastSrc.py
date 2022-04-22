import mss
import mss.tools
import numpy as np


with mss.mss() as sct:
    # Область
    monitor = {"top":  717, "left": 954, "width": 651, "height": 687}
    #monitor = {"top": 953 , "left": 754, "width": 651, "height": 687}
    output = "sct-{top}x{left}_{width}x{height}.png".format(**monitor)
                        
    # Передача данных
    scr = sct.grab(monitor)
    # Сохранение
    mss.tools.to_png(scr.rgb, scr.size, output=output)
    print(output)