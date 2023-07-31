from cell_mark import CellMark
import pygame

class Cell:
    def __init__(self, start, end, width, height):
        self.bounds = pygame.Rect(start, end, width, height)
        self.mark = CellMark.EMPTY
    
    def markCell(self, cellMark: CellMark):
        if (self.mark != CellMark.EMPTY):
            return False
        self.mark = cellMark
        return True
    
    def collidesWithPoint(self, point: list[float]):
        return self.bounds.collidesWith(point[0], point[1])
    
    def draw(self, screen, color):
        pygame.draw.rect(screen, color, self.bounds, 1)

