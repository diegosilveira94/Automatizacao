import pyautogui as pa
import time
pa.PAUSE = 2

pa.press('win')
pa.write('lightroom')
pa.press('ENTER')
time.sleep(5)
pa.hotkey('ctrl','alt','1')
pa.hotkey('ctrl','0')
pos_Click1 = pa.locateOnScreen('filter_key_words.png')
pa.click(pos_Click1)
pa.write('1 - ')
pos_Click2 = pa.locateOnScreen('number_1.png')
pa.click(pos_Click2)