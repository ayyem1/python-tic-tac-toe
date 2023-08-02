from cell import Cell
from cell_mark import CellMark
from idrawable import IDrawable

import pygame

"""
Represents the state of the game and has logic to render its state.
"""
class GameBoard(IDrawable):
    NUM_ROWS = 3
    NUM_COLUMNS = 3
         
    def reset(self, width: float, height: float, paddingX: float, paddingY: float) -> None:
        self.cells = []
        cellSize = ((width - (2 * paddingX)) / self.NUM_COLUMNS, (height - (2 * paddingY)) / self.NUM_ROWS)
        for x in range(self.NUM_COLUMNS):
            for y in range(self.NUM_ROWS): 
                self.cells.append(Cell(paddingX + (x * cellSize[0]), paddingY + (y * cellSize[1]), cellSize[0], cellSize[1]));
    
    def markCellAtPosition(self, position: tuple[float], marker: CellMark) -> bool:
        for cell in self.cells:
            if cell.bounds.collidepoint(position[0], position[1]):
                return self.markCell(cell, marker)
        return False
    
    def markCell(self, cellToMark: Cell, marker: CellMark) -> bool:
        return cellToMark.mark(marker)
    
    # TODO: Make this generic
    def getWinner(self) -> CellMark:
        # Check Columns
        if self.cells[0].marker == self.cells[1].marker == self.cells[2].marker:
            return self.cells[0].marker
        elif self.cells[3].marker == self.cells[4].marker == self.cells[5].marker:
            return self.cells[3].marker
        elif self.cells[6].marker == self.cells[7].marker == self.cells[8].marker:
            return self.cells[6].marker
        # Check Rows
        elif self.cells[0].marker == self.cells[3].marker == self.cells[6].marker:
            return self.cells[0].marker
        elif self.cells[1].marker == self.cells[4].marker == self.cells[7].marker:
            return self.cells[1].marker
        elif self.cells[2].marker == self.cells[5].marker == self.cells[8].marker:
            return self.cells[2].marker
        # Check Diagonals
        elif self.cells[0].marker == self.cells[4].marker == self.cells[8].marker:
            return self.cells[0].marker
        elif self.cells[2].marker == self.cells[4].marker == self.cells[6].marker:
            return self.cells[2].marker
    
    def isBoardFilled(self) -> bool:
        return len(self.getAllCellsWithMark(CellMark.EMPTY)) == 0
    
    def getAllCellsWithMark(self, marker: CellMark) -> list[Cell]:
        return list(filter(lambda cell: cell.marker == marker, self.cells))
    
    # IDrawable implementation
    def draw(self, screen, color: tuple[int]) -> None:
        # Draw vertical lines for board
        for c in range(self.NUM_COLUMNS - 1):
            pygame.draw.aaline(screen, color, self.cells[c * self.NUM_ROWS].bounds.topright, self.cells[(c * self.NUM_ROWS) + (self.NUM_ROWS - 1)].bounds.bottomright, 1)

        # Draw horizontal lines for board
        for r in range(self.NUM_ROWS - 1):
            pygame.draw.aaline(screen, color, self.cells[r].bounds.bottomleft, self.cells[r + self.NUM_ROWS * (self.NUM_COLUMNS - 1)].bounds.bottomright, 1)

        # Draw each cell's marker, if it exists.
        for cell in self.cells:
            cell.draw(screen, color)