import pygame

#frames
clock = pygame.time.Clock()
fps=60
#score
score=0
killed=0
#windows size
width=600
height=800
game_window = pygame.display.set_mode((width, height))
#enemy
enemy_unit=[]
enemy_unit_x=[]
enemy_unit_y=[]
enemy_unit_drop=[]
enemy_moving=[]
units=[]
bar_update=50
escaped=0

#states
running = True
game_over=False
start_over=False
