from cell_mark import CellMark
from game_board import GameBoard

import pygame

class Player:
    def __init__(self, playerMarker: CellMark) -> None:
        self.playerMarker = playerMarker

    def doMove(self, gameBoard: GameBoard) -> bool:
        result = False
        if pygame.mouse.get_pressed()[0]:
            clickedCell = gameBoard.getCellForPosition(pygame.mouse.get_pos())
            if (clickedCell != None):
                result = clickedCell.mark(self.playerMarker)
        return result