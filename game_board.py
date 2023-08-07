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
    
    """
    Overridden toString to easily debug the GameBoard in terminal.
    """
    def __str__(self) -> str:
        result = ""
        for i in range(self.DIMENSION):
            for j in range(self.DIMENSION):
                result += f'{self.cells[i + j * self.DIMENSION].marker} '
            result += '\n'
        return result
    
    def __init__(self, size: tuple[float], padding: tuple[float]) -> None:
        self.cells = []
        self.gridSize = size
        self.padding = padding

    """
    Resets the game board by recreated the cells that compose the grid.
    """
    def reset(self) -> None:
        self.cells.clear()
        cellSize = ((self.gridSize[0] - (2 * self.padding[0])) / self.DIMENSION, (self.gridSize[1] - (2 * self.padding[1])) / self.DIMENSION)
        for x in range(self.DIMENSION):
            for y in range(self.DIMENSION): 
                self.cells.append(Cell(self.padding[0] + (x * cellSize[0]), self.padding[1] + (y * cellSize[1]), cellSize[0], cellSize[1]));
    
    """
    Utility function that determines which cell the user clicked on based on the position of their click and marks that cell.
    @returns bool True if the cell was successfully marked.
    """
    def markCellThatCollidesWithPoint(self, position: tuple[float], marker: CellMark) -> bool:
        for cell in self.cells:
            if cell.bounds.collidepoint(position[0], position[1]):
                return cell.mark(marker)
        return False
    
    """
    Utility function that attempts to mark a cell at the given index.
    @returns bool True if the cell was successfully marked.
    """
    def markCellAtIndex(self, index: int, marker: CellMark) -> bool:
        if index < 0 or index > len(self.cells):
            return False
        return self.cells[index].mark(marker)
    
    """
    Determines the winner of the game, if one exists, based on the current state of the game board.

    NOTE: This is not as efficient as hard-coding the 8 checks for a 3x3
    tic-tac-toe game, but it allows us the flexibility to have an NxN
    tic-tac-toe game 

    @returns CellMark The marker that corresponds to who won. If there is no winner, None is returned.
    """
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
    
    """
    Helper function that determines if a group of cells, specified by their indices, are all marked with the same marker.
    @returns bool True if the cells are marked with the same marker.
    """
    def areCellsMatching(self, cellIndices: list[int]) -> bool:
        marker = self.cells[cellIndices[0]].marker
        for cellIndex in cellIndices:
            if self.cells[cellIndex].marker != marker:
                return False
        
        return True
    
    """
    Helper function that determines if all cells on the board have been marked with something other than CellMark.EMPTY.
    @returns bool True if all cells have been marked with something other than CellMark.EMPTY.
    """
    def isBoardFilled(self) -> bool:
        return len(self.getAvailableGridIndices()) == 0
    
    """
    @returns Either CellMark.X or CellMark.O depending on which has fewer instances on the board
    """
    def getLesserMark(self) -> CellMark:
        XMarkerCount = len(self.getAllCellsWithMark(CellMark.X))
        OMarkerCount = len(self.getAllCellsWithMark(CellMark.O))
        if XMarkerCount > OMarkerCount:
            return CellMark.O
        else:
            return CellMark.X
        
    """
    @returns A list of all cells that are marked with the given marker.
    """
    def getAllCellsWithMark(self, marker: CellMark) -> list[Cell]:
        return list(filter(lambda cell: cell.marker == marker, self.cells))
    
    def getAvailableGridIndices(self) -> list[int]:
        return list(filter(lambda cellIndex: self.cells[cellIndex].isMarkEmpty(), range(len(self.cells))))
    
    #region IDrawable implementation
    """
    Draws the current state of this game board to the screen. Lines will be drawn in the given color.
    """
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
    
    #endregion