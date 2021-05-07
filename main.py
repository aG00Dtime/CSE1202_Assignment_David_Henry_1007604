#imports
import pygame
from modules import collision as col
import modules.vars as var
from modules.classes import enemy,player,projectile
import random
import modules.misc as func

#startup 
pygame.init()

#set display size and title
pygame.display.set_caption("David Henry - 1007604 - CSE 1202")

#game over text when player dies
def game_over_text():
    global running
    global game_over
    font = pygame.font.SysFont('Verdana', 50)
    game_over_text=font.render("GAME OVER", 1, (255,255,255))
    func.draw(game_over_text,150,300)
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
        elif event.type==pygame.KEYDOWN:
            welcome_show=False
    var.game_window.blit(var.welcome,(0,0))
    pygame.display.flip()

#play music
func.play_music()
while var.running:
    #game over  
    if var.game_over:
        game_over_text()

    #close 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                var.running = False 

    #player movement            
    action = pygame.key.get_pressed()
    if not var.game_over:
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
                pygame.mixer.Sound.play(var.shooting_sound)
                projectile.reset() 

        #boundaries
        player.boundaries(player.x,player.y)
        
    #background    
    func.draw(var.bg,0,0)

    #projectile
    if projectile.y <=0:
            projectile.state=False
            projectile.reset()

    elif projectile.state:        
        var.game_window.blit(projectile.art,(projectile.x,projectile.y))
        projectile.y-=projectile.speed

    #reset enemy.amount
    if enemy.amount >= 100:
        enemy.amount = 100
        enemy.drop+=50
    elif enemy.amount <= 0 :
        enemy.amount += int(var.score/2)
        enemy.speed += 1
        enemy.drop += int(var.score/5)
        projectile.speed +=1

    #for loops to check enemies
    if not var.game_over:
        for i in range(enemy.amount):
            var.enemy_unit.append(enemy.art)
            var.enemy_unit_x.append(random.randint(0,550))
            var.enemy_unit_y.append(random.randint(0,250))  
            var.enemy_unit_drop.append(enemy.drop)
            var.enemy_moving.append(False)        
            enemy.spawn(var.enemy_unit[i],var.enemy_unit_x[i],var.enemy_unit_y[i])

        #movement of enemies    
        for i in range(enemy.amount):
            if  var.enemy_unit_x[i] >= 550:
                var.enemy_unit_x[i]=550 
                var.enemy_unit_y[i]+=var.enemy_unit_drop[i] 
                var.enemy_moving[i]=False

            elif var.enemy_unit_x[i] <= 0:
                var.enemy_unit_x[i]=0
                var.enemy_unit_y[i]+=var.enemy_unit_drop[i]
                var.enemy_moving[i]=True
                
            if  var.enemy_moving[i]==True:
                var.enemy_unit_x[i]+=enemy.speed
            else:            
                var.enemy_unit_x[i]-=enemy.speed

            if  var.enemy_unit_y[i] >=750:
                var.escaped+=1
                var.enemy_unit_y[i]=0
                enemy.amount-=1
                enemy.remove(i)
            
    #projectile hit
    for i in range(enemy.amount):
        if projectile.state:            
            if col.hit(projectile.x,projectile.y,var.enemy_unit_x[i],var.enemy_unit_y[i],40):
                var.game_window.blit(var.explosion_art,(var.enemy_unit_x[i],var.enemy_unit_y[i])) 
                var.score+=1                
                enemy.amount-=1        
                projectile.state=False
                projectile.reset()                  
                enemy.remove(i)                   
                pygame.mixer.Sound.play(var.explosion)          
            
    for i in range(enemy.amount):
        if col.hit(player.x,player.y,var.enemy_unit_x[i],var.enemy_unit_y[i],50):
            var.game_window.blit(var.explosion_art,(var.enemy_unit_x[i],var.enemy_unit_y[i])) 
            player.health-=1
            if player.health <=0:
                player.health=0
                
            var.bar_update=player.health*10             
            pygame.mixer.Sound.play(var.explosion) 
            enemy.remove(i)
            enemy.amount-=1 

    #player
    if player.health <=0:
        var.game_over=True
        
    #escaped check
    if var.escaped >=5:
        var.game_over=True
        

    if not var.game_over:
        func.score_draw(var.score)
        player.health_bar(var.bar_update)
        func.draw(player.art,player.x,player.y)

        #refresh display
        pygame.display.flip()
        var.clock.tick(var.fps)