from tkinter import *
import tkinter.messagebox as mb
from tkinter import ttk
<<<<<<< HEAD
import trafficLight

root = Tk()
root.title("Listener")

def buttons():
	topFrame = Frame(root)
	topFrame.pack(side=TOP)
	
	green = Button(topFrame, text='Green', fg='green')
	yellow = Button(topFrame, text='Yellow', fg='yellow')
	red = Button(topFrame, text='Red', fg='red')
	
	green.pack(side=LEFT)
	yellow.pack(side=LEFT)
	red.pack(side=LEFT)

buttons()
=======
import _thread as th

# import gpio
from time import sleep
import math

speed, cars = None, None

run = True
# speed of train

def getData():
	global speed, cars
	trainF = open('train.txt').readlines()
	# opens up train.txt and reads it
	cars = int(trainF[0])
	# only reads first char from trainF
	speed = int(trainF[1])


def red(event): print("REEED")

def yellow(event): print("YELLOWW")

def green(event): print("GREEEEN")

def start(event):
	global run
	run = True
	trafficLoop()
def stop(event):
	global run
	run = False

def trafficLoop():
	global speed, cars, run
	mode = 1
	while run:
		getData()
		print('# of cars: ' + str(cars))
		if cars == 0: break
		# if 0 trians, it'll stop the loop
		if cars >= 3 and run == True:
			sleep(1)
			mode = 2
			rTime = int(speed * 0.12)
			print("RED light for: ", rTime)
			for i in range(rTime):
				print("<<Red>>")
				sleep(1)

			print('Green >>  Yellow')
			#### RED ###
		if mode == 2:
			yTime = int(speed * .08)
			print("YELLOW Light for: ", yTime)
			for i in range(yTime):
				print('<<Yellow>>')
				sleep(1)
			mode = 3
			print("Yellow >> Red")

		if mode == 3:
			gTime = int(speed * 0.2)
			print("GREEN light for: ", gTime)
			for i in range(gTime):
				print("<<Green>>")
				sleep(1)
			print("Green >> Yellow")
			yellow()
		print(stop)
	print(run)


def tkinter():
	root = Tk()
	root.title("Listener")
	topFrame = Frame(root)
	topFrame.pack(side=TOP)

	greenB = ttk.Button(topFrame, text='Green', command=green).pack()
	yellowB = ttk.Button(topFrame, text='Yellow', command=yellow).pack()
	redB = ttk.Button(topFrame, text='Red', command=red).pack()
	startB = ttk.Button(topFrame, text='Start', command=start).pack()
	stopB = ttk.Button(topFrame, text='STOP', command=stop).pack()
	#
	# start.pack(side=LEFT)
	# greenB.pack(side=LEFT)
	# yellowB.pack(side=LEFT)
	# redB.pack(side=LEFT)
	# stop.pack(side=LEFT)

	def quitF(event): quit()
	root.bind('<g>', green)
	root.bind('<y>', yellow)
	root.bind('<r>', red)
	root.bind('<q>', stop)
	root.bind('<space>', start)
	root.bind('<p>', quitF)

	root.mainloop()
th.start_new_thread(trafficLoop, ())
th.start_new_thread(tkinter, ())

>>>>>>> iol
