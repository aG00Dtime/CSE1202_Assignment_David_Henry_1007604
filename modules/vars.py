import pygame

import os

# frames
clock = pygame.time.Clock()
fps = 60

# score
score = 0
killed = 0

# windows size
width = 600
height = 700
game_window = pygame.display.set_mode((width, height))

# enemy
enemy_unit = []
enemy_unit_x = []
enemy_unit_y = []
enemy_unit_drop = []
enemy_moving = []
stage=1
# health bar
bar_update = 50

# enemies escaped
escaped = 0

# states
running = True
game_over = False
enemies_alive = False
# sounds and art
pygame.init()
enemy_art_list = [pygame.transform.scale(pygame.image.load("art\\enemy0.png").convert_alpha(), (50, 50)),
                  pygame.transform.scale(pygame.image.load("art\\enemy1.png").convert_alpha(), (50, 50)),
                  pygame.transform.scale(pygame.image.load("art\\enemy2.png").convert_alpha(), (50, 50)),
                  pygame.transform.scale(pygame.image.load("art\\enemy3.png").convert_alpha(), (50, 50)),
                  pygame.transform.scale(pygame.image.load("art\\enemy4.png").convert_alpha(), (50, 50))]
#
shooting_sound = pygame.mixer.Sound("sound\\shoot.wav")
explosion = pygame.mixer.Sound('sound\\explosion.wav')
bg = pygame.image.load("art\\bg.png").convert()
explosion_art = pygame.transform.scale(pygame.image.load("art\\explosion.png").convert_alpha(), (60, 60))
shield_art = pygame.image.load("art\\shield.png").convert_alpha()
welcome = pygame.image.load("art\\welcome.png").convert()
pygame.mixer.music.load("sound\\music.wav")

# volume
pygame.mixer.Sound.set_volume(shooting_sound, 0.015)
pygame.mixer.Sound.set_volume(explosion, 0.05)
pygame.mixer.music.set_volume(0.04)

#path
path = os.getcwd()
