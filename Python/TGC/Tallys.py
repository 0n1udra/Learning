from turtle import *
# imports turtle module, used to draw tallys

speed(10) # sets the speed of how fast it draws

def hund():
#Makes a big squre to indicate 100
    up()
    backward(5)
    right(90)
    forward(120)
    down()
    # moves the pointer in position

    for i in range(2):
        left(90)
        forward(155)
        left(90)
        forward(120)
    # makes the box

    up()
    left(90)
    forward(160)
    left(90)
    forward(8)
    right(90)
    down()
    # moves it to beginning position for next

def twent():
# moves up a row at 25 to make more room
        up()
        left(90)
        forward(28)
        right(90)
        back(150)
        down()

def slash():
# puts a slash on tallys for 5
    Pos = pos() # get's the current position

    up()
    forward(5)
    left(90)
    forward(3)
    right(90)
    down()
    # moves pointer in position

    goto(Pos[0] - 22, Pos[1] + 14)
    up()
    goto(Pos)
    forward(5)
    down()
    # draws the slash

def draw_Tally():
# draws tally line

    up()
    forward(5)
    down()
    # moves forward for next tally

    left(90)
    forward(20)
    backward(20)
    right(90)
    # drawing the line

def Main():
# main part of the program, gets how many tallys to draw, or to make a big square for 100
    x = int(input("Number > ")) # gets input
    i = S = T = H = 0 # sets variables 0
    for i in range(x):
        i += 1
        draw_Tally() # calls this function
        if i % 5 == 0: # checks to see if it's divisiobale by five, if so makes a slash
            S += 1
            slash()
        if i % 25 == 0: # checks to see if made 5 packs(25 tallys), then calls twent function, to move up a row
            T += 1
            twent()
        if i % 100 == 0: # if hundred makes a box
            H += 1
            hund()

    # prints out what it did
    print("Inputted number:", i)
    print("Number of Rows:", T)
    print("Hundreds:", H)


Main()
input("Enter to quit: ") # pasues the turtle so it doesn't quit when done