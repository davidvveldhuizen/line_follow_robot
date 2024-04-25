import serial
import pygame as pg
from sys import exit

w,h = (290,470)

port = 'COM13'
ser = serial.Serial(port, 9600, timeout=1)  # Change baudrate if necessary
ser.write(b'S')

screen = pg.display.set_mode((w,h))
clock = pg.time.Clock()


read = False

threshold = 3000

while True:
  for event in pg.event.get():
    if event.type == pg.QUIT:
      pg.quit()
      exit()
    
    if event.type == pg.KEYDOWN:
      if event.unicode in ['s', 'S']:
        ser.write(b'S')
        read = True
        print('start reading')
        ser.readline()
      if event.unicode in ['t', 'T']:
        ser.write(b'T')
        read = False
  
  screen.fill((200,200,200))
  
  if read:
    line = ser.readline().decode().strip()
    values = [int(val) for val in line.split(',')]
    print(values)
    for i,value in enumerate(values):
      val = value / 10
      # if value < threshold:
      #   pg.draw.circle(screen, (0,0,0),(45 + i*50,0),20,20)
      pg.draw.rect(screen, (0,0,100),(30 + i*50, h - 30 - val, 30, val))
    
    
  pg.display.update()
  
  
  
      
