#imports
import pygame 
from modules import collision as col
from modules.vars import enemy_moving,enemy_unit,enemy_unit_drop,enemy_unit_x,enemy_unit_y,clock,fps,score,game_window,killed
from modules.classes import enemy,player,projectile,shield
import random

#startup 
pygame.init()
#sounds
shooting_sound=pygame.mixer.Sound("sound\\shoot.wav")
explosion=pygame.mixer.Sound('sound\\explosion.wav')
bg=pygame.image.load("art\\bg.png")
explosion_art=pygame.image.load("art\\explosion.png")
shield_art=pygame.image.load("art\\shield.png")
#volume
pygame.mixer.Sound.set_volume(shooting_sound,0.015)
pygame.mixer.Sound.set_volume(explosion,0.05)

#set display size and title
pygame.display.set_caption("David Henry - 1007604 - CSE 1202")
#score
font = pygame.font.SysFont('Verdana', 20)

def score_draw(score):
        score_text = font.render("Score : "+str(score), 1, (255,255,255))
        game_window.blit(score_text, (5, 12))
#main game loop
running = True

while running:  
        #close 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                running = False 
                
    #player movement            
    action = pygame.key.get_pressed()

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
        enemy.amount = 50
    
    #for loops to check enemies
    for i in range(enemy.amount):
        enemy_unit.append(enemy.art)
        enemy_unit_x.append(random.randint(0,400))
        enemy_unit_y.append(random.randint(0,200))  
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
            enemy_unit_x[i]=random.randint(0,40)
            enemy_unit_y[i]+=enemy_unit_drop[i]
            enemy_moving[i]=True
            
        if  enemy_moving[i]==True:
            enemy_unit_x[i]+=enemy.speed
        else:            
            enemy_unit_x[i]-=enemy.speed

        if  enemy_unit_y[i] >=750:
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
                    
                

    
    
    if shield.active:        
        
        game_window.blit(shield_art,(player.x-25,player.y-25))        

        for i in range(enemy.amount):
            if col.hit(player.x,player.y,enemy_unit_x[i],enemy_unit_y[i],100):
                shield.health-=1
                pygame.mixer.Sound.play(explosion) 
                enemy.remove(i)
                enemy.amount-=1 
                
    else:
        for i in range(enemy.amount):
            if col.hit(player.x,player.y,enemy_unit_x[i],enemy_unit_y[i],50):
                game_window.blit(explosion_art,(enemy_unit_x[i],enemy_unit_y[i])) 
                player.health-=1    
                pygame.mixer.Sound.play(explosion) 
                enemy.remove(i)
                enemy.amount-=1  

    #player
    score_draw(score)
    game_window.blit(player.art,(player.x,player.y))
    
        
    #refresh display
    pygame.display.flip()
    clock.tick(fps)


    







