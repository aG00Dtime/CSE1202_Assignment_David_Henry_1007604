import pygame,modules.vars as var

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
                
