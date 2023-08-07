from ai_player import AIPlayer
from cell_mark import CellMark
from game_board import GameBoard
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
    DARK_GREY = (128,128,128)
    GREY = (169,169,169)

    def __init__(self, screenSize: tuple[float], padding: tuple[float]) -> None:
        self.screenSize = screenSize
        self.padding = padding

        self.gameBoard = GameBoard(self.screenSize, self.padding)
        self.player = Player(CellMark.X)
        self.opponent = AIPlayer(CellMark.O)

        self.restartGame()

        self.infoTextRect = None
    
    def onMouseButtonPressed(self, mousePos: tuple[float]) -> None:
        x, y = mousePos
        if self.infoTextRect.collidepoint(x, y):
            self.restartGame()
            return

    def restartGame(self) -> None:
        self.gameBoard.reset()
        self.isOver = False
        self.winner = CellMark.EMPTY
        
    def nextTurn(self) -> None:
        if self.isOver:
            return

        self.getActivePlayer().doMove(self.gameBoard)
        self.checkForGameOver()

    def getActivePlayer(self) -> Player:
        lesserMark = self.gameBoard.getLesserMark()
        if (lesserMark == self.player.playerMarker):
            return self.player
        else:
            return self.opponent

    def checkForGameOver(self):
        winner = self.gameBoard.getWinner()
        isDraw = self.gameBoard.isBoardFilled() and winner == None
        if isDraw:
            self.isOver = True
        elif winner == self.player.playerMarker:
            self.winner = self.player.playerMarker
            self.isOver = True
        elif winner == self.opponent.playerMarker:
            self.winner = self.opponent.playerMarker
            self.isOver = True

    def render(self, screen, gameOverFont, infoFont) -> None:
        screen.fill(self.WHITE)
        self.gameBoard.draw(screen, self.BLACK)

        infoText = infoFont.render('Restart', True, self.BLACK)

        self.infoTextRect = infoText.get_rect()
        self.infoTextRect.center = (self.screenSize[0] / 2, self.screenSize[1] - (self.padding[1] / 2))

        # Handle the player hovering over the restart button.
        mouseX, mouseY = pygame.mouse.get_pos()
        if self.infoTextRect.collidepoint(mouseX, mouseY):
            pygame.draw.rect(screen, self.DARK_GREY, self.infoTextRect)
        else:
            pygame.draw.rect(screen, self.GREY, self.infoTextRect)

        screen.blit(infoText, self.infoTextRect)

        if (self.isOver):
            gameOverText = None
            if self.winner == CellMark.EMPTY:
                gameOverText = gameOverFont.render('Draw', True, self.BLUE)
            elif self.winner == self.player.playerMarker:
                gameOverText = gameOverFont.render('Win!', True, self.GREEN)
            else:
                gameOverText = gameOverFont.render('Lose!', True, self.RED)


            gameOverTextRect = gameOverText.get_rect()
            gameOverTextRect.center = (self.screenSize[0] / 2, self.padding[1] / 2)
            screen.blit(gameOverText, gameOverTextRect)
    
 