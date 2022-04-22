import mss
import mss.tools
import numpy as np


with mss.mss() as sct:
    # Область
    monitor = {"top": 598, "left": 958, "width": 649, "height": 841}
    output = "sct-{top}x{left}_{width}x{height}.png".format(**monitor)
                        
    # Передача данных
    scr = np.array(sct.grab(monitor))
    scr_remove = scr[:,:,:3]
    # Сохранение
    mss.tools.to_png(scr_remove.rgb, scr_remove.size, output=output)
    print(output)