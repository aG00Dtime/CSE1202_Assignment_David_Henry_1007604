#imports
import pygame
from pygame.constants import MOUSEBUTTONDOWN 
from modules import collision as col
from modules.vars import enemy_moving,enemy_unit,enemy_unit_drop,enemy_unit_x,enemy_unit_y,clock,fps,score,game_window,bar_update,running,game_over,start_over,escaped
from modules.classes import enemy,player,projectile,shield
import random

#startup 
pygame.init()

#sounds and art
shooting_sound=pygame.mixer.Sound("sound\\shoot.wav")
explosion=pygame.mixer.Sound('sound\\explosion.wav')
bg=pygame.image.load("art\\bg.png").convert()
explosion_art=pygame.image.load("art\\explosion.png").convert_alpha()
shield_art=pygame.image.load("art\\shield.png").convert_alpha()
welcome=pygame.image.load("art\\welcome.png").convert()

#volume
pygame.mixer.Sound.set_volume(shooting_sound,0.015)
pygame.mixer.Sound.set_volume(explosion,0.05)

#set display size and title
pygame.display.set_caption("David Henry - 1007604 - CSE 1202")


# draw score
def score_draw(score):
        font = pygame.font.SysFont('Verdana', 20)
        score_text = font.render("Score : "+str(score), 1, (255,255,255))
        game_window.blit(score_text, (5, 5))
        escaped_text = font.render("Escaped : "+str(escaped)+"/5", 1, (255,255,255))
        game_window.blit(escaped_text, (5, 30))

# game over text when player dies
def game_over_text():
    global running
    global game_over
    font = pygame.font.SysFont('Verdana', 50)
    game_over_text=font.render("GAME OVER", 1, (255,255,255))
    game_window.blit(game_over_text, (150, 300))
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                running = False 

#show welcome screen
welcome_show=True
while welcome_show:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                welcome_show = False 
                running=False
        if event.type==pygame.KEYDOWN:
            welcome_show=False
    game_window.blit(welcome,(0,0))
    pygame.display.flip()


while running:
    #game over  
    if game_over:
        game_over_text()

        #close 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                running = False 

    #player movement            
    action = pygame.key.get_pressed()
    if not game_over:
        if action[pygame.K_UP]: 
            player.y -= player.speed

        if action[pygame.K_DOWN]: 
            player.y += player.speed

        if action[pygame.K_LEFT]: 
            player.x -= player.speed

        if action[pygame.K_RIGHT]: 
            player.x += player.speed 

        if action[pygame.K_SPACE]:
            if not projectile.state:
                projectile.state=True
                pygame.mixer.Sound.play(shooting_sound)
                projectile.reset() 

        #boundaries
        player.boundaries(player.x,player.y)
        
    #background
    game_window.blit(bg,(0,0)) 

     #projectile
    if projectile.y <=0:
            projectile.state=False
            projectile.reset()

    elif projectile.state:        
        game_window.blit(projectile.art,(projectile.x,projectile.y))
        projectile.y-=projectile.speed

    #reset enemy.amount
    if enemy.amount <= 0 :
        enemy.amount = 10   

    #for loops to check enemies
    if not game_over:
        for i in range(enemy.amount):
            enemy_unit.append(enemy.art)
            enemy_unit_x.append(random.randint(0,550))
            enemy_unit_y.append(random.randint(0,250))  
            enemy_unit_drop.append(enemy.drop)
            enemy_moving.append(False)        
            enemy.spawn(enemy_unit[i],enemy_unit_x[i],enemy_unit_y[i])

    #movement of enemies
    
        for i in range(enemy.amount):
            if  enemy_unit_x[i] >= 550:
                enemy_unit_x[i]=550 
                enemy_unit_y[i]+=enemy_unit_drop[i] 
                enemy_moving[i]=False

            elif enemy_unit_x[i] <= 0:
                enemy_unit_x[i]=0
                enemy_unit_y[i]+=enemy_unit_drop[i]
                enemy_moving[i]=True
                
            if  enemy_moving[i]==True:
                enemy_unit_x[i]+=enemy.speed
            else:            
                enemy_unit_x[i]-=enemy.speed

            if  enemy_unit_y[i] >=750:
                escaped+=1
                enemy_unit_y[i]=0
                enemy.amount-=1
                enemy.remove(i)
            
    # projectile hit
    for i in range(enemy.amount):
        if projectile.state:            
            if col.hit(projectile.x,projectile.y,enemy_unit_x[i],enemy_unit_y[i],40):
                game_window.blit(explosion_art,(enemy_unit_x[i],enemy_unit_y[i])) 
                score+=1                
                enemy.amount-=1        
                projectile.state=False
                projectile.reset()                  
                enemy.remove(i)                   
                pygame.mixer.Sound.play(explosion)          
            
    for i in range(enemy.amount):
        if col.hit(player.x,player.y,enemy_unit_x[i],enemy_unit_y[i],50):
            game_window.blit(explosion_art,(enemy_unit_x[i],enemy_unit_y[i])) 
            player.health-=1
            if player.health <=0:
                player.health=0
                
            bar_update=player.health*10             
            pygame.mixer.Sound.play(explosion) 
            enemy.remove(i)
            enemy.amount-=1 

    #player
    if player.health <=0:
        game_over=True 
    #escaped check
    if escaped >=5:
        game_over=True

    if not game_over:
        score_draw(score)
        player.health_bar(bar_update)
        game_window.blit(player.art,(player.x,player.y)) 

        #refresh display
        pygame.display.flip()
        clock.tick(fps)