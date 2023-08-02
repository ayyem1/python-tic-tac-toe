import copy
from cell import Cell
from cell_mark import CellMark
from game_board import GameBoard
from player import Player

"""
Represents a player whose moves are controlled via a decision tree.
"""
class AIPlayer(Player):
    def doMove(self, gameBoard: GameBoard) -> bool:
        availableMoves = gameBoard.getAllCellsWithMark(CellMark.EMPTY)
        if len(availableMoves) == 0:
            return False
        
        return gameBoard.markCell(availableMoves[0], self.playerMarker)
    
    # def minmax(self, gameBoard: GameBoard) -> Cell:
    #     availableCells = gameBoard.getAllCellsWithMark(CellMark.EMPTY)
    #     for cell in availableCells:
    #         simulatedBoard = self.simulateMove(gameBoard, cell)
    #     return None
    
    # def simulateMove(self, gameBoard: GameBoard, cellToMark: Cell):
    #     copiedBoard = copy.deepcopy(gameBoard) # Deep copy of gameBoard.
