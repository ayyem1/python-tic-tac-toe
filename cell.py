from cell_mark import CellMark
from idrawable import IDrawable

import pygame

"""
Represents a single cell on the game board and has logic to render its state.
"""
class Cell(IDrawable):
    # The amount of padding between the border of the cell and drawing of the marker (X or O)
    RENDER_PADDING = 5

    def __init__(self, start, end, width, height) -> None:
        self.bounds = pygame.Rect(start, end, width, height)
        self.renderBounds = pygame.Rect(start + self.RENDER_PADDING, end + self.RENDER_PADDING, width - (self.RENDER_PADDING * 2), height - (self.RENDER_PADDING * 2))
        self.marker = CellMark.EMPTY
    
    """
    @returns True if this cell has yet to be marked.
    """
    def isMarkEmpty(self) -> bool:
        return self.marker == CellMark.EMPTY
    
    """
    Marks this cell with the given marker.
    @returns True if this cell was marked successfully.
    """
    def mark(self, cellMark: CellMark) -> bool:
        if not self.isMarkEmpty():
            return False
        self.marker = cellMark
        return True
    
    #region IDrawable implementation

    """
    Draws the current state of this cell to the screen. The shapes will be drawn using the given color.
    """
    def draw(self, screen, color: tuple[int]) -> None:
        if self.marker == CellMark.X:
            self.drawX(screen, color)
        elif self.marker == CellMark.O:
            self.drawO(screen, color)
    
    """
    Utility to draw an X on the screen.
    """
    def drawX(self, screen, color: tuple[int]) -> None:
        pygame.draw.aaline(screen, color, self.renderBounds.topleft, self.renderBounds.bottomright)
        pygame.draw.aaline(screen, color, self.renderBounds.topright, self.renderBounds.bottomleft)
        return
    
    """
    Utility to draw an O on the screen.
    """
    def drawO(self, screen, color: tuple[int]) -> None:
        pygame.draw.circle(screen, color, self.renderBounds.center, self.renderBounds.width / 2, 1)
        return
    
    #endregion
