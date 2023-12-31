from grid import Grid
from blocks import *
import random
import pygame


class Game:
    def __init__(self):
        self.grid = Grid()
        self.blocks =[IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        self.current_block = self.get_random_block()#blocke actual
        self.next_block = self.get_random_block()#siguiente blocke
        self.game_over = False #atributo end game
        self.score = 0
        self.rotate_sound = pygame.mixer.Sound("sounds/rotar_blocke.mp3")#sonido rotar o mover
        self.clear_sound = pygame.mixer.Sound("sounds/limpiar_fila.mp3")#sonido limpiar linea
        self.colision_sound = pygame.mixer.Sound("sounds/colision_blocke.mp3")#sonido colicion
        
        
       # pygame.mixer.music.load('sounds/Tetris.ogg')musica de fondo
       # pygame.mixer.music.play(-1)

    #sistema de puntos
    def update_score(self, lines_cleared, move_down_points):
        if lines_cleared == 1:
            self.score += 100
        elif lines_cleared == 2:
            self.score += 300
        elif lines_cleared == 3:
            self.score += 500
        self.score += move_down_points
        
    
        
    def get_random_block(self):#metodo obtener blocke aleatorio
        if len(self.blocks) == 0:#averiguo el num de elemntos en la lista
            self.blocks =[IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()] 
        block = random.choice(self.blocks)#devuelve un elemento aleatoriamente del atributo blocks y lo guarda en variable
        self.blocks.remove(block)
        return block


    #metodos para mover blockes
    def move_left(self):
        self.current_block.move(0, -1)
        if self.block_inside() == False or self.block_fits() == False:#si el blocke se sale
            self.current_block.move(0, 1)
        else:
            self.rotate_sound.play()#movimiento de blocke sonido
            
    def move_right(self):
        self.current_block.move(0, 1)
        if self.block_inside() == False or self.block_fits() == False:
             self.current_block.move(0, -1)
        else:
            self.rotate_sound.play()#movimiento de blocke sonido
            
    def move_down(self):
        self.current_block.move(1, 0)
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(-1, 0)
            self.lock_block()
            

    def lock_block(self):#metodo para usar otro blocke cuando este llegue al piso
        tiles = self.current_block.get_cell_positions()
        for position in tiles:
            self.grid.grid[position.row][position.column] = self.current_block.id
        self.current_block = self.next_block
        self.next_block = self.get_random_block()
        rows_cleared = self.grid.clear_full_rows()
        if rows_cleared > 0:
            self.clear_sound.play()#sonido al limpiar fila
            self.update_score(rows_cleared, 0)
        if self.block_fits() == False:
            self.game_over = True
        else:
            self.colision_sound.play()#sonido al colisionar en le suelo
            
    def reset(self):#al reiniciar el juego
        self.grid.reset()
        self.blocks =[IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.score = 0

        
    def block_fits(self):#metodo si los blockes encajan
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if self.grid.is_empty(tile.row, tile.column) == False:
                return False
        return True
                
        
            
    def rotate(self):
        self.current_block.rotate()
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.undo_rotation()
        else:
            self.rotate_sound.play()

            




    def block_inside(self):
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if self.grid.is_inside(tile.row, tile.column) == False:
                return False
        return True
    
    def draw(self, screen):#dibuja pantalla
        self.grid.draw(screen)
        self.current_block.draw(screen, 11, 11)

        #muestra los blockes que siguen en la interfas
        if self.next_block.id == 3:
            self.next_block.draw(screen, 255, 270)
        elif self.next_block.id == 4:
            self.next_block.draw(screen, 285, 270)
        else:
            self.next_block.draw(screen, 270, 270)
