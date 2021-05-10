import pygame,modules.vars as var,random
import modules.classes as classes

def music():
    pygame.mixer.music.play(-1)

def score_draw(score):
        font = pygame.font.SysFont('Verdana', 20)
        score_text = font.render("Score : "+str(score), 1, (255,255,255))
        var.game_window.blit(score_text, (5, 5))
        escaped_text = font.render("Escaped : "+str(var.escaped)+"/5", 1, (255,255,255))
        var.game_window.blit(escaped_text, (5, 30))

def draw(img,x,y):
    var.game_window.blit(img, (x, y))

def sound(sound):
    pygame.mixer.Sound.play(sound) 

def game_over_text():
    
    if var.game_over:
        
        pygame.mixer.music.stop()
        font = pygame.font.SysFont('Verdana', 50)
        game_over_text=font.render("GAME OVER", 1, (255,255,255))
        draw(game_over_text,150,300)
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    var.game_over=False 
                    var.running = False
                
def redraw():
    if not var.game_over:
        
        score_draw(var.score)
        classes.player.health_bar(var.bar_update)
        draw(classes.player.art,classes.player.x,classes.player.y)
        pygame.display.flip()



def player_movement():
    
    if not var.game_over:            
        action = pygame.key.get_pressed()
    
        if action[pygame.K_UP]: 
            classes.player.y -= classes.player.speed

        if action[pygame.K_DOWN]: 
            classes.player.y += classes.player.speed

        if action[pygame.K_LEFT]: 
            classes.player.x -= classes.player.speed

        if action[pygame.K_RIGHT]: 
            classes.player.x += classes.player.speed 

        if action[pygame.K_SPACE]:
            if not classes.projectile.state:
                classes.projectile.state = True
                sound(var.shooting_sound)
                classes.projectile.reset() 

        classes.player.boundaries(classes.player.x,classes.player.y)


def enemy_update():

    if classes.enemy.amount >= 50:
        classes.enemy.amount = 50
        classes.enemy.drop += 40

    elif classes.enemy.amount <= 0 :
        classes.enemy.amount += 5 + int(var.score/2)
        classes.enemy.speed += 3
        classes.enemy.drop += int(var.score/5)
        classes.projectile.speed +=1 


def create_enemies():    
    #create a list of enemies 
    for i in range(classes.enemy.amount):
            var.enemy_unit.append(pygame.image.load("art\\enemy" +str(random.randrange(1,5))+".png").convert_alpha())
            var.enemy_unit_x.append(random.randint(0,550))
            var.enemy_unit_y.append(random.randint(0,250))  
            var.enemy_unit_drop.append(classes.enemy.drop)
            var.enemy_moving.append(False)        
            draw(var.enemy_unit[i],var.enemy_unit_x[i],var.enemy_unit_y[i])


def enemy_movement():
    #handles the enemy movement , change their direction when they hit the walls
    for i in range(classes.enemy.amount):

            if  var.enemy_moving[i]:
                var.enemy_unit_x[i] += classes.enemy.speed
            else:            
                var.enemy_unit_x[i] -= classes.enemy.speed

            if  var.enemy_unit_x[i] >= 550:
                var.enemy_unit_x[i] = 550 
                var.enemy_unit_y[i] += var.enemy_unit_drop[i] 
                var.enemy_moving[i] = False

            elif var.enemy_unit_x[i] <= 0:
                var.enemy_unit_x[i] = 0
                var.enemy_unit_y[i] += var.enemy_unit_drop[i]
                var.enemy_moving[i] = True

            if  var.enemy_unit_y[i] >=750:
                var.escaped += 1
                var.enemy_unit_y[i] = 0
                classes.enemy.amount -= 1
                classes.enemy.remove(i)


def collision_check():
    if classes.projectile.state:
        for i in range(classes.enemy.amount):    
            if classes.projectile.hit(i):
                draw(var.explosion_art,var.enemy_unit_x[i],var.enemy_unit_y[i]) 
                var.score += 1                
                classes.enemy.amount -= 1        
                classes.projectile.state=False
                classes.projectile.reset()                  
                classes.enemy.remove(i)                   
                sound(var.explosion)    
        
    for i in range(classes.enemy.amount):
        if classes.player.hit(i): 
            draw(var.explosion_art,var.enemy_unit_x[i],var.enemy_unit_y[i])            
            classes.player.health -= 1

            if classes.player.health <= 0:
                classes.player.health = 0
                
            var.bar_update = classes.player.health * 10             
            sound(var.explosion) 
            classes.enemy.remove(i)
            classes.enemy.amount -= 1 