from block import Block
from position import Position

#blocke 1
class LBlock(Block):
    def __init__(self):#CONSTRUCTOR BLOCKE
        super().__init__(id = 1)
        self.cells = {
                0:[Position(0, 2), Position(1, 0), Position(1, 1), Position(1, 2)],
                1:[Position(0, 1), Position(1, 1), Position(2, 1), Position(2, 2)],
                2:[Position(1, 0), Position(1, 1), Position(1, 2), Position(2, 0)],
                3:[Position(0, 0), Position(0, 1), Position(1, 1), Position(2, 1)]
            }#diccionario de posiciones en la tabla
        self.move(0, 3)

        
#blocke 2
class JBlock(Block):
    def __init__(self):
        super().__init__(id = 2)
        self.cells = {
                0:[Position(0, 0), Position(1, 0), Position(1, 1), Position(1, 2)],
                1:[Position(0, 1), Position(0, 2), Position(1, 1), Position(2, 1)],
                2:[Position(1, 0), Position(1, 1), Position(1, 2), Position(2, 2)],
                3:[Position(0, 1), Position(1, 1), Position(2, 0), Position(2, 1)]
            }#diccionario de posiciones en la tabla
        self.move(0, 3)

#blocke 3
class IBlock(Block):
    def __init__(self):
        super().__init__(id = 3)
        self.cells = {
                0:[Position(1, 0), Position(1, 1), Position(1, 2), Position(1, 3)],
                1:[Position(0, 2), Position(1, 2), Position(2, 2), Position(3, 2)],
                2:[Position(2, 0), Position(2, 1), Position(2, 2), Position(2, 3)],
                3:[Position(0, 1), Position(1, 1), Position(2, 1), Position(3, 1)]
            }#diccionario de posiciones en la tabla
        self.move(0, 3)
        
        
#blocke 4
class OBlock(Block):
    def __init__(self):
        super().__init__(id = 4)
        self.cells = {
                0:[Position(0, 0), Position(0, 1), Position(1, 0), Position(1, 1)]
            }#diccionario de posiciones en la tabla
        self.move(0, 3)

        
#blocke 5
class SBlock(Block):
    def __init__(self):
        super().__init__(id = 5)
        self.cells = {
                0:[Position(0, 1), Position(0, 2), Position(1, 0), Position(1, 1)],
                1:[Position(0, 1), Position(1, 1), Position(1, 2), Position(2, 2)],
                2:[Position(1, 1), Position(1, 2), Position(2, 0), Position(2, 1)],
                3:[Position(0, 0), Position(1, 0), Position(1, 1), Position(2, 1)]
            }#diccionario de posiciones en la tabla
        self.move(0, 3)

#blocke 6
class TBlock(Block):
    def __init__(self):
        super().__init__(id = 6)
        self.cells = {
                0:[Position(0, 1), Position(1, 0), Position(1, 1), Position(1, 2)],
                1:[Position(0, 1), Position(1, 1), Position(1, 2), Position(2, 1)],
                2:[Position(1, 0), Position(1, 1), Position(1, 2), Position(2, 1)],
                3:[Position(0, 1), Position(1, 0), Position(1, 1), Position(2, 1)]
            }#diccionario de posiciones en la tabla
        self.move(0, 3)


#blocke 7
class ZBlock(Block):
    def __init__(self):
        super().__init__(id = 7)
        self.cells = {
                0:[Position(0, 0), Position(0, 1), Position(1, 1), Position(1, 2)],
                1:[Position(0, 2), Position(1, 1), Position(1, 2), Position(2, 1)],
                2:[Position(1, 0), Position(1, 1), Position(2, 1), Position(2, 2)],
                3:[Position(0, 1), Position(1, 0), Position(1, 1), Position(2, 0)]
            }#diccionario de posiciones en la tabla
        self.move(0, 3)



