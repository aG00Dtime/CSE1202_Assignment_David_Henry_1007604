import modules.collision as col
import modules.vars as var
import pygame
import modules.misc as func


# player
class Player(object):
    def __init__(self):

        # starting position
        self.x = (var.width - 50) / 2
        self.y = var.height - 100

        # health
        self.health = 5

        # speed
        self.speed = 5

        # art
        self.art = pygame.transform.scale(pygame.image.load("art\\ship.png").convert_alpha(), (50, 50))

    # keep player inside the window
    def boundaries(self, x, y):
        if x >= 550:
            self.x = 550
        if x <= 0:
            self.x = 0
        if y >= 750:
            self.y = 750
        if y <= 600:
            self.y = 600

    @staticmethod
    def health_bar(bar_update):
        pygame.draw.rect(var.game_window, (55, 54, 78), pygame.Rect(player.x, player.y + 60, 50, 5))
        pygame.draw.rect(var.game_window, (89, 155, 134), pygame.Rect(player.x, player.y + 60, bar_update, 5))

    def hit(self, i):
        if col.hit(self.x, self.y, var.enemy_unit_x[i], var.enemy_unit_y[i], 40):
            return True


# enemy
class Enemy(object):
    def __init__(self):
        self.amount = 5
        # self.art=pygame.image.load("art\\enemy" +str(random.randrange(1,5))+".png").convert_alpha()
        self.speed = 10
        self.drop = 30

    # remove enemies from the list after they are destroyed
    @staticmethod
    def remove(enemy_id):
        var.enemy_unit.remove(var.enemy_unit[enemy_id])
        var.enemy_unit_x.remove(var.enemy_unit_x[enemy_id])
        var.enemy_unit_y.remove(var.enemy_unit_y[enemy_id])
        var.enemy_unit_drop.remove(var.enemy_unit_drop[enemy_id])
        var.enemy_moving.remove(var.enemy_moving[enemy_id])

    @staticmethod
    def draw():
        for i in range(enemy.amount):
            func.draw(var.enemy_unit[i], var.enemy_unit_x[i], var.enemy_unit_y[i])


# projectile
class Projectile(object):
    def __init__(self):
        self.state = False
        self.art = pygame.image.load("art\\bullet.png").convert_alpha()
        self.speed = 20
        self.x = player.x + 15
        self.y = player.y - 15

    # reset the projectile
    def reset(self):
        self.x = player.x + 15
        self.y = player.y - 15

    def hit(self, i):
        if col.hit(self.x, self.y, var.enemy_unit_x[i], var.enemy_unit_y[i], 40):
            return True


player = Player()
projectile = Projectile()
enemy = Enemy()
