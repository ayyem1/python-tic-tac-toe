import sys, pygame

pygame.init()

size = width, height = 640, 480
white = 255,255,255
black = 0, 0, 0

screen = pygame.display.set_mode(size)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    screen.fill(white)
    # 1. Draw Grid
    # 2. Determine turn
    # 3. Wait for valid action
    # 4. Check if game is over.
    #    4a. If won, show win screen and option to restart
    #    4b. If lost, show lose screen and option to restart
    #    4c. If neither, keep playing.
    pygame.display.flip()