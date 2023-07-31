from cell import Cell
from cell_mark import CellMark
import pygame

# Initialize pygame
pygame.init()

# Setup screen
size = width, height = 600, 600
paddingX, paddingY = 100, 100
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Tic Tac Toe")

# Game definitions
white = 255,255,255
black = 0,0,0
# Set up the game board rect using the screen size and padding definitions.
gameBoard = []
cellSize = ((width - (2 * paddingX)) / 3, (height - (2 * paddingY)) / 3)
for x in range(3):
    for y in range(3):
        gameBoard.append(Cell(paddingX + (x * cellSize[0]), paddingY + (y * cellSize[1]), cellSize[0], cellSize[1]));

isPlayerTurn = True
done = False

# Function definitions
def getCellForPosition(point: list[float]):
    for cell in gameBoard:
        if cell.collidesWith(point):
            return cell;
    return None

# Game Loop
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if isPlayerTurn and pygame.mouse.get_pressed()[0]:
                clickedCell = getCellForPosition(pygame.mouse.get_pos());
                if (clickedCell != None):
                    success = clickedCell.markCell(CellMark.X)
                    if success: isPlayerTurn = False

    screen.fill(white)
    # 1. Draw Grid
    for cell in gameBoard:
        #TODO: Need to fix overdraw issues.
        cell.draw(screen, black)

    # 2. Determine turn
    if (not isPlayerTurn):
        # TODO: Process AI action.
        isPlayerTurn = True;
    
    # 4. Check if game is over.
    #    4a. If won, show win screen and option to restart
    #    4b. If lost, show lose screen and option to restart
    #    4c. If neither, keep playing.
    pygame.display.flip()

pygame.quit()