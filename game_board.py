from cell import Cell
from cell_mark import CellMark
from idrawable import IDrawable

import pygame

"""
Represents the state of the game and has logic to render its state.
"""
class GameBoard(IDrawable):
    # NOTE: The game enforces equality of number of rows and columns.
    DIMENSION = 3

    def reset(self, width: float, height: float, paddingX: float, paddingY: float) -> None:
        self.cells = []
        cellSize = ((width - (2 * paddingX)) / self.DIMENSION, (height - (2 * paddingY)) / self.DIMENSION)
        for x in range(self.DIMENSION):
            for y in range(self.DIMENSION): 
                self.cells.append(Cell(paddingX + (x * cellSize[0]), paddingY + (y * cellSize[1]), cellSize[0], cellSize[1]));
    
    def markCellAtPosition(self, position: tuple[float], marker: CellMark) -> bool:
        for cell in self.cells:
            if cell.bounds.collidepoint(position[0], position[1]):
                return self.markCell(cell, marker)
        return False
    
    def markCell(self, cellToMark: Cell, marker: CellMark) -> bool:
        return cellToMark.mark(marker)
    
    # NOTE: This is not as efficient as hard-coding the 8 checks for a 3x3
    # tic-tac-toe game, but it allows us the flexibility to have an NxN
    # tic-tac-toe game 
    def getWinner(self) -> CellMark:
        # Check Columns
        for i in range(self.DIMENSION):
            columnIndices = range(i * self.DIMENSION, (i * self.DIMENSION) + self.DIMENSION)
            targetMarker = self.cells[columnIndices[0]].marker
            if targetMarker != CellMark.EMPTY and self.areCellsMatching(columnIndices):
                return targetMarker

        # Check Rows
        for j in range(self.DIMENSION):
            rowIndices = list(filter(lambda index: index % self.DIMENSION == j, range(j, j + self.DIMENSION * self.DIMENSION)))
            targetMarker = self.cells[rowIndices[0]].marker
            if targetMarker != CellMark.EMPTY and self.areCellsMatching(rowIndices):
                return targetMarker

        firstDiagonalIndices = list(map(lambda index: index + index * self.DIMENSION, range(self.DIMENSION)))
        targetMarker = self.cells[firstDiagonalIndices[0]].marker
        if targetMarker != CellMark.EMPTY and self.areCellsMatching(firstDiagonalIndices):
            return targetMarker
        
        secondDiagonalIndices = range(self.DIMENSION - 1, self.DIMENSION * (self.DIMENSION - 1) + 1, self.DIMENSION - 1)
        targetMarker = self.cells[secondDiagonalIndices[0]].marker
        if targetMarker != CellMark.EMPTY and self.areCellsMatching(secondDiagonalIndices):
            return targetMarker
            
        return None
    
    def areCellsMatching(self, cellIndices: list[int]) -> bool:
        marker = self.cells[cellIndices[0]].marker
        for cellIndex in cellIndices:
            if self.cells[cellIndex].marker != marker:
                return False
        
        return True
    
    def isBoardFilled(self) -> bool:
        return len(self.getAllCellsWithMark(CellMark.EMPTY)) == 0
    
    def getAllCellsWithMark(self, marker: CellMark) -> list[Cell]:
        return list(filter(lambda cell: cell.marker == marker, self.cells))
    
    # IDrawable implementation
    def draw(self, screen, color: tuple[int]) -> None:
        # Draw vertical lines for board
        for c in range(self.DIMENSION - 1):
            pygame.draw.aaline(screen, color, self.cells[c * self.DIMENSION].bounds.topright, self.cells[(c * self.DIMENSION) + (self.DIMENSION - 1)].bounds.bottomright, 1)

        # Draw horizontal lines for board
        for r in range(self.DIMENSION - 1):
            pygame.draw.aaline(screen, color, self.cells[r].bounds.bottomleft, self.cells[r + self.DIMENSION * (self.DIMENSION - 1)].bounds.bottomright, 1)

        # Draw each cell's marker, if it exists.
        for cell in self.cells:
            cell.draw(screen, color)