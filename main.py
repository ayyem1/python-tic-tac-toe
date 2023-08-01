from cell_mark import CellMark
from game_board import GameBoard
import pygame

# Initialize pygame
pygame.init()

# Setup screen
size = width, height = 600, 600
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Tic Tac Toe")

# Set up game clock
clock = pygame.time.Clock()

# Set up game board
paddingX, paddingY = 100, 100
gameBoard = GameBoard()

# Color definitions
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)

# Game definitions
def resetGame() -> None:
    gameBoard.reset(width, height, paddingX, paddingY)
    global gameOverFont
    gameOverFont = pygame.font.Font('freesansbold.ttf', 40)

    global infoFont
    infoFont = pygame.font.Font('freesansbold.ttf', 16)

    global infoText
    infoText = infoFont.render('(Press \'r\' at any point to restart)', True, black)

    global gameOverText;
    gameOverText = None

    global isPlayerTurn
    isPlayerTurn = True

    global isGameOver
    isGameOver = False

    global done
    done = False

resetGame()

#TODO: Create AI for opponent
#TODO: Add comments to code.

# Game Loop
while not done:
    # 0. Check if quit button was pressed.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYUP and event.key == pygame.K_r:
            resetGame()

    # 1. Check if game is over
    if (isGameOver):
        continue

    # 2. Get action for active player and manage turn.
    if pygame.mouse.get_pressed()[0]:
        cellMark = CellMark.X if isPlayerTurn else CellMark.O
        if gameBoard.markCellAtPosition(pygame.mouse.get_pos(), cellMark):
            isPlayerTurn = not isPlayerTurn
    
    # 3. Check game state
    winner = gameBoard.getWinner()
    isDraw = gameBoard.areAllCellsFilled() and winner == None
    if isDraw:
        gameOverText = gameOverFont.render('Draw', True, blue)
        isGameOver = True
    elif winner == CellMark.X:
        gameOverText = gameOverFont.render('Win!', True, green)
        isGameOver = True
    elif winner == CellMark.O:
        gameOverText = gameOverFont.render('Lose!', True, red)
        isGameOver = True

    # 4. Render
    screen.fill(white)

    if (isGameOver):
        gameOverTextRect = gameOverText.get_rect()
        gameOverTextRect.center = (width / 2, paddingY / 2)
        screen.blit(gameOverText, gameOverTextRect)
    
    infoTextRect = infoText.get_rect()
    infoTextRect.center = (width / 2, height - (paddingY / 2))
    screen.blit(infoText, infoTextRect)

    gameBoard.draw(screen, black)
    pygame.display.flip()

    # 5. Update Clock
    clock.tick(60) # limits FPS to 60

pygame.quit()