from cell_mark import CellMark
import pygame

class Cell:
    def __init__(self, start, end, width, height):
        self.bounds = pygame.Rect(start, end, width, height)
        self.mark = CellMark.EMPTY
    
    def markCell(self, cellMark: CellMark):
        if self.mark != CellMark.EMPTY:
            return False
        self.mark = cellMark
        return True
    
    def collidesWithPoint(self, point: list[float]):
        return self.bounds.collidepoint(point[0], point[1])
    
    def draw(self, screen, color):
        # TODO: Fix over draw.
        pygame.draw.rect(screen, color, self.bounds, 1)
        if self.mark == CellMark.X:
            self.drawX(screen, color)
        elif self.mark == CellMark.O:
            self.drawO(screen, color)
    
    def drawX(self, screen, color):
        pygame.draw.aaline(screen, color, self.bounds.topleft, self.bounds.bottomright)
        pygame.draw.aaline(screen, color, self.bounds.topright, self.bounds.bottomleft)
        return
    
    def drawO(self, screen, color):
        pygame.draw.circle(screen, color, self.bounds.center, self.bounds.width / 2, 1)
        return
    

