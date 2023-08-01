from cell_mark import CellMark
from game_board import GameBoard
from player import Player


class AIPlayer(Player):
    def doMove(self, gameBoard: GameBoard) -> bool:
        availableMoves = gameBoard.getCellsWithMark(CellMark.EMPTY)
        if len(availableMoves) == 0:
            return False
        
        return availableMoves[0].mark(self.playerMarker)