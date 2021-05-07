import pygame,modules.collision as col,modules.vars as var
from modules.vars import width,height
from modules.vars import width,height,enemy_moving,enemy_unit,enemy_unit_drop,enemy_unit_x,enemy_unit_y,game_window

#player
class Player(object):
    def __init__(self):
        #starting position
        self.x=(width - 50) /2 
        self.y=height - 100
        #health
        self.health=5
        #speed
        self.speed=5
        #art
        self.art=pygame.image.load("art\\ship.png").convert_alpha()

        #keep player inside the window
    def boundaries(self,x,y):
        if x >= 550:
            self.x=550
        if x <=0:
            self.x=0
        if y >= 750:
            self.y=750
        if y <=600:
            self.y=600 

    def health_bar(self,bar_update):
        pygame.draw.rect(game_window,(0,0,0),pygame.Rect(player.x, player.y+60, 50, 5))        
        pygame.draw.rect(game_window,(0,255,0),pygame.Rect(player.x, player.y+60, bar_update, 5))
    
    def hit(self,i):
        if col.hit(self.x,self.y,var.enemy_unit_x[i],var.enemy_unit_y[i],40):
            return True
#enemy     
class Enemy(object):
    def __init__(self) :
        self.amount=10
        self.art=pygame.image.load("art\\enemy.png").convert_alpha()
        self.speed=10
        self.drop=30

    def remove(self,i):
            enemy_unit.remove(enemy_unit[i])
            enemy_unit_x.remove(enemy_unit_x[i])
            enemy_unit_y.remove(enemy_unit_y[i])
            enemy_unit_drop.remove(enemy_unit_drop[i])
            enemy_moving.remove (enemy_moving[i])        
#projectile
class Projectile(object):
    def __init__(self):
        self.state=False
        self.art=pygame.image.load("art\\bullet.png").convert_alpha()
        self.speed=20
        self.x=player.x+15
        self.y=player.y

    #reset the projectile
    def reset(self):        
        self.x=player.x+15
        self.y=player.y 

    def hit(self,i):
        if col.hit(self.x,self.y,var.enemy_unit_x[i],var.enemy_unit_y[i],40): 
            return True 
       

        
player=Player()
projectile=Projectile()
enemy=Enemy()

