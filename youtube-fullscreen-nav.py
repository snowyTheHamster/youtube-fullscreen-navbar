#stupid script that keeps mouse moving to prevent youtube 
# navbar hiding in fullscreen mode
import pyautogui as pag
import time

pag.FAILSAFE = True
print('move cursor to top left of screen to quit.')
print('Press Ctrl-C to quit.')
print('Press Ctrl-Alt-Del to quit.')

time.sleep(5)

for i in range(99999):
    pag.moveTo(3, 3, duration = 0.5)
    time.sleep(0.3)
    pag.moveTo(4, 4, duration = 0.5)
    time.sleep(0.3)