import modules.vars as var
import pygame
import random

import modules.classes as classes


# play music
def music():
    pygame.mixer.music.play(-1)


# draw the score on the screen
def score_draw(score):
    font = pygame.font.SysFont('Verdana', 20)
    score_text = font.render("Score : " + str(score), True, (255, 255, 255))
    var.game_window.blit(score_text, (5, 5))
    escaped_text = font.render("Escaped : " + str(var.escaped) + "/5", True, (255, 255, 255))
    var.game_window.blit(escaped_text, (5, 30))


# function to draw things
def draw(img, x, y):
    var.game_window.blit(img, (x, y))


# play sound effects
def sound(sound_effect):
    pygame.mixer.Sound.play(sound_effect)


# game over message
def game_over_text():
    if var.game_over:

        pygame.mixer.music.stop()
        font = pygame.font.SysFont('Verdana', 50)
        game_over_message = font.render("GAME OVER", True, (255, 255, 255))
        draw(game_over_message, 150, 300)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                var.game_over = False
                var.running = False


# update screen objects
def redraw():
    if not var.game_over:
        score_draw(var.score)
        classes.player.health_bar(var.bar_update)
        draw(classes.player.art, classes.player.x, classes.player.y)
        pygame.display.flip()


# handles player movement
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

        classes.player.boundaries(classes.player.x, classes.player.y)


# update enemy list
def enemy_update():
    if classes.enemy.amount >= 50:
        classes.enemy.amount = 50
        classes.enemy.drop += 40

    elif classes.enemy.amount <= 0:
        classes.enemy.amount += 5 + int(var.score / 2)
        classes.enemy.speed += 3
        classes.enemy.drop += int(var.score / 5)
        classes.projectile.speed += 1


# create enemies and append them to a list
def create_enemies():
    # create a list of enemies 
    for i in range(classes.enemy.amount):
        var.enemy_unit.append(random.choice(var.enemy_art_list))
        var.enemy_unit_x.append(random.randint(0, 550))
        var.enemy_unit_y.append(random.randint(0, 250))
        var.enemy_unit_drop.append(classes.enemy.drop)
        var.enemy_moving.append(False)
        draw(var.enemy_unit[i], var.enemy_unit_x[i], var.enemy_unit_y[i])


# handles enemy movement
def enemy_movement():
    # handles the enemy movement , change their direction when they hit the walls
    for i in range(classes.enemy.amount):

        if var.enemy_moving[i]:
            var.enemy_unit_x[i] += classes.enemy.speed
        else:
            var.enemy_unit_x[i] -= classes.enemy.speed

        if var.enemy_unit_x[i] >= 550:
            var.enemy_unit_x[i] = 550
            var.enemy_unit_y[i] += var.enemy_unit_drop[i]
            var.enemy_moving[i] = False

        elif var.enemy_unit_x[i] <= 0:
            var.enemy_unit_x[i] = 0
            var.enemy_unit_y[i] += var.enemy_unit_drop[i]
            var.enemy_moving[i] = True

        if var.enemy_unit_y[i] >= 750:
            var.escaped += 1
            var.enemy_unit_y[i] = 0
            classes.enemy.amount -= 1
            classes.enemy.remove(i)


# collision check
def collision_check():
    if classes.projectile.state:
        for i in range(classes.enemy.amount):
            if classes.projectile.hit(i):
                draw(var.explosion_art, var.enemy_unit_x[i], var.enemy_unit_y[i])
                var.score += 1
                classes.enemy.remove(i)
                classes.enemy.amount -= 1
                classes.projectile.state = False
                classes.projectile.reset()
                sound(var.explosion)

    for i in range(classes.enemy.amount):
        if classes.player.hit(i):
            draw(var.explosion_art, var.enemy_unit_x[i], var.enemy_unit_y[i])
            classes.player.health -= 1

            if classes.player.health <= 0:
                classes.player.health = 0

            var.bar_update = classes.player.health * 10
            sound(var.explosion)
            classes.enemy.remove(i)
            classes.enemy.amount -= 1
