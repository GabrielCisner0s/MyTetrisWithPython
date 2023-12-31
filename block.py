from colors import Colors
import pygame
from position import Position

class Block:
    
    def __init__(self, id):
        self.id = id
        self.cells = {}# atributo diccionario
        self.cell_size = 30 #atributo celdas
        self.row_offset = 0 #atributo posicion fila 
        self.column_offset = 0#atributo posicion columna
        self.rotation_state = 0
        self.colors = Colors.get_cell_colors()

    def move(self, rows, columns):#metodo mover
        self.row_offset += rows
        self.column_offset += columns

    def get_cell_positions(self):#metodo obtener posicion de celdas
        tiles = self.cells[self.rotation_state]
        move_tiles = []#lista vacia para las losas
        for position in tiles:
            position = Position(position.row + self.row_offset, position.column + self.column_offset)
            move_tiles.append(position)#agrego posiciones a la lista
        return move_tiles


    def rotate(self):#metodo rotar
        self.rotation_state += 1
        if self.rotation_state == len(self.cells):
            self.rotation_state = 0


    def undo_rotation(self):#para evitar que en la rotacion, se salga de la pantalla
        self.rotation_state -= 1
        if self.rotation_state == -1:
            self.rotation_state = len(self.cells) - 1
     
    
    def draw(self, screen, offset_x, offset_y):#metodo dibujar losas
        tiles = self.get_cell_positions()
        for tile in tiles:
            tile_rect = pygame.Rect(offset_x + tile.column * self.cell_size, offset_y + tile.row * self.cell_size,
                                    self.cell_size -1, self.cell_size -1)
            pygame.draw.rect(screen, self.colors[self.id], tile_rect)
