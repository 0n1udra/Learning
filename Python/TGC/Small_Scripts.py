from getpass import getpass as gp
from time import sleep
from matplotlib.pyplot import *
import pyglet


def login():
    accounts = {'drake': 'Kirby550'}

    for i in range(2):
        name = input("Name > ").lower()
        passwd = input("Pass > ")
        if name in list(accounts.keys()):
            if passwd == accounts[name]:
                print("Welcome!")
                break

    print("To Many Failed Attempts")

def weather():
    ###### read wather data #####
    # ask for filename
    #inputFile = input("Ope file > ") # ask for name of file, (need file attribute(.csv))
    #dataFile = open(inputFile, "r") # opens file
    dataFile = open("weatherData.csv", 'r')
    # read data from file
    dates, temps = [], []
    for i in dataFile: # goes through each line and puts it in variable 'i', then runs the code, and chages the variable
        d = i.split(',')
        print(d[0:2], d[-5:-1])
        dates.append(d[0:2])
        temps.append(d[-5:-1])
        sleep(.00001)
    print('Done loading data')
    sleep(3)
    def checkTemp():
        global dates, temps
        inp = input("Wanna find temps? Date > ")
        if inp in dates:
            ind = dates.index(inp)
            print("Date", dates[ind])
            print("Temps", temps[ind])
            input("\nEnter to continue")
            checkTemp()
    checkTemp()

    dataFile.close()

def turtle_Shapes():
    def spiral(gap=20):
        c_rad = gap
        while not stay_In():
            circum = 2 * 3.14159 * c_rad
            frac = 1 / circum

            left(frac * 360)
            forward(1)
            c_rad += gap * frac

    def sqr_Spiral():
        pass

def plots():

    balance = float(input("Current Balance > "))
    interest = float(input("Interest > "))
    interestM = float(input("Interest Goes up > "))
    STOP = int(input("Stop Time > "))
    time = 0
    timelist = []
    balancelist = []

    interestlist = []

    while (time < STOP):
        balance += balance * interest
        interest += interest * interestM
        interestlist.append(interest)
        time += 1
        timelist.append(time)
        balancelist.append(balance)

    for i in range(len(timelist)):
        print("Year: ", timelist[i], "  Balance: ", str(balancelist[i])[:6], "  Interest: ", str(interestlist[i])[:5])

    axis([0, time, 0, balance])
    plot(timelist, balancelist, label='Money Over Time', marker="X", color='green')
    plot(timelist, interestlist, label='Interest!', marker='X', color='yellow')
    legend()
    show()

def GUE():

    windows = pyglet.windows.Window(width=400, height=300, caption="Pyglet")

    pyget.app.run()

    input()
