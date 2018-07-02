import pygame as pg
import random as rd
import DT

pg.init()

windowSize = 800, 600
gameDisplay = pg.display.set_mode(windowSize)
clock = pg.time.Clock()


##### Draw Text to Screen #########
def show_Msg(msg='', coords=(), color=DT.RED, font='verdana', fSize=30, fBold=False):
    font = pg.font.SysFont(font, fSize, bold=fBold)  # sets settings for displaying text
    if coords[0] == 0:
        msgCenter = font.size(msg)[0]  # finds the width of teh text
        coords = ((windowSize[0]/2) - (msgCenter/2), coords[1])
    screenText = font.render(msg, True, color)
    gameDisplay.blit(screenText, [coords[0], coords[1]])

def game_Loop(): pass



game_Loop()













