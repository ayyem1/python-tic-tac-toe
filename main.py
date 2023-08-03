from game import Game
import pygame

# Init pygame
pygame.init()

# Setup screen
SCREENSIZE = (600, 600)
PADDING = (100, 100)
screen = pygame.display.set_mode(SCREENSIZE)
pygame.display.set_caption("Tic Tac Toe")

# Create Fonts
infoFont = pygame.font.Font('freesansbold.ttf', 16)
gameOverFont = pygame.font.Font('freesansbold.ttf', 40)

# Create new game instance
game = Game(SCREENSIZE, PADDING)

# Set up game clock
clock = pygame.time.Clock()

done = False
# Game Loop
while not done:
    # Handle user input for quitting and refreshing game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYUP and event.key == pygame.K_r:
            game.resetGame()

    game.nextTurn()

    game.render(screen, gameOverFont, infoFont)

    pygame.display.flip()

    # Limit FPS to 60
    clock.tick(60)

pygame.quit()