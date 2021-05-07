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

#sounds and art
pygame.init()
shooting_sound=pygame.mixer.Sound("sound\\shoot.wav")
explosion=pygame.mixer.Sound('sound\\explosion.wav')
bg=pygame.image.load("art\\bg.png").convert()
explosion_art=pygame.image.load("art\\explosion.png").convert_alpha()
shield_art=pygame.image.load("art\\shield.png").convert_alpha()
welcome=pygame.image.load("art\\welcome.png").convert()
pygame.mixer.music.load("sound\\music.wav")

#volume
pygame.mixer.Sound.set_volume(shooting_sound,0.015)
pygame.mixer.Sound.set_volume(explosion,0.05)




