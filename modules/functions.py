import pygame
import modules.classes as classes
import modules.vars as var

def music():
    pygame.mixer.music.play(-1)

# draw the score on the screen
def score_draw(score):
    font = pygame.font.Font(var.path + "\\font\\New Space.ttf", 25)
    score_text = font.render("Score : " + str(score), True, (175, 167, 212))
    escaped_text = font.render("Escaped : " + str(var.escaped) + "/5", True, (175, 167, 212))
    stage_text = font.render("Stage : " + str(var.stage), True, (175, 167, 212))
    var.game_window.blit(score_text, (5, 5))
    var.game_window.blit(stage_text, (5, 30))
    var.game_window.blit(escaped_text, (5, 55))

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
        font = pygame.font.Font(var.path + "\\font\\ArtisualDeco.ttf", 50)
        game_over_message = font.render("GAME OVER", True, (255, 255, 255))
        draw(game_over_message, 150, 300)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                var.game_over = False
                var.running = False

# collision check
def collision_check():
    if classes.projectile.state:
        for i in range(classes.enemy.amount):
            if classes.projectile.hit(i):
                draw(var.explosion_art, var.enemy_unit_x[i], var.enemy_unit_y[i])
                classes.enemy.amount -= 1
                classes.enemy.remove(i)
                classes.projectile.state = False
                classes.projectile.reset()
                sound(var.explosion)
                var.score += 1

    for i in range(classes.enemy.amount):
        if classes.player.hit(i):
            draw(var.explosion_art, var.enemy_unit_x[i], var.enemy_unit_y[i])
            classes.player.health -= 1

            if classes.player.health <= 0:
                classes.player.health = 0

            var.bar_update = classes.player.health * 10
            sound(var.explosion)
            classes.enemy.amount -= 1
            classes.enemy.remove(i)