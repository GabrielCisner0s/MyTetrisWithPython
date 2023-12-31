import pygame, sys
from game import Game
from colors import Colors


#inicializar pygame
pygame.init()

title_font = pygame.font.Font(None, 40)
score_surface = title_font.render("Score", True, Colors.white)
next_surface = title_font.render("Next", True, Colors.white)
game_over_surface = title_font.render("GAME OVER", True, Colors.white)

score_rect = pygame.Rect(320, 55, 170, 60)#tamaño de contenedor de
next_rect = pygame.Rect(320, 215, 170, 180)

#establese el tamaño de la pantalla
screen = pygame.display.set_mode((500, 620))

#Establecer titulo de ventana
pygame.display.set_caption("TETRIS")

#crear reloj para controlar la velocidad del juego
clock = pygame.time.Clock()

game = Game()

GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 400)#velocidad de caida de blockes

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

         #Controles   
        if event.type == pygame.KEYDOWN:
            if game.game_over == True:
                game.game_over = False
                game.reset()
            if event.key == pygame.K_LEFT and game.game_over == False:
                game.move_left()
            if event.key == pygame.K_RIGHT and game.game_over == False             :
                game.move_right()
            if event.key == pygame.K_DOWN and game.game_over == False:
                game.rotate_sound.play()
                game.move_down()
                game.update_score(0, 1)
            if event.key == pygame.K_UP and game.game_over == False:
                game.rotate()

        if event.type == GAME_UPDATE and game.game_over == False:#mueve el blocke hacia abato
                game.move_down()
        
    #dibujo pantalla
    score_value_surface = title_font.render(str(game.score), True, Colors.white)
                
    screen.fill(Colors.dark_blue)#fondo color
    screen.blit(score_surface, (365, 20, 50, 50))
    screen.blit(next_surface, (375, 180, 50, 50))

    if game.game_over == True:
        screen.blit(game_over_surface, (320, 450, 50, 50))
    pygame.draw.rect(screen, Colors.light_blue, score_rect, 0, 10)
    screen.blit(score_value_surface, score_value_surface.get_rect(centerx = score_rect.centerx,
                                                                  centery = score_rect.centery))
    
    pygame.draw.rect(screen, Colors.light_blue, next_rect, 0, 10)
    
    game.draw(screen)
    
    pygame.display.update()
    clock.tick(60)
