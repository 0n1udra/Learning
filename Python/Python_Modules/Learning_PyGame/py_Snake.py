import pygame as pg
import DT as c
from random import randrange
from time import sleep


pg.init()

##### Settings/Config #######
windowSize = (900, 600)
# it's in a variable so the game window can change and won't screw up anything else, like the game exit on side contact
gameDisplay = pg.display.set_mode(windowSize)
# sets window size

clock = pg.time.Clock()

pg.display.set_caption('Slither')
# sets window title
pg.display.set_icon(pg.image.load('apple.png'))
# sets window icon. best size is 32x32

fps = 15  # fps
snakeSize = 20  # snake size
appleSize = 45  # apple size
movement = 20  # movement speed

# some game variables

### Images/Sprites/Color ###
snakeHead = pg.image.load('snakehead.png')
apple = pg.image.load('apple.png')


# loads up images to use as sprites

### Drawing Snake ###
def snake(sSize, sList, sHead):
    gameDisplay.blit(sHead, (sList[-1]))  # draws snake head sprite

    for i in range(len(sList[:-1])):
        pg.draw.rect(gameDisplay, c.BROWN, [sList[i][0], sList[i][1], sSize, sSize])
        # draws body of snake


### Apple ###
def rand_Apple():
    randAppleX = randrange(appleSize, windowSize[0] - appleSize)  # ,sSize)
    randAppleY = randrange(appleSize, windowSize[1] - appleSize)  # ,sSize)
    # creates a random position to put apple. (minNum, maxNum, divisibleBy)
    return randAppleX, randAppleY


### Draw Text to Screen ###
def show_Msg(msg, coords, color=c.RED, font='verdana', fSize=30, fBold=False):
    font = pg.font.SysFont(font, fSize, bold=fBold)  # sets settings for displaying text

    if coords[0] == 0:
        # checks if the x in coords is a 0
        msgCenter = font.size(msg)[0]  # finds the width of teh text
        coords = ((windowSize[0] / 2) - (msgCenter / 2), coords[1])
        # finds the middle of text, then subtracts it from the middle of screen, so it's the center

    screenText = font.render(msg, True, color)
    # creates text to render with input from msg and color
    gameDisplay.blit(screenText, [coords[0], coords[1]])
    # sets coords to put text at
    # this well not show the text ingame yet you have to do pg.display.update()


### Game Intro ###
def game_Intro():
    while True:
        show_Msg('Snake', (0, 100), c.BLUE, fSize=80)
        show_Msg('Q - Quit | SPACE - Begin', (0, 240), c.GREEN)
        pg.display.update()
        # shows messages on screen
'''
        for event in pg.event.get():  # gets input
            if event.type == pg.QUIT:
                quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_q:
                    quit()
                if event.key == pg.K_SPACE:
                    for i in reversed(range(1, 6)):
                        gameDisplay.fill(c.BLACK)
                        show_Msg(str(i), (0, 200), c.RED)
                        pg.display.update()
                        sleep(1)
                    # countdown to begin game.
                    break
'''

### Game Over ###
def game_Over(score):
    while True:
        show_Msg('GAME OVER', (0, 250), fSize=80)  # gives text, color, and position to put it at
        show_Msg('C - Continue | Q - Quit', (0, 340))  # 0 for x if you want it to be centered
        show_Msg('SCORE: {}'.format(score), (0, 380))
        # prints stuff out to screen in red
        pg.display.update()

        for event in pg.event.get():  # gets key event
            if event.type == pg.QUIT:
                quit()
            # the makes it so you can press q or the close window button to quit
            if event.type == pg.KEYDOWN:
                # checks if event is a keydown event(press key)
                if event.key == pg.K_q:
                    quit()
                # checks if it's q to stop the game
                elif event.key == pg.K_c:
                    game_Loop()
            # if c continues game
            else:
                print("Error | Q/C")

### Pause Game ###
def pause_Game(score):
    while True:
        show_Msg('PASUED', (0, 250), fSize=60)  # gives text, color, and position to put it at
        pg.display.update()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_q:
                    quit()
                elif event.key == pg.K_c:
                    return
                # if c continues game, stops all loops and returns nothing
                else:
                    print("Error | Q/C")


