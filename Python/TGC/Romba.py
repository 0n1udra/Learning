from turtle import *
from random import *
from time import sleep

speed(1)

def fence():
    up()
    forward(250)
    right(90)
    forward(250)
    down()
    for i in range(4):
        right(90)
        forward(500)
    up()
    goto(0,0)
    down()


def wonder():
    left(randrange(0,360))
    while not stay_In():
        forward(1)
        print(pos())


prox = 10
xmax = 250
xmin = -250
ymax = 250
ymin = -250
def stay_In():

    if xmax - pos()[0] < prox:
        # right wall
        return True
    if pos()[0] - xmin < prox:
        # left wall
        return True
    if ymax - pos()[1] < prox:
        # top wall
        return True
    if pos()[0] - ymin < prox:
        # bottum wall
        return True
    return False

def spiral(gap = 20):
    c_rad = gap
    while not stay_In():
        circum = 2 * 3.14159 * c_rad
        frac = 1/circum

        left(frac * 360)
        forward(1)
        c_rad += gap * frac

def fol_Wall():
    min = xmax - pos()[0]
    setheading(90)
    if pos()[0] - xmin < min:
        min = pos()[0] - xmin
        setheading(270)
    if ymax - pos()[1] < min:
        min = ymax - pos()[1]
        setheading(180)
    if pos()[1] - ymin < min:
        setheading(0)

    while not stay_In():
        forward(1)

def backup_Spiral(backup = 100, gap = 10):
    while not stay_In() and backup > 0:
        backward(1)
        backup -= 1

    spiral(gap)

def striaght():
    left(randrange(0,360))
    while not stay_In():
        forward(1)



while True:
    backward(1)

    which_Func = choice(['a,', 'b', 'c'])

    if which_Func == 'a':
        wonder()
    if which_Func == 'b':
        backup_Spiral(randrange(100,200), (randrange(10,50)))
    if which_Func == 'c':
        fol_Wall()









input("Quit > ")