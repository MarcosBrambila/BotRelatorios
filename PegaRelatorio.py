import pyautogui as pe
import time

pe.hotkey('win', 'e')
pe.moveTo(488,305,duration=1)
pe.scroll(-800)
pe.click(515,559,duration=1)
pe.click(819,350,duration=1)
pe.write('marcos')
time.sleep(1)
pe.hotkey('enter')
pe.write('dev')
time.sleep(1)
pe.hotkey('enter')
time.sleep(1)
pe.hotkey('down')
pe.hotkey('ctrl', 'c')
time.sleep(1)
pe.hotkey('ctrl', 't')
pe.click(488,297, duration=1)
pe.doubleClick(700,357, duration=1)
time.sleep(1)
pe.hotkey('ctrl', 'v')
time.sleep(1)
pe.hotkey('enter')
time.sleep(3)
pe.hotkey('alt', 'f4')