##### Main Game Loop ################
def game_Loop():
    global snakeHead

    ### Config ###
    leadX = windowSize[0] / 2
    leadY = windowSize[1] / 2
    # sets position of snake
    leadX_Change = 0
    leadY_Change = -movement
    sHead = snakeHead
    # sets change in direction. leadY_Change is -sSize so the game starts with it moving up

    sList = []  # list of positions for snake parts
    sLength = 0  # sets the length of the snake. sets score
    score = 0

    randAppleX, randAppleY = rand_Apple()

    ### Hitting the Apple ###

    # this is when you hit an apple. Respawns apple, adds to snake, add 1 to score

    while True:
        # while False game keeps running

        for event in pg.event.get():
            # gets events going on(any interaction with window)
            if event.type == pg.QUIT:
                quit()
            ### Movement ###
            elif event.type == pg.KEYDOWN:
                # checks if the current event is a KEYDOWN event

                if event.key == pg.K_SPACE:
                    pause_Game(score)
                elif event.key == pg.K_LEFT:  # checks for what key it was
                    leadX_Change = leadY_Change = 0  # clears current movement
                    sHead = pg.transform.rotate(snakeHead, 90)  # rotates the snake
                    leadX_Change -= movement  # move snake
                elif event.key == pg.K_RIGHT:
                    leadX_Change = leadY_Change = 0
                    sHead = pg.transform.rotate(snakeHead, 270)
                    leadX_Change += movement
                elif event.key == pg.K_UP:
                    leadX_Change = leadY_Change = 0
                    sHead = pg.transform.rotate(snakeHead, 0)
                    leadY_Change -= movement
                elif event.key == pg.K_DOWN:
                    leadX_Change = leadY_Change = 0
                    sHead = pg.transform.rotate(snakeHead, 180)
                    leadY_Change += movement

        gameDisplay.fill(c.BLACK)  # sets background color
        # this is down here so that when you pause you can see where you are and everything

        show_Msg(msg=str(score), fSize=20, coords=(0, 10))
        # shows score on screen

        leadX += leadX_Change
        leadY += leadY_Change
        # moves snake according to what you pressed

        ### Border ###
        if (leadX > windowSize[0]):
            leadX = 0
        elif (leadX < 0):
            leadX = windowSize[0]
        elif (leadY > windowSize[1]):
            leadY = 0
        elif (leadY < 0):
            leadY = windowSize[1]
        # you can now go through a wall to go on the other side, Ex. go through right wall to come out of left wall

        print(leadX, leadY)

        ### Apple Boundary ###
        if (leadX > randAppleX) and (leadX < randAppleX + appleSize) or \
                        (leadX + snakeSize > randAppleX) and (leadX + snakeSize < randAppleX + appleSize):
            # checks if you are in the X boundary
            if (leadY > randAppleY) and (leadY < randAppleY + appleSize) or \
                            (leadY + snakeSize > randAppleY) and (leadY + snakeSize < randAppleY + appleSize):
                # checks Y boundary
                randAppleX, randAppleY = rand_Apple()  # hits apple
                score += 1
                sLength += 1

        ### Snake ###
        sHeadList = []  # snake head position
        sHeadList.extend((leadX, leadY))  # adds current snake head position to sHead
        sList.append(sHeadList)  # adds to sList (snakeList)
        snake(snakeSize, sList, sHead)  # calls function to draw snake

        for segment in sList[:-1]:
            if sHeadList == segment: game_Over(score)
        # checks if you moved into a position where your snake body already is in it'll stop game

        if len(sList) > sLength:
            del sList[0]
            # makes sure snake length is the same as how many apples you picked up
            # this basically makes sure your snake isn't always growing when moving

        ### Draw Apple ###
        gameDisplay.blit(apple, [randAppleX, randAppleY])

        pg.display.update()
        # updates display. you need this if you want any animation or things to happen

        clock.tick(fps)  # goes to next frame

    pg.quit()
    quit()
    # quits pygame and quits script


game_Intro()
#####
'''
What is going on
~ Init pygame
~ Set Display size

'''
