from ai_player import AIPlayer
from cell_mark import CellMark
from game_board import GameBoard
from idrawable import IDrawable
from player import Player

import pygame

"""
Represents a game of tic tac toe. 
Handles managing player turns and capturing user input to update game state.
"""
class Game:
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)

    SCREENSIZE = (600, 600)
    PADDING = (100, 100)

    def __init__(self) -> None:
        pygame.init()

        self.screen = pygame.display.set_mode(self.SCREENSIZE)
        pygame.display.set_caption("Tic Tac Toe")

        self.gameOverFont = pygame.font.Font('freesansbold.ttf', 40)
        self.gameOverText = None

        self.infoFont = pygame.font.Font('freesansbold.ttf', 16)
        self.infoText = self.infoFont.render('(Press \'r\' at any point to restart)', True, self.BLACK)

        self.gameBoard = GameBoard()
        self.player = Player(CellMark.X)
        self.opponent = AIPlayer(CellMark.O)

        self.resetGame()

    def getActivePlayer(self) -> Player:
        playerMarkerCount = len(self.gameBoard.getAllCellsWithMark(self.player.playerMarker))
        opponentMarkerCount = len(self.gameBoard.getAllCellsWithMark(self.opponent.playerMarker))
        if playerMarkerCount > opponentMarkerCount:
            return self.opponent
        else:
            return self.player
    
    def nextTurn(self) -> None:
        if self.isOver: return
        self.getActivePlayer().doMove(self.gameBoard)
        self.checkForGameOver()

    def checkForGameOver(self):
        winner = self.gameBoard.getWinner()
        isDraw = self.gameBoard.isBoardFilled() and winner == None
        if isDraw:
            self.gameOverText = self.gameOverFont.render('Draw', True, self.BLUE)
            self.isOver = True
        elif winner == self.player.playerMarker:
            self.gameOverText = self.gameOverFont.render('Win!', True, self.GREEN)
            self.isOver = True
        elif winner == self.opponent.playerMarker:
            self.gameOverText = self.gameOverFont.render('Lose!', True, self.RED)
            self.isOver = True
    
        
    def resetGame(self) -> None:
        self.gameBoard.reset(self.SCREENSIZE[0], self.SCREENSIZE[1], self.PADDING[0], self.PADDING[1])
        self.gameOverText = None
        self.isOver = False

    def render(self) -> None:
        self.screen.fill(self.WHITE)
        self.gameBoard.draw(self.screen, self.BLACK)

        infoTextRect = self.infoText.get_rect()
        infoTextRect.center = (self.SCREENSIZE[0] / 2, self.SCREENSIZE[1] - (self.PADDING[1] / 2))
        self.screen.blit(self.infoText, infoTextRect)

        if (self.isOver):
            gameOverTextRect = self.gameOverText.get_rect()
            gameOverTextRect.center = (self.SCREENSIZE[0] / 2, self.PADDING[1] / 2)
            self.screen.blit(self.gameOverText, gameOverTextRect)
    
 