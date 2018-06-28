# Importing Modules
from tkinter import *
# Tkinter for the GUI and key-bindings
import tkinter.messagebox as mb
from tkinter import ttk
# ttk for styling the tkinter widgets
import threading as th
# threading so tkinter can run and listen for keys while a loop is running in the background
# import gpio
from time import sleep
# used for the pause fuction

### Global Variables ###
# sets global variables, which will be changes later
speed, cars, = None, None
mode = 1
run, pause = True, False
# gets data from train.txt. # of cars and speed
def getData():
    global speed, cars
    trainF = open('train.txt').readlines()
    # opens up train.txt and reads it by line. so trainF[0] would be everything on line 1 and so on......

    cars = int(trainF[0])
    # only reads first line from trainF to set as cars
    speed = int(trainF[1])
    # then sets second line to speed

### Light Functions ###
# shows red for x time, then go back to trafficLoop
def red(event=''):
    pauseF()
    # pauses the trafficLoop to run this. or you'll have both interfering with each other.
    for i in range(3):
        print("REEED")
        sleep(1)
    cont()
    # when this loop is done it'll continue the trafficLoop from where it was

def yellow(event=''):
    pauseF()
    for i in range(5):
        print("YELLOWW")
        sleep(1)
    cont()

def green(event=''):
    pauseF()
    for i in range(2):
        print("GREEEEN")
        sleep(1)
    cont()

### Traffic Loop Functions ###
# checks to see if to continue with loop
def check():
    if run is True and pause is False and cars > 0:
        statusLabel.config(text="trafficLabel STATUS : Running...", fg='green')
        pass
    # checks to see if run is True and have 1 or more cars from first line of train.txt. if so it'll continue the loop
    elif pause is True and run is True:
        try: pausedNoPrint()
        except: print("ERROR: CALLING pausedNoPrint | FROM check Func")
    # checks to see if pause and run is True. which means it'll pause it but will not print anything to console. used for green, yellow, and red functions
    elif run is False:
        try:
            statusLabel.config(text="trafficLoop STATUS : Paused", fg='orange')
            paused()
        except: print("ERROR: CALLING paused | FROM check Func")
    # checks to see if run is False, if so it'll pause the trafficLoop and print 'PAUSE' to console
    else: print("ERROR: check function issue | FROM check Func")
    # prints this if anything else happens

# starts trafficLoop
def start(event=''):
    global run
    # makes it so run is now in the scope of this function, basically so you can edit the global variable for other parts of the script to see
    run = True
    try: trafficThread.start()
    except: print("ERROR: CALLING trafficThread.start | FROM start Func")
    # starts the loop

# continues trafficLoop 
def cont(event=''):
    global run, pause
    run = True
    pause = False

# pauses the loop.
def stop(event=''):
    global run, pause
    run = False
    pause = True

def pauseF():
    global pause
    pause = True

# pauses trafficLoop. and prints 'PAUSE' every 2s
def paused(event=''):
    while pause:
        print('PAUSED')
        sleep(2)

def pausedNoPrint(event=''):
    while pause: pass

# quits script
def quitF(event=''):
    global run, Exit
    print("QUIT")
    run = False
    exit()

# Main traffic light loop. this keeps repeating, unless you call other functions
def trafficLoop():
    global speed, cars, run, mode
    while run:
        getData()
        check()
        # if 0 trians, it'll stop the loop
        if cars >= 3:
            sleep(1)
            mode = 2
            print('green >>  yellow')
            green()
        if mode == 2:
            sleep(1)
            mode = 3
            print("yellow >> red")
            rTime = int(speed * 0.12)
            print("RED light for: ", rTime)
            for i in range(rTime):
                check()
                print("<<Red>>")
                sleep(1)

            print('Green >>  Yellow')
            #### RED ###
        if mode == 2:
            yTime = int(speed * .08)
            print("YELLOW Light for: ", yTime)
            for i in range(yTime):
                check()
                print('<<Yellow>>')
                sleep(1)
            mode = 3
            print("Yellow >> Red")

        if mode == 3:
            gTime = int(speed * 0.2)
            print("GREEN light for: ", gTime)
            for i in range(gTime):
                check()
                print("<<Green>>")
                sleep(1)
            print("Green >> Yellow")

### GUI and Keyboard interaction ###
def tkinter():
    global statLabel, statusLabel
    root = Tk()

    # Window name
    root.title("Listener")
    ### Left Frame ###
    topFrame = Frame(root)
    topFrame.pack(side=LEFT)


    ### Key-bindings ###
    # changes light color
    root.bind('<g>', green)
    root.bind('<y>', yellow)
    root.bind('<r>', red)
    # starts trafficLoop
    root.bind('<space>', start)
    # pauses trafficLoop
    root.bind('<q>', stop)
    # continues trafficLoop
    root.bind('<w>', cont)
    # quits program
    root.bind('<p>', quitF)


    ### Buttons ###
    # trafficLoop is the main loop, unless you press other buttons to make temporary affects then goes back to loop.
    # Starts trafficLoop
    startB = ttk.Button(topFrame, text='START', command=start).pack()
    # turns to green,yellow, and red light then back to trafficLoop
    redB = ttk.Button(topFrame, text='Red', command=red).pack()
    yellowB = ttk.Button(topFrame, text='Yellow', command=yellow).pack()
    greenB = ttk.Button(topFrame, text='Green', command=green).pack()
    # pauses trafficLoop. prints 'PAUSE' every 2s, until you press w
    pauseB = ttk.Button(topFrame, text='Pause', command=stop).pack()
    # continues trafficLoop
    contB = ttk.Button(topFrame, text='Cont', command=cont).pack()
    # quits the program
    quitB = ttk.Button(topFrame, text='QUIT', command=quitF).pack()

    rightFrame = Frame(root)
    rightFrame.pack(side=RIGHT)

    statusLabel = Label(rightFrame)
    statusLabel.pack()
    statusLabel.config(text="trafficLoop STATUS: Off", fg='red')

    #root.focus_force()
    root.mainloop()

# creates 2 threads
tkinterThread = th.Thread(target=tkinter)
trafficThread = th.Thread(target=trafficLoop, daemon=True)
tkinterThread.run()
tkinterThread.join()
trafficThread.join()



