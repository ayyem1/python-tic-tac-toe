from game import Game
import pygame

# Create new game instance
game = Game()

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

    game.render()

    pygame.display.flip()

    # Limit FPS to 60
    clock.tick(60)

pygame.quit()