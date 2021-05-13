# imports
import pygame

import modules.misc as func
import modules.vars as var
from modules.classes import player, projectile, enemy

# startup
pygame.init()

# set display size and title
# pygame.display.set_caption("David Henry - 1007604 - CSE 1202")


# show welcome screen
welcome_show = True

while welcome_show:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            welcome_show = False
            running = False
        elif event.type == pygame.KEYDOWN:
            welcome_show = False
    func.draw(var.welcome, 0, 0)
    pygame.display.flip()

# play music
func.music()
# main loop
while var.running:
    pygame.display.set_caption("David Henry - 1007604 - CSE 1202 -FPS :{}".format(var.clock.get_fps()))
    # game over  check
    func.game_over_text()

    # close
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            var.running = False
    # player movement
    func.player_movement()

    # background
    func.draw(var.bg, 0, 0)

    # projectile
    if projectile.y <= 0:
        projectile.state = False
        projectile.reset()
    if projectile.state:
        func.draw(projectile.art, projectile.x, projectile.y)
        projectile.y -= projectile.speed

    # for loops to check enemies
    if not var.game_over:
        func.create_enemies()

    enemy.draw()
    # movement of enemies
    func.enemy_update()
    func.enemy_movement()

    # projectile hit
    func.collision_check()

    # game over
    if player.health <= 0 or var.escaped >= 5:
        var.game_over = True

    # draw objects on the screen
    func.redraw()

    # fps
    var.clock.tick(var.fps)
