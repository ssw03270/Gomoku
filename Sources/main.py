import pygame
import numpy as np
# draw gomoku board
def drawBoard():
    screen.fill(BROWN)              # fill screen brown

    for i in range(15):
        pygame.draw.line(screen, BLACK, [15, i * 30 + 15], [435, i * 30 + 15], 1)    # divide boundaries
    for i in range(15):
        pygame.draw.line(screen, BLACK, [i * 30 + 15, 15], [i * 30 + 15, 435], 1)    # divide boundaries
    for i in range(3):
        for j in range(3):
            x = 2 + i * 5
            y = 2 + j * 5
            pygame.draw.circle(screen, BLACK, [x * 30 + 15, y * 30 + 15], 3)         # design board
# draw each player's stone 
def drawStone(mousePos:tuple, playerNum:int, map:list)->int:
    x = mousePos[0]                 # mouse position X
    y = mousePos[1]                 # mouse position Y

    x = round((x - 15) / 30)        # normalize mouse position X
    y = round((y - 15) / 30)        # normalize mouse position Y
    
    if map[x][y] == 0:
        if playerNum == 1:          # if player number is 1
            screen.blit(blackStone, (x * 30, y * 30))     # draw stone
            map[x][y] = playerNum   # set map as player number
            playerNum = 2           # set player number 2
        elif playerNum == 2:        # if player number is 2
            screen.blit(whiteStone, (x * 30, y * 30))     # draw stone
            map[x][y] = playerNum   # set map as player number
            playerNum = 1           # set player number 1
    
    return playerNum                # return player number

def checkGameEnd(map:list)->int:    # return 0 : no winner, return 1 : black win, return 2 : white win
    # check Horizontal
    for i in range(15):
        for j in range(15):
            straightBlackStoneCnt = 0
            straightWhiteStoneCnt = 0
            for k in range(5):
                try:
                    if map[i][j + k] == 1:
                        straightBlackStoneCnt += 1
                    elif map[i][j + k] == 2:
                        straightWhiteStoneCnt += 1
                except:
                    continue
            if straightBlackStoneCnt == 5:
                return 1
            elif straightWhiteStoneCnt == 5:
                return 2
    
    # check Vertical
    for i in range(15):
        for j in range(15):
            straightBlackStoneCnt = 0
            straightWhiteStoneCnt = 0
            for k in range(5):
                try:
                    if map[i + k][j] == 1:
                        straightBlackStoneCnt += 1
                    elif map[i + k][j] == 2:
                        straightWhiteStoneCnt += 1
                except:
                    continue
            if straightBlackStoneCnt == 5:
                return 1
            elif straightWhiteStoneCnt == 5:
                return 2

    # check Cross 1
    for i in range(15):
        for j in range(15):
            straightBlackStoneCnt = 0
            straightWhiteStoneCnt = 0
            for k in range(5):
                try:
                    if map[i + k][j + k] == 1:
                        straightBlackStoneCnt += 1
                    elif map[i + k][j + k] == 2:
                        straightWhiteStoneCnt += 1
                except:
                    continue
            if straightBlackStoneCnt == 5:
                return 1
            elif straightWhiteStoneCnt == 5:
                return 2

    # check Cross 2
    for i in range(15):
        for j in range(15):
            straightBlackStoneCnt = 0
            straightWhiteStoneCnt = 0
            for k in range(5):
                try:
                    if map[i - k][j + k] == 1:
                        straightBlackStoneCnt += 1
                    elif map[i - k][j + k] == 2:
                        straightWhiteStoneCnt += 1
                except:
                    continue
            if straightBlackStoneCnt == 5:
                return 1
            elif straightWhiteStoneCnt == 5:
                return 2
    
    return 0

# pygame start
pygame.init()

# game color
BLACK   = (  0,   0,   0)                           # color black
WHITE   = (255, 255, 255)                           # color white
BROWN   = (167, 133, 106)                           # color brown

# game image
blackStone = pygame.transform.scale(pygame.image.load(r".\Resources\BlackStone.png"), (30, 30))     # load image black stone
whiteStone = pygame.transform.scale(pygame.image.load(r".\Resources\WhiteStone.png"), (30, 30))     # load image white stone

# set display size
size = [450, 450]                                   # set pygame screen size
screen = pygame.display.set_mode(size)              # set pygame screen

# set display title
pygame.display.set_caption("Gomoku")                # set pygame title

# game value
done = False                                        # save game done
end = False                                         # save game round done
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

    if mouseDown and not end:                       # if mouse button down
        mousePos = pygame.mouse.get_pos()           # get mouse position
        playerNum = drawStone(mousePos, playerNum, map)     # draw stone at mouse position
        winner = checkGameEnd(map)                  # check winner
        if winner == 1:                             # if black win
            print("winner is black!!")
            end = True                              # set game end
        elif winner == 2:                           # if white win
            print("winnner is white!!")
            end = True                              # set game end

    mouseDown = False                               # set mouse button down false

    pygame.display.flip()                           # update game display 