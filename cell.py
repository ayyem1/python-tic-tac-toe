from cell_mark import CellMark
import pygame

class Cell:
    def __init__(self, start, end, width, height) -> None:
        self.bounds = pygame.Rect(start, end, width, height)
        self.marker = CellMark.EMPTY
    
    def isMarkEmpty(self) -> bool:
        return self.marker == CellMark.EMPTY
    
    def mark(self, cellMark: CellMark) -> bool:
        if not self.isMarkEmpty():
            return False
        self.marker = cellMark
        return True
    
    def collidesWithPoint(self, point: tuple[float]) -> bool:
        return self.bounds.collidepoint(point[0], point[1])
    
    def draw(self, screen, color: tuple[int]) -> None:
        if self.marker == CellMark.X:
            self.drawX(screen, color)
        elif self.marker == CellMark.O:
            self.drawO(screen, color)
    
    def drawX(self, screen, color: tuple[int]) -> None:
        pygame.draw.aaline(screen, color, self.bounds.topleft, self.bounds.bottomright)
        pygame.draw.aaline(screen, color, self.bounds.topright, self.bounds.bottomleft)
        return
    
    def drawO(self, screen, color: tuple[int]) -> None:
        pygame.draw.circle(screen, color, self.bounds.center, self.bounds.width / 2, 1)
        return
    

