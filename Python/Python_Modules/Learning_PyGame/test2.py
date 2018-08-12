#!/usr/bin/env python
# Drake Thoams
# 8/5/2018

import pygame as pg
from random import randrange as rd
from time import sleep

WHITE = 255, 255, 255
BLACK = 0, 0, 0
RED = 255, 0, 0
GREEN = 0, 255, 0
BLUE = 0, 0, 255
BROWN = 153, 102, 51

pg.init()

# sets window size
window_size = (900, 600)
game_display = pg.display.set_mode(window_size)
# Window title and window icon
pg.display.set_caption('Slither')
pg.display.set_icon(pg.image.load('apple.png'))

clock = pg.time.Clock()

fps = 15
snake_size = 20
apple_size = 45
movement = 20

snake_head = pg.image.load('snakehead.png')
apple = pg.image.load('apple.png')

# Display messages on screen function
def show_Msg(msg, coords, color=RED, font='verdana', fSize=30, fBold=False):
    font = pg.font.SysFont(font, fSize, bold=fBold)

    if coords[0] == 0:
        # finds the middle of text, then subtracts it from the middle of screen, so it's the center
        msg_center = font.size(msg)[0]
        coords = ((window_size[0] / 2) - (msg_center / 2), coords[1])

    # creates text to render with input from msg and color
    screen_text = font.render(msg, True, color)
    game_display.blit(screen_text, [coords[0], coords[1]])
    # this well not show the text ingame yet you have to do pg.display.update()

# Game Intro
def game_Intro():
    while True:
        show_Msg('Snake', (0, 100), WHITE, fSize=80)
        show_Msg('Q - Quit | SPACE - Begin', (0, 240), BLUE)
        pg.display.update()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_q:
                    quit()
                if event.key == pg.K_SPACE:
                    Main().main()

# Game over screen
def game_Over(score):
    while True:
        # prints stuff out to screen in red
        show_Msg('GAME OVER', (0, 250), fSize=80)
        show_Msg('C - Continue | Q - Quit', (0, 340))
        show_Msg('SCORE: %d'%score, (0, 380))
        pg.display.update()

        for event in pg.event.get():
            # Close window button to quit
            if event.type == pg.QUIT:
                quit()
            if event.type == pg.KEYDOWN:
                # Checks if event was q keypress for quit or c to continue
                if event.key == pg.K_q:
                    quit()
                elif event.key == pg.K_c:
                    Main().main()

# Pause game
def pause_Game(score):
    while True:
        show_Msg('PASUED', (0, 250), fSize=60)
        show_Msg('C - Continue | Q - Quit', (0, 340), BLUE)
        show_Msg('SCORE: %d'%score, (0, 380), GREEN)
        pg.display.update()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_q:
                    quit()
                elif event.key == pg.K_c:
                    return

# Random apple XY position
def rand_Apple():
    return rd(apple_size, window_size[0] - apple_size), \
           rd(apple_size, window_size[1] - apple_size)

# Draws snake
def snake(sSize, snake_list, snake_head):
    # draws snake head sprite
    game_display.blit(snake_head, (snake_list[-1]))
    # draws body of snake
    for i in range(len(snake_list[:-1])):
        pg.draw.rect(game_display, BROWN, [snake_list[i][0], snake_list[i][1], sSize, sSize])

class Main:
    # Main Game Loop


    @staticmethod
    def main():
        global new_snake_head, movement

        # sets position of snake
        leadX = window_size[0] / 2
        leadY = window_size[1] / 2
        leadX_Change = 0
        leadY_Change = -movement
        new_snake_head = snake_head
        snake_list = []
        snake_length = 0
        rand_appleX, rand_appleY = rand_Apple()

        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    quit()
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_SPACE:
                        pause_Game(snake_length)
                    elif event.key in (pg.K_LEFT, pg.K_a):
                        # Resets movement
                        leadX_Change = leadY_Change = 0
                        # Changes rotationn of snake head
                        new_snake_head = pg.transform.rotate(snake_head, 90)
                        # Change direction of correct axi
                        leadX_Change -= movement
                    elif event.key in (pg.K_RIGHT, pg.K_d):
                        leadX_Change = leadY_Change = 0
                        new_snake_head = pg.transform.rotate(snake_head, 270)
                        leadX_Change += movement
                    elif event.key in (pg.K_UP, pg.K_w):
                        leadX_Change = leadY_Change = 0
                        new_snake_head = pg.transform.rotate(snake_head, 0)
                        leadY_Change -= movement
                    elif event.key in (pg.K_DOWN, pg.K_s):
                        leadX_Change = leadY_Change = 0
                        new_snake_head = pg.transform.rotate(snake_head, 180)
                        leadY_Change += movement

            # sets background color. Redraws screen. Comment this to see affect.
            game_display.fill(BLACK)

            # shows score
            show_Msg(msg=str(snake_length), fSize=20, coords=(0, 10))

            # moves snake according to what you pressed
            leadX += leadX_Change
            leadY += leadY_Change

            # you can now go through a wall to go on the other side
            if (leadX > window_size[0]):
                leadX = 0
            elif (leadX < 0):
                leadX = window_size[0]
            elif (leadY > window_size[1]):
                leadY = 0
            elif (leadY < 0):
                leadY = window_size[1]

            # checks if you are in the X boundary of the apple
            if (leadX > rand_appleX) and (leadX < rand_appleX + apple_size) or \
            (leadX + snake_size > rand_appleX) and (leadX + snake_size < rand_appleX + apple_size):
                # checks Y boundary
                if (leadY > rand_appleY) and (leadY < rand_appleY + apple_size) or \
                (leadY + snake_size > rand_appleY) and (leadY + snake_size < rand_appleY + apple_size):
                    # hits apple
                    rand_appleX, rand_appleY = rand_Apple()
                    snake_length += 1

            # Snake head position
            snake_head_list = []
            # Adds current snake head position to snake_head
            snake_head_list.extend((leadX, leadY))
            snake_list.append(snake_head_list)
            # Draw snake
            snake(snake_size, snake_list, new_snake_head)

            # checks if you moved into a position where your snake body already is
            for segment in snake_list[:-1]:
                if snake_head_list == segment:
                    game_Over(snake_length)

            if len(snake_list) > snake_length:
                del snake_list[0]
                # makes sure snake length is the same as how many apples you picked up
                # this basically makes sure your snake isn't always growing when moving

            # Draw apple
            game_display.blit(apple, [rand_appleX, rand_appleY])

            # Updates screen then goes to next frame
            pg.display.update()
            clock.tick(fps)

        pg.quit()
        quit()

Main().main()
