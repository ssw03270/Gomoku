import pygame
import numpy as np
# draw gomoku board
def drawBoard():
    screen.fill(BROWN)              # fill screen brown

    for i in range(15):
        pygame.draw.line(screen, BLACK, [15, i * 30 + 15], [435, i * 30 + 15], 1)    # divide boundaries
    for i in range(15):                                                             #    
        pygame.draw.line(screen, BLACK, [i * 30 + 15, 15], [i * 30 + 15, 435], 1)    # divide boundaries
    for i in range(3):
        for j in range(3):
            x = 2 + i * 5
            y = 2 + j * 5
            pygame.draw.circle(screen, BLACK, [x * 30 + 15, y * 30 + 15], 3)                # design board
# draw each player's stone 
def drawStone(mousePos:tuple, playerNum:int, map:list)->int:
    x = mousePos[0]                 # mouse position X
    y = mousePos[1]                 # mouse position Y

    x = round((x - 15) / 30)        # normalize mouse position X
    y = round((y - 15) / 30)        # normalize mouse position Y
    
    if map[x][y] == 0:
        if playerNum == 1:          # if player number is 1
            pygame.draw.circle(screen, BLACK, [x * 30 + 15, y * 30 + 15], 15)   # draw stone
            map[x][y] = playerNum   # set map as player number
            playerNum = 2           # set player number 2
        elif playerNum == 2:        # if player number is 2
            pygame.draw.circle(screen, WHITE, [x * 30 + 15, y * 30 + 15], 15)   # draw stone
            map[x][y] = playerNum   # set map as player number
            playerNum = 1           # set player number 1
    
    return playerNum                # return player number

# pygame start
pygame.init()

# game color
BLACK   = (  0,   0,   0)                           # color black
WHITE   = (255, 255, 255)                           # color white
BROWN   = (167, 133, 106)                           # color brown

# set display size
size = [450, 450]                                   # set pygame screen size
screen = pygame.display.set_mode(size)              # set pygame screen

# set display title
pygame.display.set_caption("Gomoku")                # set pygame title

# game value
done = False                                        # save game done
mouseDown = False                                   # save mouse button down

playerNum = 1                                       # save player number

map = np.zeros((15, 15))                            # save map information
clock = pygame.time.Clock()                         # save pygame clock

# drawing gomoku board
drawBoard()

while not done:
    clock.tick(10)                                  # set pygame fps

    for event in pygame.event.get():                # list of pygame event
        if event.type == pygame.QUIT:               # if quit game
            done = True                             # quit game
        if event.type == pygame.MOUSEBUTTONDOWN:    # if mouse button down
            mouseDown = True                        # set mouse button down true

    if mouseDown:                                   # if mouse button down
        mousePos = pygame.mouse.get_pos()           # get mouse position
        playerNum = drawStone(mousePos, playerNum, map)     # draw stone at mouse position

    mouseDown = False                               # set mouse button down false

    pygame.display.flip()                           # update game display 