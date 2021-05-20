import pygame as pg
import math
from pygame.draw import rect
import random
pg.init()
width = 600
height = 700
display = pg.display.set_mode((width, height))

running=True
color = (255,0,0)

clock = pg.time.Clock()

rect_x=20
rect_y=10
angle=-(random.randint(10,360))

while running:
    for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False    
    
    
    display.fill((255,255,255))
    
    rect_x += math.cos(angle) * 1
    rect_y -= math.sin(angle) * 5
    print(rect_x,rect_y)

    pg.draw.rect(display, color, pg.Rect(rect_x,rect_y, 20, 20)) 

    if rect_x > 600:
        rect_x=600
    elif rect_x<= 0:
        rect_x=600

    if rect_y > 700:
        rect_y=0 

    elif rect_y <= 0:
        rect_y =700

    pg.display.update()

    clock.tick(60)










