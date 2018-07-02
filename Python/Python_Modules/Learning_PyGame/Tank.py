import pygame as pg
import random as rd
import time as t
import DT

pg.init()

##### Settings/Config #######
windowSize = 900, 600
gameDisplay = pg.display.set_mode(windowSize)  # window size

clock = pg.time.Clock()

pg.display.set_caption('Tank')  # window name


fps = 20

tSize = 20
def tank(leadX, leadY, Size=20):
    pg.draw.rect(gameDisplay, DT.BROWN, [leadX, leadY, Size, Size])

def shoot(leadX, leadY, pSize=5):
    while not (leadY > windowSize[1]):
        leadY += 5
        pg.draw.rect(gameDisplay, DT.BLUE, [leadX, leadY, pSize, pSize])


def game_Loop():
    changeX = changeY = 0
    leadX, leadY = 50, 50
    while True:
        gameDisplay.fill(DT.BLACK)
        for event in pg.event.get():
            if event.type == pg.QUIT: quit()

            if event.type == pg.KEYDOWN:
                if (event.key == pg.K_RIGHT):
                    changeX += 10
                elif (event.key == pg.K_LEFT):
                    changeX -= 10
                elif (event.key == pg.K_UP):
                    changeY -= 10
                elif (event.key == pg.K_DOWN):
                    changeY += 10

                if event.key == pg.K_SPACE:
                    shoot(leadX, leadY)

            if event.type == pg.KEYUP:
                if (event.key == pg.K_RIGHT) or (event.key == pg.K_LEFT)\
                 or (event.key == pg.K_UP) or (event.key == pg.K_DOWN):
                    changeX = changeY = 0



            if (leadX <= 0): leadX = 0
            if (leadX + 10 >= windowSize[0]): leadX = windowSize[0] - tSize
            if (leadY <= 0): leadY = 0
            if (leadY + 10 >= windowSize[1]): leadY = windowSize[1] - tSize

        leadX += changeX
        leadY += changeY
        tank(leadX, leadY, tSize)




        pg.display.update()  # update display

        clock.tick(fps)  # goes to next frame

    pg.quit()
    quit()

game_Loop()

