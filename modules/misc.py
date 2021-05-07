import pygame,modules.vars as var

def play_music():
    pygame.mixer.music.play(-1)

def score_draw(score):
        font = pygame.font.SysFont('Verdana', 20)
        score_text = font.render("Score : "+str(score), 1, (255,255,255))
        var.game_window.blit(score_text, (5, 5))
        escaped_text = font.render("Escaped : "+str(var.escaped)+"/5", 1, (255,255,255))
        var.game_window.blit(escaped_text, (5, 30))

def draw(img,x,y):
    var.game_window.blit(img, (x, y))
