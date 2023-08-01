from cell import Cell
from cell_mark import CellMark

import pygame

class GameBoard:
    def __init__(self, width: float, height: float, paddingX: float, paddingY: float) -> None:
        self.cells = []
        cellSize = ((width - (2 * paddingX)) / 3, (height - (2 * paddingY)) / 3)
        for x in range(3):
            for y in range(3):
                self.cells.append(Cell(paddingX + (x * cellSize[0]), paddingY + (y * cellSize[1]), cellSize[0], cellSize[1]));
    
    def markCellAtPosition(self, position: tuple[float], cellMark: CellMark) -> bool:
            success = False
            clickedCell = self.getCellForPosition(position);
            if (clickedCell != None):
                success = clickedCell.markCell(cellMark)
            
            return success
    
    def getCellForPosition(self, point: tuple[float]) -> Cell:
        for cell in self.cells:
            if cell.collidesWithPoint(point): return cell
        return None
    
    def draw(self, screen, color: tuple[int]) -> None:
        for cell in self.cells:
            # TODO: Fix over draw.
            pygame.draw.rect(screen, color, cell.bounds, 1)
            cell.draw(screen, color)
    
    def getWinner(self) -> CellMark:
        # Check Rows
        if (self.cells[0].mark == self.cells[1].mark and self.cells[0].mark == self.cells[2].mark):
            return self.cells[0].mark
        elif (self.cells[3].mark == self.cells[4].mark and self.cells[3].mark == self.cells[5].mark):
            return self.cells[3].mark
        elif (self.cells[6].mark == self.cells[7].mark and self.cells[6].mark == self.cells[8].mark):
            return self.cells[6].mark
        # Check Columns
        elif (self.cells[0].mark == self.cells[3].mark and self.cells[0].mark == self.cells[6].mark):
            return self.cells[0].mark
        elif (self.cells[1].mark == self.cells[4].mark and self.cells[1].mark == self.cells[7].mark):
            return self.cells[1].mark
        elif (self.cells[2].mark == self.cells[5].mark and self.cells[2].mark == self.cells[8].mark):
            return self.cells[2].mark
        # Check Diagonals
        elif (self.cells[0].mark == self.cells[4].mark and self.cells[0].mark == self.cells[8].mark):
            return self.cells[0].mark
        elif (self.cells[2].mark == self.cells[4].mark and self.cells[2].mark  == self.cells[6].mark):
            return self.cells[2].mark
    
    def areAllCellsFilled(self) -> bool:
        for cell in self.cells:
            if (cell.isMarkEmpty()):
                return False