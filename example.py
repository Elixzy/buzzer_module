from machine import Pin
from music import play
import time

pin = Pin(33, Pin.OUT)

tetris = ('E_6_ne', 'B_5_co', 'C_6_co', 'D_6_ne', 'C_6_co','B_5_co','A_5_ne','A_5_co','C_6_co',
          'E_6_ne','D_6_co', 'C_6_co','B_5_ne','B_5_co','C_6_co','D_6_ne','E_6_ne','C_6_ne','A_5_ne','A_5_ne','PAUSE_ne',
          'PAUSE_co','D_6_ne','F_6_co','A_6_ne','G_6_co','F_6_co','E_6_ne','PAUSE_co','C_6_co','E_6_ne','D_6_co', 
          'C_6_co','B_5_ne','B_5_co','C_6_co','D_6_ne','E_6_ne','C_6_ne','A_5_ne','A_5_ne','PAUSE_ne')

while True:
    play(pin, tetris, 127, 0.5)
    time.sleep(1)