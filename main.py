import pygame
from modules.classes import player, projectile, enemy
import modules.vars as var
import modules.misc as func
import math
import random
# startup
pygame.init()

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
    # background
    func.draw(var.bg, 0, 0)
    # screen title with fps
    pygame.display.set_caption("David Henry - 1007604 - CSE 1202 -FPS :{}".format(var.clock.get_fps()))
    # game over  check
    func.game_over_text()

    # close
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            var.running = False
    # projectile
    if projectile.y <= 0:
        projectile.state = False
        projectile.reset()
    if projectile.state:
        func.draw(projectile.art, projectile.x, projectile.y)
        projectile.y -= projectile.speed    

    # for loops to check enemies
    if not var.game_over:
        enemy.create()
        enemy.movement()
        enemy.amount_update()
        

        # projectile hit
        func.collision_check()     

    # draw objects on the screen
    
    func.score_draw(var.score)
    player.movement()
    player.health_bar(var.bar_update)
    player.update()
    

       
    # game over
    if player.health <= 0 or var.escaped >= 5:
        var.game_over = True
    # fps
    if not var.game_over:
        pygame.display.update()

    var.clock.tick(var.fps-1)
 



 