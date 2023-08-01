from cell_mark import CellMark
from game_board import GameBoard
import pygame

# Initialize pygame
pygame.init()

# Setup screen
size = width, height = 600, 600
screen = pygame.display.set_mode(size)

white = 255,255,255
screen.fill(white)

pygame.display.set_caption("Tic Tac Toe")

# Set up game clock
clock = pygame.time.Clock()

# Set up game board
paddingX, paddingY = 100, 100
gameBoard = GameBoard(width, height, paddingX, paddingY)

# Game definitions
black = 0,0,0
isPlayerTurn = True
isGameOver = False
done = False

# Game Loop
while not done:
    # 0. Check if quit button was pressed.
    for event in pygame.event.get():
        if event.type == pygame.QUIT: done = True

    # 1. Check if game is over
    if (isGameOver):
        continue

    # 2. Get action for active player
    changeTurns = False
    if pygame.mouse.get_pressed()[0]:
        cellMark = CellMark.X if isPlayerTurn else CellMark.O
        changeTurns = gameBoard.markCellAtPosition(pygame.mouse.get_pos(), cellMark)

    if changeTurns: isPlayerTurn = not isPlayerTurn
    
    # 3. Check game state
    winner = gameBoard.getWinner()
    isDraw = gameBoard.areAllCellsFilled() and winner == None
    if isDraw:
        print("Draw!")
        isGameOver = True
    elif winner == CellMark.X:
        print("Player Won!")
        isGameOver = True
        # TODO: Show win screen and option to restart
    elif winner == CellMark.O:
        print("Opponent Won!")
        isGameOver = True
        # TODO: Show lose screen and option to restart

    # 4. Draw Grid
    gameBoard.draw(screen, black)
    pygame.display.flip()

    # 5. Update Clock
    clock.tick(60) # limits FPS to 60

pygame.quit()