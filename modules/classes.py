import pygame
import random
import modules.vars as var
import modules.functions as func
import modules.collision as col


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

    # keep player inside the window and restricted to the bottom

    def boundaries(self, x, y):
        if x >= 550:
            self.x = 550
        if x <= 0:
            self.x = 0
        if y >= 625:
            self.y = 625
        if y <= 550:
            self.y = 550

    @staticmethod
    def health_bar(bar_update):
        pygame.draw.rect(var.game_window, (55, 54, 78), pygame.Rect(player.x, player.y + 60, 50, 5))
        pygame.draw.rect(var.game_window, (89, 155, 134), pygame.Rect(player.x, player.y + 60, bar_update, 5))

    def hit(self, i):
        if col.hit(self.x, self.y, var.enemy_unit_x[i], var.enemy_unit_y[i], 40):
            return True

    def update(self):
        if not var.game_over:
            func.draw(self.art, self.x, self.y)
            

    # handles player movement

    def movement(self):
        if not var.game_over:
            action = pygame.key.get_pressed()

            if action[pygame.K_UP]:
                self.y -= self.speed

            if action[pygame.K_DOWN]:
                self.y += self.speed

            if action[pygame.K_LEFT]:
                self.x -= self.speed

            if action[pygame.K_RIGHT]:
                self.x += self.speed

            if action[pygame.K_SPACE]:
                if not projectile.state:
                    projectile.state = True
                    func.sound(var.shooting_sound)
                    projectile.reset()

            self.boundaries(self.x, self.y)


# enemy

class Enemy(object):

    # enemy class
    def __init__(self):
        self.amount = 5
        self.speed = 1
        self.drop = 20

    # remove enemies from the list after they are destroyed

    @staticmethod # removes enemy data from the lists 
    def remove(enemy_id):
        var.enemy_unit.remove(var.enemy_unit[enemy_id])
        var.enemy_unit_x.remove(var.enemy_unit_x[enemy_id])
        var.enemy_unit_y.remove(var.enemy_unit_y[enemy_id])
        var.enemy_unit_drop.remove(var.enemy_unit_drop[enemy_id])
        var.enemy_moving.remove(var.enemy_moving[enemy_id])

    # handles the enemy movement , change their direction when they hit the walls
    def movement(self):

        for i in range(self.amount):
            if var.enemy_moving[i]:
                var.enemy_unit_x[i] += self.speed
            else:
                var.enemy_unit_x[i] -= self.speed

            if var.enemy_unit_x[i] >= 550:
                var.enemy_unit_x[i] = 550
                var.enemy_unit_y[i] += var.enemy_unit_drop[i]
                var.enemy_moving[i] = False

            elif var.enemy_unit_x[i] <= 0:
                var.enemy_unit_x[i] = 0
                var.enemy_unit_y[i] += var.enemy_unit_drop[i]
                var.enemy_moving[i] = True

            if var.enemy_unit_y[i] >= 650:
                var.escaped += 1
                var.enemy_unit_y[i] = 0
                self.amount -= 1
                self.remove(i)

    # create the enemy list

    def create(self):

        if var.enemies_alive:
            art = var.enemy_art_list[4]
        else:
            art = var.enemy_art_list[random.randrange(0, 4)]

        for i in range(self.amount):
            var.enemy_unit.append(art)
            var.enemy_unit_x.append(random.randint(0, 550))
            var.enemy_unit_y.append(random.randint(0, 300))
            var.enemy_unit_drop.append(self.drop)
            var.enemy_moving.append(False)
            func.draw(var.enemy_unit[i], var.enemy_unit_x[i], var.enemy_unit_y[i])

        if self.amount != 0:
            var.enemies_alive = True
            
        else:
            var.enemies_alive = False
            var.enemy_unit.clear()
            var.stage += 1

    # update enemy list
    def amount_update(self):
        if self.amount >= 50:
            self.amount = 50
            self.drop += 50

        if self.amount <= 0:
            if self.amount < 50:
                self.amount += 5 + int(var.score * .5)
            self.speed += 2
            self.drop += int(var.score * .25)
            projectile.speed += 5


# projectile
class Projectile(object):

    def __init__(self):
        self.state = False
        self.art = pygame.image.load("art\\bullet.png").convert_alpha()
        self.speed = 10
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
