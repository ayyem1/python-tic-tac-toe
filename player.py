from cell_mark import CellMark
from game_board import GameBoard

import pygame

"""
Represents a player whose moves are controlled via user input.
"""
class Player:
    def __init__(self, playerMarker: CellMark) -> None:
        self.playerMarker = playerMarker

    def doMove(self, gameBoard: GameBoard) -> bool:
        result = False
        if pygame.mouse.get_pressed()[0]:
            result = gameBoard.markCellAtPosition(pygame.mouse.get_pos(), self.playerMarker)
        return result